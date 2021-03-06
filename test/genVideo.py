import cv2
import numpy as np
import glob

img_array = []
for filename in sorted(glob.glob('/home/chaitanya/Documents/Bid data/project/test/images/*.jpg')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('pk.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
