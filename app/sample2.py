# -*- coding: utf-8 -*-

from SimpleCV import *


if __name__ == '__main__':

    # Load and show the main image
    main = Image('image2.jpg')

    bg = Image('background.jpg')

    # Create the mask to apply and show the mask
    # mask = main.hueDistance(color=Color.GREEN, minsaturation=170, minvalue=80).binarize()
    mask = main.hueDistance(color=(0, 192, 95), minsaturation=130, minvalue=35).binarize()

    mask.save('mask.jpg')

    # Combine the mask and other images to get the final result
    result = (main - mask) + (bg - mask.invert())
    result.save('output.jpg')
