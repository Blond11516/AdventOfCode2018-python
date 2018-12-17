import os
import sys
from functools import reduce

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from Coordinates import Coordinates

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, Coordinates.parse)

minX = min(inputs, key=lambda coord: coord.x).x
maxX = max(inputs, key=lambda coord: coord.x).x
minY = min(inputs, key=lambda coord: coord.y).y
maxY = max(inputs, key=lambda coord: coord.y).y

points = [[None] * (maxY - minY + 1) for i in range(maxX - minX + 1)]

size = 0
for i in range(len(points)):
    for j in range(len(points[0])):
        if sum(list(map(lambda coord: coord.calculateManhattanDistance(i + minX, j + minY), inputs))) < 10000:
            size += 1

print(size)