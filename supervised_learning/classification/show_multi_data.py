#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# load data
lib = np.load(r'C:\Users\user\alu-machine_learning\supervised_learning\classification\data\MNIST.npz')
print(lib.files)
X_train_3D = lib['X_train']
Y_train = lib['Y_train']

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_train_3D[i])
    plt.title(str(Y_train[i]))
    plt.axis('off')
plt.tight_layout()
plt.show()