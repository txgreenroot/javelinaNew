import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/rooms"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Look for gallery container structure
print("Page structure:")
print("=" * 50)

# Find main content areas
sections = soup.find_all(['section', 'div'], class_=True)
for section in sections[:10]:
    classes = ' '.join(section.get('class', []))
    if 'galler' in classes.lower() or 'grid' in classes.lower() or 'masonry' in classes.lower():
        print(f"Found: {section.name} with classes: {classes}")

# Check if there's a grid or column structure
print("\nLooking for grid/column patterns...")
grid_elements = soup.find_all(['div'], class_=lambda x: x and ('grid' in str(x).lower() or 'column' in str(x).lower() or 'row' in str(x).lower()))
for elem in grid_elements[:5]:
    print(f"Grid element: {elem.get('class')}")
