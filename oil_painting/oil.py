import cv2
import numpy as np

img = cv2.imread('picture.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 3), np.uint8)
pixel_class = 4
section = int(256 / pixel_class)
# Traverse each data of a picture with a two-tier for loop
for i in range(3, height - 3):
    for j in range(3, width - 3):
        # The gray levels defined in the current program are four
        # Define an array to load the number of pixels in these four levels
        array1 = np.zeros(pixel_class, np.uint8)
        # The small box defined in the current program is 6x6
        for m in range(-3, 3):
            for n in range(-3, 3):
                # p1 It divides the level segment of the pixel and represents 0 with subscripts.-3
                p1 = int(gray[i + m, j + n] / section)
                # Next, the pixel level is counted. The subscript of array1 represents the pixel level.
                # The value represents the number of pixels in the small box of the pixel level.
                array1[p1] = array1[p1] + 1
        # Next, determine which segment has the most pixels in the small box.
        currentMax = array1[0]
        l = 0  # Here we set an array subscript l to record the largest number of pixel segments.
        for k in range(0, pixel_class):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        # Mean Processing
        u = v = w = 0
        for m in range(-3, 3):
            for n in range(-3, 3):
                if gray[i + m, j + n] >= (l * section) and gray[i + m, j + n] <= ((l + 1) * section):
                    (b, g, r) = img[i + m, j + n]
                    u += b
                    v += g
                    w += r
        u = int(u / array1[l])
        v = int(v / array1[l])
        w = int(w / array1[l])
        dst[i, j] = [u, v, w]
cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()