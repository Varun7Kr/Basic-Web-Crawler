import random

import urllib.request

def download_web(url):
    name=random.randrange(1, 1000)
    fullname=str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download_web("https://duckduckgo.com/i/91f6e0d8.png")
