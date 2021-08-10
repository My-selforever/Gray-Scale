import cv2
import numpy as np

i1 = cv2.imread('fandc.png')
i2 = cv2.imread('ice.png')

ws = cv2.addWeighted(i1,0.5,i2,0.4,0)

cv2.imshow('img',ws)

cv2.imwrite('new.png',ws)
cv2.waitKey(0)