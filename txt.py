import cv2 

img = cv2.imread('new.png')

image = cv2.putText(img,'FrosttBurnn',(150,200), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)

cv2.imshow('img',image)


cv2.imwrite('newtxt.png',image)

cv2.waitKey(0)
