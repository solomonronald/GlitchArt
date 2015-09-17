__author__ = 'Solomon'

def removewhite(img1):
    "function_docstring"

    pixdata = img1.load()

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in xrange(img1.size[1]):
        for x in xrange(img1.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (0, 0, 0, 255)

    return img1