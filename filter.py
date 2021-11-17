from PIL import Image
import numpy as np
from itertools import product


def get_middle(i, j):
    """
    Функция находит среднее значение вокруг заданного i, j, в зависимости от размеров мозайки
    :param i: номер строчки пикселя
    :param j: номер колонки пикселя
    :return: среднее значение
    >>>: get_middle(45, 2)
    19.0
    >>>:get_middle(58, 60)
    22.0
    >>>get_middle(235, 101)
    214.0
    """
    s = 0
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, len(matrix[int(n)][int(n1)])):
            if n >= x or n1 >= y:
                break
            s += int(matrix[int(n)][int(n1)][a])
    return int(s // (sizeX*sizeY)) / 3


def get_color(i, j):
    """
    Функция находит присваивает значение цвета вокруг заданного пикселя, в зависимости от размеров мозайки и градации серого
    :param i: номер строчки пикселя
    :param j: номер колонки пикселя
    """
    s = get_middle(i, j)
    step = 255 / gradation
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, 3):
            if n >= x or n1 >= y:
                break
            matrix[n, n1][a] = int(s // step) * step


def get_mosaic():
    """
    Функция применяет get_color для пикселей, в зависимости от размеров мозайки
    """
    [[get_color(i, j) for j in range(0, y, sizeY)] for i in range(0, x, sizeX)]
    res = Image.fromarray(matrix)
    res.save(newImg)


print('Введите имя исходного изображения')
img = Image.open(input())
matrix = np.array(img)
x = len(matrix)
y = len(matrix[1])
print('Введите имя нового изображения')
newImg = input()
print('Введите высоту мозайки')
sizeX = int(input())
print('Введите ширину мозайки')
sizeY = int(input())
print('Введите количество градаций серого')
gradation = float(input())
get_mosaic()

