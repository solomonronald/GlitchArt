__author__ = 'Solomon'

import os
import Image
from glitching import sort_image
var = raw_input("Enter path of image to glitch: ")

img_file = Image.open(var)

img = img_file.convert("RGBA")

filename = os.path.splitext(var)[0]

# glitching algorithm

img = sort_image.glitch_one(img)

img.save(filename+"_glitched.png")
img.show()

