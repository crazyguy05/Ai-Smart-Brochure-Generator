# AI Smart Brochure Generator

## 1. Overview

The **AI Smart Brochure Generator** is an AI-powered application that automatically creates a concise, professional brochure for a company using information extracted from its website.
The system scrapes relevant pages from a given company website, intelligently selects important links (such as About, Blogs, Careers, and social profiles), and then uses a **Large Language Model (LLM)** to generate a structured brochure suitable for customers, investors, and potential recruits.
This project demonstrates **end-to-end AI engineering**, including web scraping, prompt engineering, LLM orchestration, and a simple interactive UI.

---

## 2. Key Features
1. Website scraping to extract text content and links from company websites  
2. AI-based relevant link selection using an LLM  
3. Automated brochure generation in structured Markdown format  
4. Interactive user interface built with Streamlit  
5. Local LLM execution using Ollama with no cloud dependency  

---

## 3. How It Works (High-Level Architecture)

1. The user enters a company name and website URL  
2. The scraper extracts:
   - Landing page content  
   - All website links  
3. An LLM filters the links to identify the most relevant ones  
4. Content from selected pages is aggregated  
5. Another LLM prompt generates a company brochure  
6. The brochure is displayed in the Streamlit web interface  

---

## 4. Tech Stack

- Python  
- Streamlit – User interface  
- Ollama – Local LLM inference  
- OpenAI-compatible SDK – Communication with the LLM  
- BeautifulSoup – HTML parsing  
- Requests – HTTP requests  
- python-dotenv – Environment variable management  

---

## 5. LLM Usage Notes

This project uses a **local LLM via Ollama** (for example, `llama3.x` models), which enables:

1. No API costs  
2. Full local execution  
3. Privacy-friendly experimentation  

**Important Note:**  
Because local models are smaller and less strictly controlled than cloud-based LLMs, brochure quality and JSON consistency may vary.

Using a **cloud-based LLM** (such as OpenAI GPT-4 or GPT-4.1) can significantly improve:

1. Brochure quality and richness  
2. Link relevance selection  
3. Structured JSON reliability  
4. Overall response consistency  

The system is intentionally designed so that switching to a cloud-based LLM requires **minimal code changes**.

---

## 6. How to Run Locally

### 6.1 Prerequisites

- Python 3.10 or higher  
- Ollama installed and running  
- A supported Ollama model pulled locally:

```bash
ollama pull llama3.2:1b

git clone https://github.com/yourusername/ai-smart-brochure-generator.git
cd ai-smart-brochure-generator

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt

streamlit run app.py

ai-smart-brochure-generator/
│
├── app.py                    # Streamlit UI
├── brochure_generator.py     # AI and LLM logic
├── scraper.py                # Website scraping utilities
├── requirements.txt
├── README.md
└── notebooks/                # Optional exploration notebooks

8. Future Improvements
Support for cloud-based LLMs with a model selector
Improved JSON reliability for small local models
Optional brochure export (PDF or other formats)
Caching scraped content for faster performance
UI enhancements and configuration options
