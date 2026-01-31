import requests
from bs4 import BeautifulSoup
import re

url = "https://www.javelinahideout.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Look for animation-related classes and data attributes
print("Looking for animation-related attributes:\n")

# Find elements with animation/transition classes
elements = soup.find_all(attrs={'class': re.compile(r'(animate|animation|fade|slide|zoom|parallax|reveal|entrance)', re.I)})
print(f"Found {len(elements)} elements with animation classes\n")

for i, elem in enumerate(elements[:10]):
    print(f"{i+1}. Tag: {elem.name}")
    classes = elem.get('class', [])
    print(f"   Classes: {' '.join(classes) if classes else 'none'}")
    
    # Check for data attributes
    data_attrs = {k: v for k, v in elem.attrs.items() if k.startswith('data-')}
    if data_attrs:
        for k, v in data_attrs.items():
            print(f"   {k}: {v}")
    print()

# Look for style attributes with transform/transition
print("\n\nLooking for inline styles with animations:")
styled_elements = soup.find_all(style=re.compile(r'(transform|transition|animation)', re.I))
for elem in styled_elements[:5]:
    print(f"Tag: {elem.name}")
    print(f"Style: {elem.get('style', '')[:200]}")
    print()
