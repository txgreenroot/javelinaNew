import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Remove scripts and styles
for tag in soup(['script', 'style', 'nav', 'footer']):
    tag.decompose()

# Find all headings and images in order
elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'img'])

print("Page structure in order:")
print("=" * 60)

for i, elem in enumerate(elements[:50]):  # First 50 elements
    if elem.name == 'img':
        src = elem.get('src', '')
        if 'wixstatic' in src:
            # Get image ID
            img_id = src.split('875dec_')[1].split('~')[0] if '875dec_' in src else 'unknown'
            alt = elem.get('alt', 'no alt')[:50]
            print(f"{i}. IMAGE: {img_id[:10]}... ({alt})")
    elif elem.name in ['h1', 'h2', 'h3']:
        text = elem.get_text().strip()
        if text and len(text) < 100:
            print(f"{i}. {elem.name.upper()}: {text}")
    elif elem.name == 'p':
        text = elem.get_text().strip()
        if text and len(text) > 20 and len(text) < 150:
            print(f"{i}. TEXT: {text[:80]}...")
