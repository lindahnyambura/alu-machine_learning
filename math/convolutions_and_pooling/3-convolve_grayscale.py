#!/usr/bin/env python3

"""
Performs a convolution on grayscale images using a
given kernel with flexible padding and stride
"""


import numpy as np


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
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                           mode='constant')

    # Calculate output dimensions
    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1

    convolved_images = np.zeros((m, out_h, out_w))

    # Loop over each image
    for h in range(out_h):
        for w in range(out_w):
            region = padded_images[:, h*sh : h*sh + kh, w*sw : w*sw + kw]
            result = np.sum(region * kernel, axis=(1)).sum(axis=1)
            convolved_images[:, h, w] = result
            
    return convolved_images
