#!/usr/bin/env python3

"""
Performs a same convolution on grayscale images using a given kernel.
"""


import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images using a given kernel.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate padding dimensions
    pad_h = kh // 2
    pad_w = kw // 2

    # Pad images with zeros
    padded_images = np.pad(images, ((0, 0), (pad_h, pad_h),
                                    (pad_w, pad_w)), mode='constant')


    convolved_images = np.zeros((m, h, w))

    # Loop over each image
    for i in range(m):
        # Perform same convolution for each image
        for y in range(h):
            for x in range(w):

                region = padded_images[i, y:y+kh, x:x+kw]
                convolved_images[i, y, x] = np.sum(region * kernel)

    return convolved_images
