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

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                           mode='constant')

    out_h = h + 2 * ph - kh + 1
    out_w = w + 2 * pw - kw + 1

    convolved_images = np.zeros((m, out_h, out_w))
    # Loop over each image
    for i in range(out_h):
        for j in range(out_w):
            region = padded_images[:, i:i+kh, j:j+kw]
            convolved_images[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return convolved_images
