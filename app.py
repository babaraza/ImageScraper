import requests
from bs4 import BeautifulSoup
from pathlib import Path

url = "https://www.google.com"

r = requests.Session()
res = r.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, 'html.parser')

images = soup.findAll('img')


for image in images:
    image_url = url + image.get('src')
    image_ext = image_url[-4:]
    image_data = r.get(image_url)
    image_data.raise_for_status()

    filename = Path('logo.png' + image_ext)

    if filename.exists():
        print(f'{filename} already exists')
    else:
        with open(filename, 'wb') as file:
            for chunk in image_data.iter_content(100000):
                file.write(chunk)

    print("Done")
