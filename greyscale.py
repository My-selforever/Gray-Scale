import cv2

img = cv2.imread('newtxt.png')
cv2.imshow('One',img)
cv2.waitKey(0)


gImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Two',gImg)
cv2.waitKey(0)

cv2.destroyAllWindows()