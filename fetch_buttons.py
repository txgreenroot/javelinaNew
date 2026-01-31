import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links
links = soup.find_all('a')

# Look for gallery and FAQ related links
print("Links containing 'gallery' or 'faq':")
for link in links:
    text = link.get_text().strip().lower()
    href = link.get('href', '')
    if 'gallery' in text or 'faq' in text or 'gallery' in href.lower() or 'faq' in href.lower():
        print(f"Text: {link.get_text().strip()}")
        print(f"Href: {href}")
        print(f"Classes: {link.get('class', [])}")
        print(f"OnClick: {link.get('onclick', '')}")
        print("---")
