import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_images(url):
    # Open url
    r = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    res = r.get(url, headers=headers)
    res.raise_for_status()

    # Parse result to BeautifulSoup
    soup = BeautifulSoup(res.content, 'html.parser')

    # Find all <img> tags
    images = soup.findAll('img')

    # Iterate through <img> tags to extract image src
    for image in images:
        image_url = url + image.get('src')
        image_ext = image_url[-4:]
        image_name = image_url[image_url.rfind('/') + 1:-4]
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