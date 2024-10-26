#!/usr/bin/env python3

"""
Performs a valid convolution on grayscale images using a given kernel.
"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images using a given kernel.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    # Determine output dimensions
    out_h = h - kh + 1
    out_w = w - kw + 1

    convolved_images = np.zeros((m, out_h, out_w))

    # Loop over each image
    for i in range(m):
        for y in range(out_h):
            for x in range(out_w):
                region = images[i, y:y+kh, x:x+kw]
                convolved_images[i, y, x] = np.sum(region * kernel)

    return convolved_images
