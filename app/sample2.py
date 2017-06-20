# -*- coding: utf-8 -*-

from SimpleCV import *


if __name__ == '__main__':

    # Load and show the main image
    main = Image("image.jpg")

    # Create the mask to apply and show the mask
    mask = main.hueDistance(color=(118, 251, 77), minsaturation=100, minvalue=80).binarize()

    mask.save('output-mask2.jpg')

    # Combine the mask and other images to get the final result
    result = (main - mask)
    result.save('output2.jpg')
