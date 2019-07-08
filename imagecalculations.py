import cv2
import numpy as np
from math import sqrt
from PIL import Image

X_data = []
file = "/Users/mohanpraveenhazaru/Desktop/03.0000002a.png"
image = Image.open("/Users/mohanpraveenhazaru/Desktop/face.png")

X_data.append(cv2.imread(file))
min = np.min(X_data)
max = np.max(X_data)
mean = np.mean(X_data)
std = np.std(X_data)
# std = sqrt(mean(abs(min - max.mean())**2))
# adjsted = max(std,1/np.sum(np.array(X_data).shape))
print('X_data shape:', np.array(X_data).shape)
# print 1 / np.sum(np.array(X_data).shape)
print mean
print std
print min
print max
# print np.array(X_data).size
# # print list(image.getdata())
# image=cv2.imread("/Users/mohanpraveenhazaru/Desktop/face.png")
# print image.shape
# print (image.size)

