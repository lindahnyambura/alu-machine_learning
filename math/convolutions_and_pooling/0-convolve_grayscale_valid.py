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

    out_h = h - kh + 1
    out_w = w - kw + 1

    convolved_images = np.zeros((m, out_h, out_w))

    # Loop over each image
    for i in range(out_h):
        for j in range(out_w):
            region = images[:, i:i+kh, j:j+kw]
            convolved_images[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return convolved_images
