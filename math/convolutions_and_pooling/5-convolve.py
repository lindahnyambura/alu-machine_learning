#!/usr/bin/env python3

"""
Performs a convolution on images using multiple kernels
"""


import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple kernels
    """

    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph = pw = 0
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                           mode='constant')

    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1

    convolved_arr = np.zeros((m, out_h, out_w, nc))

    for k in range(nc):
        kernel = kernels[:, :, :, k]
        for i in range(out_h):
            for j in range(out_w):
                i_sh = i * sh
                j_sh = j * sw
                region = padded_images[:, i_sh:i_sh + kh, j_sh:j_sh + kw, :]
                convolved_arr[:, i, j, k] = np.sum(region * kernel,
                                                   axis=(1, 2, 3))

    return convolved_arr
