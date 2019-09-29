import imagescraper
import imagescraper_google

init_question = input('Extract images from (S)ingle page or (G)oogle images > ')

if init_question.lower() == "s":
    url = input('Enter url for page (without http) > ')
    imagescraper.get_images('http://' + url)

elif init_question.lower() == "g":
    base_url = 'https://www.google.com/search?safe=strict&tbm=isch&q='
    url = input('Enter search string for Google Images > ')
    quant = input('Number of pictures to pull > ')
    imagescraper_google.get_images(base_url+url, quant)

else:
    print('Invalid Input')

print("Done")
