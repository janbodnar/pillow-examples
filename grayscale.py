#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("tatras.jpg")
    
except IOError:
    print("Unable to load image")
    sys.exit(1)
    
grayscale = tatras.convert('L')
grayscale.show()
