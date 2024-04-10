import functools
from collections import deque
import sys
from pprint import pprint

tetros = [[[1,1,1,1],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]],
          [[1,1,0,0],
           [1,1,0,0],
           [0,0,0,0],
           [0,0,0,0]],
          [[1,0,0,0],
           [1,0,0,0],
           [1,1,0,0],
           [0,0,0,0]],
          [[1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,0,0,0]],
          [[1,1,1,0],
           [0,1,0,0],
           [0,0,0,0],
           [0,0,0,0]]]

print('new pivot')
for i, tetro in enumerate(tetros):
    pivot = (list(zip(*tetro)))

    print('-')
    for line in pivot:
        print(line)

    tetros[i] = pivot

print('reverse')
for i, tetro in enumerate(tetros):
    print('-')
    for li, line in enumerate(tetro):
        line = list(line)
        line.reverse()
        tetro[li] = tuple(line)

    tetros[i] = tetro

print('new pivot')
for i, tetro in enumerate(tetros):
    pivot = (list(zip(*tetro)))

    print('-')
    for line in pivot:
        print(line)

    tetros[i] = pivot

print('reverse')
for i, tetro in enumerate(tetros):
    print('-')
    for li, line in enumerate(tetro):
        line = list(line)
        line.reverse()
        tetro[li] = tuple(line)

    tetros[i] = tetro