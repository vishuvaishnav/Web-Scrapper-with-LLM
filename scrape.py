from selenium.webdriver as webdriver
from selenium.webdriver.chromium.service import Service
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time


def scrape_website(url):
    print("Launching Chorme Browser.......")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service())
    try :
      driver.get(url)
      print("Page Loaded.....")
      html = driver.page_source
      time.sleep(5)

      return html
    finally:
      driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]