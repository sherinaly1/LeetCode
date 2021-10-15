# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:16:55 2021
Character recognition using SVD
@author: sherin
"""
import numpy as np
from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
from sklearn.decomposition import TruncatedSVD
float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})
from sklearn.ensemble import RandomForestClassifier

X, y = load_digits(return_X_y=True)

image = X[0]
image = image.reshape((8, 8))
plt.matshow(image, cmap = 'gray')

U, s, V = np.linalg.svd(image)
S = np.zeros((image.shape[0], image.shape[1]))
S[:image.shape[0], :image.shape[0]] = np.diag(s)
n_component = 2
S = S[:, :n_component]
VT = V[:n_component, :]
A = U.dot(Sigma.dot(VT))
print(A)