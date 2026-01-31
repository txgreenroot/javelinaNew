import requests
from bs4 import BeautifulSoup
import os

url = "https://www.javelinahideout.com/rooms"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create the images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Find all images from wixstatic
images = soup.find_all('img')
gallery_images = []

for img in images:
    src = img.get('src', '')
    if 'static.wixstatic.com/media/875dec_' in src:
        # Extract the base URL (before /v1/)
        base_url = src.split('/v1/')[0]
        # Get the image ID from the URL
        image_id = base_url.split('875dec_')[1].split('~')[0]
        gallery_images.append((base_url, image_id))

print(f"Found {len(gallery_images)} unique gallery images")

# Download each image
for i, (url, image_id) in enumerate(gallery_images, 1):
    try:
        filename = f'images/gallery_{i:02d}_{image_id[:8]}.jpg'
        
        # Skip if already exists
        if os.path.exists(filename):
            print(f"Skipping {filename} (already exists)")
            continue
            
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

print(f"\nDownload complete. Total images: {len(gallery_images)}")
