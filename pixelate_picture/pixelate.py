import cv2

# Input image
input = cv2.imread('picture.jpg')

# Get input size
width, height, _ = input.shape

# Desired "pixelated" size
w, h = (50, 50)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', input)
cv2.imshow('Output', output)

cv2.waitKey(0)