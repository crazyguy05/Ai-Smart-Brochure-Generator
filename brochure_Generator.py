# brochure_generator.py

import json
from openai import OpenAI
from scraper import fetch_website_links, fetch_website_contents

# =========================
# Ollama configuration
# =========================

MODEL = "llama3.2:1b"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"
)

# =========================
# Link selection prompts
# =========================

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company.

Include the homepage if present.
Include blog pages and recent blog posts if relevant.
Include social media profiles if they represent the company or individual.
Include external companies closely associated with the brand.
Be inclusive rather than minimal.

Respond ONLY with valid JSON in the following format:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(url: str) -> str:
    user_prompt = f"""
Here is the list of links on the website {url}.
Please decide which of these are relevant for a company brochure.

Do not include Terms of Service, Privacy, or email links.

Links:
"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt


def select_relevant_links(url: str) -> dict:
    response = ollama.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ]
    )

    raw = response.choices[0].message.content.strip()

    # Try direct JSON parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Try to extract JSON manually
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start != -1 and end != -1:
            try:
                return json.loads(raw[start:end])
            except json.JSONDecodeError:
                pass

    # Fallback (never crash app)
    return {"links": []}

# =========================
# Content aggregation (RAG)
# =========================

def fetch_page_and_all_relevant_links(url: str) -> str:
    contents = fetch_website_contents(url)
    relevant_links = select_relevant_links(url)

    result = f"## Landing Page\n\n{contents}\n\n## Relevant Links\n"

    for link in relevant_links["links"]:
        result += f"\n\n### {link['type']}\n"
        result += fetch_website_contents(link["url"])

    return result

# =========================
# Brochure prompts
# =========================

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors, and recruits.

Base all statements strictly on the provided content.
Do not invent information.
Respond in markdown without code blocks.
"""

def get_brochure_user_prompt(company_name: str, url: str) -> str:
    user_prompt = f"""
You are looking at a company called {company_name}.

Below is content from its landing page and other relevant pages.
Use this information to create a short brochure in markdown.
"""
    user_prompt += fetch_page_and_all_relevant_links(url)

    # keep prompt size manageable for local models
    return user_prompt[:5000]

# =========================
# Main brochure generator
# =========================

def create_brochure(company_name: str, url: str) -> str:
    response = ollama.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ]
    )
    return response.choices[0].message.content

import streamlit as st

def stream_brochure_streamlit(company_name, url):
    stream = ollama.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
        stream=True
    )

    response = ""
    placeholder = st.empty()

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            response += delta
            placeholder.markdown(response)

    return response
