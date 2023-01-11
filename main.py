import matplotlib.pyplot as plt
import pytesseract
import cv2


def open_img(img_path):
    car_plate_img = cv2.imread(img_path)
    car_plate_img = cv2.cvtColor(car_plate_img, cv2.COLOR_BGR2RGB)
    plt.imshow(car_plate_img)
    plt.show()

    return car_plate_img

def main():
    car_plate_img_rgb = open_img(img_path='./plate/1.jpg')


if __name__ == '__main__':
    main()

