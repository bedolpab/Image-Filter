from pkgutil import get_data
from PIL import Image


def filter(img,
           rgb_r, rgb_g, rgb_b):
    """ Returns manipulated image given parameters.

    :param img: Image to work on.
    :param rgb_r: RGB value of red.
    :param rgb_g: RGB value of green.
    :param rgb_b: RGB value of blue.

    """
    # Sizes
    width, height = img.size

    # Get pixel data
    get_pixels = img.getdata()
    pixels = []

    # Append data to pixel list
    for i in get_pixels:
        pixels.append(i)

    pixel_location = 0

    while pixel_location < len(pixels):
        p = pixels[pixel_location]

        # Location in p-tuple
        r, g, b = p[0], p[1], p[2]

        # Update with absoloute value difference
        r = abs(r - rgb_r)
        g = abs(g - rgb_g)
        b = abs(b - rgb_b)

        pixels[pixel_location] = (r, g, b)
        pixel_location += 1

    new_image = Image.new("RGB", size=(width, height))
    new_image.putdata(pixels)

    return new_image
