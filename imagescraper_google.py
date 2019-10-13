import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_images(url, query, number_of_imgs):
    # Open url
    r = requests.Session()

    res = r.get(url+query)
    res.raise_for_status()

    # Parse result to BeautifulSoup
    soup = BeautifulSoup(res.content, 'html.parser')

    # Find all <img> tags
    images = soup.findAll('img')

    # Iterate through <img> tags to extract image src
    i = 0
    for image in images[0:int(number_of_imgs)]:
        i += 1
        image_url = image.get('src')
        image_name = f'img {str(i)}.jpg'
        image_data = r.get(image_url)
        image_data.raise_for_status()

        folder = Path(f'temp/{query.capitalize()}/')
        folder.mkdir(parents=True, exist_ok=True)
        filepath = folder / image_name

        with filepath.open('wb') as file:
            for chunk in image_data.iter_content(100000):
                file.write(chunk)