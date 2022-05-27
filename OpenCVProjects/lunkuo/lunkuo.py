import cv2
from time import sleep
import numpy as np
from cv2 import threshold

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(3, 1280)  # 设置分辨率
camera.set(4, 768)

while True:
    (grabbed, frame) = camera.read()
    dst = frame
    gaussian_img = cv2.GaussianBlur(dst, (5, 5), 10)
    gray_img = cv2.cvtColor(gaussian_img, cv2.COLOR_BGR2GRAY)
    _, threshold_img = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(dst, contours, -1, (0, 0, 255), 3)
    cv2.namedWindow('final_img', 1)
    cv2.imshow('final_img', dst)
    sleep(0.5)