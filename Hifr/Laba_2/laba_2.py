from PIL import Image, ImageOps, ImageDraw, ImageTk
from tkinter import Tk, Button, Canvas, Label, filedialog as fd
import random
import copy
import tkinter as tk
import numpy
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

pyti = 'D:/Mega/MEGAsync/VC_Code/Hifr/Laba_2/'

def createMassive(size):
    massive = []
    for i in range(size):
        massive.append(str(random.randint(0, 1)))
    print(massive)
    return massive

def writeImg(name):

    pic = Image.open(name)
    pix = numpy.array(pic)

    return pix

def refactorMass(Mass):
    i, j = 0, 0
    Mass2 = []
    print(len(Mass))
    for Mass_i in Mass:
        # Mass2_j = []
        for Mass_j in Mass_i:
            if all(Mass_j) == all([255, 255, 255, 255]):
                Mass2.append('1')
            else: Mass2.append('0')
            j+=1
        i+= 1
        j=0
    print(len(Mass2))
    return Mass2



def createImg(massive, size, number):
    mas = []
    n = int(size / 100)
    '''
        for i in range(10):
        mas.append(random.randint(0, 1))
    '''
    # print(massive)
    for i in range(len(massive)):
        massive[i] = int(massive[i])
        mas.append(abs(massive[i] - 1))
    #print(massive)
    '''
    for i in range(len(massive)):
        mas.append(massive.pop(0))
    print(mas)
    '''

    img = Image.new('1', (n, n))

    '''
        for x in range(size):
        for y in range(size):
            img.putpixel((x, y), 1)
    '''
    count = 0
    for y in range(n):
        for x in range(n):
            i = 0 if mas[count] == 1 else 1
            img.putpixel((x, y), i)
            count += 1
            # print(massive[k])

    # img.show()

    fileName = str(number) + '.png'
    img.save(pyti + fileName)


def encoding(massive):
    # mas = ['1', '1', '1', '1', '1', '0', '0', '1', '1', '1']
    #print(massive)
    mas = massive
    current = mas[0]
    encoded = ""
    buffer = []
    for i in range(len(mas)):
        if mas[i] == current:
            buffer.append(mas[i])
            continue

        current = mas[i]
        encoded = encoded + "c" + str(len(buffer)) + "v" + buffer[0]
        buffer = []
        buffer.append(mas[i])
    encoded = encoded + "c" + str(len(buffer)) + "v" + buffer[0]
    buffer = []
    print(encoded)
    #print(type(encoded))
    return encoded


def decoding(data):
    print('decoding data input length:', len(data))
    decoded = []
    # print(data[1])
    buffer = []
    count = ''
    for i in range(len(data)):
        if data[i] == 'c':
            n = 1
            while data[i+n] != 'v':
                count += data[i + n]
                n+=1

            # if data[i+2] == 'v':
            #     count = int(data[i + 1])
            # else:
            #     count = int(data[i + 1] + data[i+2])
        elif data[i] == 'v':
            for j in range(int(count)):
                buffer.append(data[i + 1])
            decoded.extend(buffer)
            count = ''
            buffer = []

    #print(massive)
    print('decoding data output length:', len(decoded))

    return decoded

def writeInFile(n, data):
    fileName = str(n) + '.txt'
    f = open(pyti + fileName, 'w')
    #print(type(data))
    if type(data) == list:
        f.write(' '.join(data))
    if type(data) == str:
        f.write(data)
    f.close()


def readFromFile(n):
    fileName = str(n) + '.txt'
    with open(pyti + fileName, 'r') as f:
        # print(f.read())
        data = f.read()
    f.close()
    return data


# size = 100 * 100
# writeInFile(1, createMassive(size))
# mas = readFromFile(1).split()
# print('Размер массива:', len(mas))
# # print(createMassive(size))

# createImg(mas, size, 1)
# mas = readFromFile(1).split()
# print(mas)
# print(len(mas))

# writeInFile(2, encoding(mas))
# writeInFile(3, decoding(readFromFile(2)))

# mas = readFromFile(3).split()
# print(len(mas))
# #encoding(mas)
# createImg(mas, size, 3)
#######################
# Mass = refactorMass(writeImg('D:/Mega/MEGAsync/VC_Code/Сжатие/1.png'))
# writeInFile(1, Mass)

# writeInFile(2, encoding(Mass))
# writeInFile(3, decoding(readFromFile(2)))

# Mass = readFromFile(3).split()
# print(len(Mass))
# #encoding(Mass)
# createImg(Mass, 10000, 3)

# Это наш конвертированный файл дизайна

# class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)  # Это нужно для инициализации нашего дизайна

# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение

# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()


