import cv2

img = cv2.imread("justit.jpg")

windown = "img"

start = (0,0)
end=(200,200)

color = (255,0,0)

thickness = 9

image = cv2.arrowedLine(img,(0,0),(200,200),(255,0,0),9)

cv2.imshow(windown,image)

cv2.waitKey(0)