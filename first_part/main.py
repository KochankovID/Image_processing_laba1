import numpy as np
import cv2

import random

if __name__ == "__main__":
    print('hello world')
    mode = int(input('mode:'))  # Считываем номер операции которую надо сделать
    if mode == 0:
        image = cv2.imread(r'C:\Users\HP-PC\Desktop\google.jpg')  # Открываем изображение r неизвестно зачем но работать так должно.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original image', image)
        cv2.imshow('Gray image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        # blue, green, red = cv2.split(image)

    # draw = ImageDraw.Draw(image)   Создаем инструмент для рисования.
    # height = image.size[1]   Определяем высоту.
    # pix = image.load()   Выгружаем значения пикселей
