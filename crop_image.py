#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("tatras.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
cropped = tatras.crop((100, 100, 350, 350))
cropped.save('tatras_cropped.jpg')
