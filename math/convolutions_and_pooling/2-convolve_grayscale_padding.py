#!/usr/bin/env python3

"""
Performs a convolution on grayscale images using a
given kernel with custom padding.
"""


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images using
    a given kernel with custom padding.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # Pad images with zeros based on custom padding (ph, pw)
    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')

    # Determine output dimensions
    out_h = h + 2 * ph - kh + 1
    out_w = w + 2 * pw - kw + 1

    # Initialize output array for convolved images
    convolved_images = np.zeros((m, out_h, out_w))

    # Loop over each image
    for i in range(m):
        # Perform convolution with custom padding for each image
        for y in range(out_h):
            for x in range(out_w):
                # Element-wise multiplication and summing for the current region
                region = padded_images[i, y:y+kh, x:x+kw]
                convolved_images[i, y, x] = np.sum(region * kernel)

    return convolved_images
