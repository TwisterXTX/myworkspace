import cv2

print('hello world')
img = cv2.imread('bird.jpg')

cv2.imshow('imshow', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
