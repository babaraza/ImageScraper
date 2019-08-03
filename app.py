import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Define target url
url = "https://www.google.com"

# Open url
r = requests.Session()
res = r.get(url)
res.raise_for_status()

# Parse result to BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')

# Find all <img> tags
images = soup.findAll('img')

# Iterate through <img> tags to extract image src
for image in images:
    image_url = url + image.get('src')
    image_ext = image_url[-4:]
    image_name = image_url[image_url.rfind('/')+1:-4]
    image_data = r.get(image_url)
    image_data.raise_for_status()

    filename = Path(image_name + image_ext)

# Check if image already exists
    if filename.exists():
        print(f'{filename} already exists')
    else:
        with open(filename, 'wb') as file:
            for chunk in image_data.iter_content(100000):
                file.write(chunk)

    print("Done")
