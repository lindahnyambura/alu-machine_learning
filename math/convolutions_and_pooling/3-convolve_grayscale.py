#!/usr/bin/env python3

"""
Performs a convolution on grayscale images using a
given kernel with flexible padding and stride
"""


import numpy as np
from math import ceil


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on grayscale images using a
    given kernel with flexible padding and stride
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    # Determine padding
    if padding == 'same':
        ph = (kh - 1) // 2
        pw = (kw - 1) // 2
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad images with zeros based on the determined padding (ph, pw)
    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')

    # Calculate output dimensions
    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1

    convolved_images = np.zeros((m, out_h, out_w))

    # Loop over each image
    for i in range(m):
        # Perform convolution with stride and padding for each image
        for y in range(out_h):
            for x in range(out_w):
                # Define region based on stride
                region = padded_images[i, y*sh:y*sh+kh, x*sw:x*sw+kw]
                convolved_images[i, y, x] = np.sum(region * kernel)

    return convolved_images
