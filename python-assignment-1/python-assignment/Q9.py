import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        print(f"Found {len(links)} links. Sample:", links[:5])
    except Exception as e:
        print(f"Error scraping: {e}")

scrape_links("https://www.python.org")