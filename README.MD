[![Python 3.7](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Image Scraper
###### Gets all the images from a URL and downloads them

### Usage

Run `app.py` with target URL

The script will follow the steps:
- Go to URL and find all `<img>` tags
- Get the `src` for each
- Get each `img` and write to memory
- Name the `file` the same name as the remote image file
- Then save with the correct *extension*