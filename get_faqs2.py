import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/about"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get main content - remove scripts, styles, headers, footers
for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
    tag.decompose()

# Get text content
text = soup.get_text()

# Clean up whitespace
lines = [line.strip() for line in text.split('\n') if line.strip()]

# Print the content
in_faq = False
for line in lines:
    if 'How far are you' in line or in_faq:
        in_faq = True
        print(line)
        if 'reach you' in line:
            # Print a few more lines after the last question
            continue
