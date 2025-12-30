The AI Smart Brochure Generator is an AI-powered application that automatically creates a concise, professional brochure for a company using information extracted from its website.
The system scrapes relevant pages from a given company website, intelligently selects important links (such as About, Blogs, Careers, and social profiles), and then uses a Large Language Model (LLM) to generate a structured brochure suitable for customers, investors, and potential recruits.
This project demonstrates end-to-end AI engineering, including web scraping, prompt engineering, LLM orchestration, and a simple interactive UI.

🚀 Key Features
🌐 Website Scraping – Extracts text content and links from company websites
🔗 Relevant Link Selection – Uses an LLM to identify important pages for brochure creation
🧠 AI-Powered Brochure Generation – Generates a readable, structured brochure in Markdown
🖥 Interactive UI – Built using Streamlit for easy user interaction
🏠 Local LLM Execution – Uses Ollama to run models locally without cloud dependency
🧠 How It Works (High-Level Architecture)

User enters a company name and website URL
The scraper extracts:
Main landing page content
All website links
An LLM filters the links to find the most relevant ones
Content from selected pages is aggregated
Another LLM prompt generates a company brochure
The brochure is displayed in the Streamlit web interface

🛠 Tech Stack
Python
Streamlit – UI for interaction
Ollama – Local LLM inference
OpenAI-compatible SDK – Used to communicate with Ollama
BeautifulSoup – HTML parsing
Requests – HTTP requests
python-dotenv – Environment variable management

🤖 LLM Usage Notes
This project uses a local LLM via Ollama (e.g. llama3.x models), which allows:
No API costs
Full local execution
Privacy-friendly experimentation

 Important Note:
Because local models are smaller and less strictly controlled than cloud-based LLMs, the generated brochure quality and JSON consistency may vary.

Using a cloud-based LLM (such as OpenAI GPT-4 / GPT-4.1) can significantly improve:
Brochure quality and richness
Link relevance selection
Structured JSON responses
Overall reliability
The system is intentionally designed so that switching to a cloud-based LLM requires minimal code changes.

How to Run Locally
Prerequisites
Python 3.10+
Ollama installed and running
A supported Ollama model pulled locally (example):
ollama pull llama3.2:1b

2️⃣ Clone the Repository
git clone https://github.com/yourusername/ai-smart-brochure-generator.git
cd ai-smart-brochure-generator

3️⃣ Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Application
streamlit run app.py

 Project Structure
ai-smart-brochure-generator/
│
├── app.py                    # Streamlit UI
├── brochure_generator.py     # AI & LLM logic
├── scraper.py                # Website scraping utilities
├── requirements.txt
├── README.md
└── notebooks/                # (Optional) exploration notebooks

🔮 Future Improvements
Support for cloud-based LLMs with a model selector
Improved JSON reliability for small local models
Optional PDF export of brochures
Caching scraped content for faster performance
UI enhancements and configuration options
