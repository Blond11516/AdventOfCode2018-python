import os
import sys

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

for i in range(len(points)):
    for j in range(len(points[0])):
        manhattanDistances = list([(coord.calculateManhattanDistance(i + minX, j + minY), coord) for coord in inputs])
        minDist = min(manhattanDistances, key=lambda dist: dist[0])
        if list(map(lambda dist: dist[0], manhattanDistances)).count(minDist[0]) <= 1:
            points[i][j] = inputs.index(minDist[1])

areaSizes = dict()
for i in range(len(points)):
    for j in range(len(points[0])):
        if not points[i][j] in areaSizes:
            areaSizes[points[i][j]] = 1
        else:
            areaSizes[points[i][j]] += 1

infiniteAreas = set()
for i in range(maxX - minX):
    infiniteAreas.add(points[i][0])
    infiniteAreas.add(points[i][maxY - minY])

for j in range(maxY - minY):
    infiniteAreas.add(points[0][j])
    infiniteAreas.add(points[maxX - minX][j])

filteredAreaSizes = dict()
for coordIndex, areaSize in areaSizes.items():
    if coordIndex and not coordIndex in infiniteAreas:
        filteredAreaSizes[coordIndex] = areaSize

print(max(filteredAreaSizes.values()))