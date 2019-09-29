[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Image Scraper
Can get images from a URL or from Google Images

### Usage

Run `app.py` and it will ask you:

`Extract images from (S)ingle page or (G)oogle images > `

### Single Page
The script will follow the steps:
- Ask `Enter url for page (without http) > '`
- Go to URL and find all `<img>` tags
- Get the `src` for each
- Get each `img` and write to memory
- Name the `file` the same name as the remote image file
- Then save with the correct *extension*

### Google Images
The script will follow the steps:
- Ask `Enter search string for Google Images > `
- Ask `Number of pictures to pull > `
- Go to Google Images and search for user search string 
- Find all `<img>` tags
- Get the `src` for each
- Get each `img` and write to memory
- Name the `file` as `img [i].jpg`
- Then save with the `.jpg` extension