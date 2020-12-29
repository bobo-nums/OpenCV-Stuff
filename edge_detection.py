"""
OpenCV Edge Detection
Based on tutorial video by NeuralNine
https://www.youtube.com/watch?v=4xq5oE9jJZg
"""

import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    success, frame = camera.read()
    
    # laplacian = cv.Laplacian(frame, cv.CV_64F)
    # laplacian = np.uint8(laplacian)
    # cv.imshow('Laplacian', laplacian)

    edges = cv.Canny(frame, 95, 95)
    cv.imshow('Camera', frame)
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()