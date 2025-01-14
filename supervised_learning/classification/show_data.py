#!/usr/bin/env python 3

import numpy as np
import matplotlib.pyplot as plt

# load data from zipped archive of multiple NumPy arrays
lib_train = np.load(r'C:\Users\user\alu-machine_learning\supervised_learning\classification\data\Binary_Train.npz')

# extract the arrays X(features) and Y(labels) from loaded file
X_3D, Y = lib_train['X'], lib_train['Y']

# plotting
fig = plt.figure(figsize=(10, 10)) # width, height
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_3D[i])
    plt.title(Y[0, i])
    plt.axis('off')
plt.tight_layout()
plt.show()