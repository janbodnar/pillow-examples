#!/usr/bin/python3

from PIL import Image
import requests
import sys

url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'

try:
    resp = requests.get(url, stream=True).raw

except requests.exceptions.RequestException as e:  
    sys.exit(1)

try:
    img = Image.open(resp)

except IOError:
    print("Unable to open image")
    sys.exit(1)

img.save('sid.jpg', 'jpeg') 
