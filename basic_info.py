#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("tatras.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
print("Format: {0}\nSize: {1}\nMode: {2}".format(tatras.format, 
    tatras.size, tatras.mode))
