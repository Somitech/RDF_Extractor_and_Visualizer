import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    if url.startswith('http'):
        response = requests.get(url)
        page_content = response.content
    else:
        with open(url, 'r', encoding='utf-8') as file:
            page_content = file.read()
    
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text()
    return text
