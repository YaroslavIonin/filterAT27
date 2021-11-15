from PIL import Image
import numpy as np
from itertools import product


def get_middle(i, j):
    s = 0
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, len(matrix[int(n)][int(n1)])):
            if n >= x or n1 >= y:
                break
            s += int(matrix[int(n)][int(n1)][a])
    return int(s // (sizeX*sizeY)) / 3


def get_color(i, j):
    s = get_middle(i, j)
    step = 255 / gradation
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, 3):
            if n >= x or n1 >= y:
                break
            matrix[n, n1][a] = int(s // step) * step


def get_mosaic():
    [[get_color(i, j) for j in range(0, y, sizeY)] for i in range(0, x, sizeX)]
    res = Image.fromarray(matrix)
    res.save(newImg)


#print('Введите имя исходного изображения')
img = Image.open("img2.jpg")
matrix = np.array(img)
x = len(matrix)
y = len(matrix[1])
#print('Введите имя нового изображения')
newImg = "res.jpg"
#print('Введите высоту мозайки')
sizeX = 10
#print('Введите ширину мозайки')
sizeY = 10
#print('Введите количество градаций серого')
gradation = 5.1
get_mosaic()
