import cv2
import numpy as np


def preprocess_image(img):
    grey_scale = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(grey_scale, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(
        resized_image, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 63, 13)
    return processed_image
