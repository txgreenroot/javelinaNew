import os
import requests

# Create the images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# List of images to download (url, filename)
images = [
    ('https://static.wixstatic.com/media/875dec_4703b0fe0680409a979460c16ac8d184~mv2.jpg', 'images/compound_sunset.jpg'),
    ('https://static.wixstatic.com/media/875dec_75de99393c3a4186b6387ecff57cf4ab~mv2.jpg', 'images/east_porch.jpg'),
    ('https://static.wixstatic.com/media/875dec_c0c0144e38484936bb9875fe17f58bab~mv2.jpg', 'images/firepit.jpg'),
    ('https://static.wixstatic.com/media/875dec_2d182f1f49524be598722ee811472be6~mv2.jpg', 'images/west_porch_sunset.jpg')
]

for url, filename in images:
    try:
        # The wix URLs don't have a file extension, so we need to get the raw image data
        # The part of the URL before '/v1/' seems to be the image identifier.
        base_url = url.split('/v1/')[0]
        
        response = requests.get(base_url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

print("Image download script finished.")
