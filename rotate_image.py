#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("tatras.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
rotated = tatras.rotate(180)
rotated.save('tatras_rotated.jpg') 
