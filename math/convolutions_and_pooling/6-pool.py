#!/usr/bin/env python3

"""
Performs pooling on images
"""


import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images
    """

    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1

    pooled = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            i_sh = i * sh
            j_sw = j * sw
            region = images[:, i_sh:i_sh + kh, j_sw:j_sw + kw, :]

            if mode == 'max':
                pooled[:, i, j, :] = np.max(region, axis=(1, 2))
            elif mode == 'avg':
                pooled[:, i, j, :] = np.mean(region, axis=(1, 2))

    return pooled
