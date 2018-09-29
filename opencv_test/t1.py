import cv2
import numpy as np
im = cv2.imread("a.jpg")
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
kernel = 1/16*np.array([[1,2,1], [2,4,2], [1,2,1]])
im_blur = cv2.filter2D(im_inv,-1,kernel)
ret, im_res = cv2.threshold(im_blur,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(im_res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
im2, contours, hierarchy = cv2.findContours(im_res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.imwrite('r1.jpg',im2)

