__author__ = 'Solomon'


def glitch_one(img):

    pix_data = img.load()

    for x in xrange(img.size[0]):

        y_list = []

        for y in xrange(img.size[1]):
            y_list.append(pix_data[x, y])

        y_list.sort()

        for y in xrange(img.size[1]):
            pix_data[x, y] = y_list[y]

    return img
