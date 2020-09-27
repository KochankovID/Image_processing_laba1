import numpy as np
import cv2


if __name__ == "__main__":
    print('hello world')
    mode = int(input('mode:'))  # Считываем номер операции которую надо сделать
    if mode == 0:  # b.	Реализовать конвертацию в оттенки серого при помощи cv::cvtColor().
        image = cv2.imread(r'C:\Users\HP-PC\Desktop\google.jpg')  # Открываем изображение r неизвестно зачем но работать так должно.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original image', image)
        cv2.imshow('Gray image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if mode == 1: #	Конвертация цветного изображения в монохромное изображение
        image = cv2.imread(r'C:\Users\HP-PC\Desktop\google.jpg')
      #  blue, green, red = cv2.split(image)  # Split the image into its channels
        b = image[:, :, 0]
        g = image[:, :, 1]
        r = image[:, :, 2]
        single = (b + g + r) / 3
        #-----------------
        copy = image.copy()
        copy[:, :, 0] = single = (b + g + r) / 3
        copy[:, :, 1] =  single = (b + g + r)/3
        copy[:, :, 2] =  single = (b + g + r)/3
        
        #-------------------
        cv2.imshow('Original image', image)
        cv2.imshow('average image', copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()