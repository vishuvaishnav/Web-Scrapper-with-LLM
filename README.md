```markdown
AI Web Scraper

This project is an AI-powered web scraper built with Streamlit and LangChain, designed to automate web content extraction and parsing. It scrapes webpage data, cleans up the content, and uses an AI model to extract specific information based on user-provided descriptions. Ideal for cases where you need precise data from webpages without the extra clutter!

Features

- Website Scraping: Connects to a remote Chrome instance to load and scrape website content, with support for handling CAPTCHA challenges.
- Content Extraction & Cleaning: Extracts the main body content from HTML, removing scripts, styles, and irrelevant text to produce a clean dataset.
- AI-Driven Parsing: Uses a model from LangChain to identify and retrieve content relevant to user queries, enabling precise data extraction.
- Customizable Output: Splits large DOM content into manageable chunks and only extracts information as per the given instructions.

Project Structure

- main.py: Streamlit-based UI where users enter a URL and define their query, enabling an interactive experience.
- scrape.py: Contains functions to connect to a Chrome WebDriver, extract webpage body content, clean it, and split it into chunks.
- parse.py: Handles AI-powered parsing of the content using LangChain Ollama, returning only the information specified by the user.

Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/vishuvaishnav/Web-Scrapper-with-LLM.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Chrome WebDriver URL:
     ```
     SBR_WEBDRIVER=<your_chrome_webdriver_url>
     ```

4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Usage

1. Open the app in your browser and enter the URL of the webpage you wish to scrape.
2. Click "Scrape Website" to start scraping the content.
3. After scraping, enter a description of the specific information you need.
4. Click "Parse Content" to view the parsed results based on your query.

## Requirements

- Python 3.8+
- Streamlit
- BeautifulSoup4
- LangChain and LangChain Ollama (for AI parsing)
- Selenium WebDriver with Chrome or Chromium

## Future Improvements

- **CAPTCHA Solver**: Enhanced automation to handle more complex CAPTCHA challenges.
- **More Parsing Models**: Support for additional AI models to provide more customization options.
- **Additional Export Formats**: Enable results export to CSV or JSON for easier data handling.

## Author
**Vishu Vaishnav**
