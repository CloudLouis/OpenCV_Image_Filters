# LINK: http://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html
import cv2
import numpy as np


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


def burnV2(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)


image = cv2.imread("picture.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blur_img = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
final_image = dodgeV2(blur_img, gray_image)
img_canvas = cv2.imread("canvas.jpg", cv2.IMREAD_GRAYSCALE)
final_image = cv2.multiply(final_image, img_canvas, scale=1/256)

cv2.imshow('Picture', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
