#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

try:
    tatras = Image.open("tatras.jpg")

except:
    print("Unable to load image")
    sys.exit(1)
    
idraw = ImageDraw.Draw(tatras)
text = "High Tatras"

font = ImageFont.truetype("arial.ttf", size=18)

idraw.text((10, 10), text, font=font)
 
tatras.save('tatras_watermarked.png')
