import matplotlib.pyplot as plt
import pytesseract
import cv2


def open_img(img_path):
    car_plate_img = cv2.imread(img_path)
    car_plate_img = cv2.cvtColor(car_plate_img, cv2.COLOR_BGR2RGB)
