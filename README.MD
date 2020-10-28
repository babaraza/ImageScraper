[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Image Scraper
Script to get images from a specified URL or from Google Images

### Usage

Run `app.py` in Python shell or CMD/Terminal and it will prompt user:

`Extract images from (S)ingle page or (G)oogle images > `

### Single Page
The script will follow the steps:
- Prompt user for the URL to scrape for images:
  - `Enter url for page (without http) > '`
- It will then go to URL and find all `<img>` tags
- Get the `src` for each
- Get each `img` and write to memory
- Name the `file` the same name as the remote image file
- Then save with the correct *extension*

### Google Images
The script will follow the steps:
- Prompt user for the search string to use on Google Image search: 
  - `Enter search string for Google Images > `
- It will then prompt user for number of images to pull:
  - Ask `Number of images to pull > `
- Go to Google Images and search for user search string 
- Find all `<img>` tags
- Get the `src` for each
- Get each `img` and write to memory
- Name the `file` as `img [i].jpg`
  - where `i` gets automatically incremented for each image found
- Then save with the `.jpg` extension