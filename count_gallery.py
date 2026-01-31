import requests
from bs4 import BeautifulSoup

url = "https://www.javelinahideout.com/rooms"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all images
images = soup.find_all('img')

# Filter out small icons, logos, etc - only count gallery images
gallery_images = [img for img in images if img.get('src', '').startswith('https://static.wixstatic.com')]

print(f"Total images on original gallery page: {len(images)}")
print(f"Gallery images (from wixstatic): {len(gallery_images)}")
print("\nGallery image URLs:")
for img in gallery_images[:20]:  # Show first 20
    print(img.get('src', '')[:100])
