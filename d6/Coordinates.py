from __future__ import annotations
import re

class Coordinates:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def calculateManhattanDistance(self, x: int, y: int) -> int:
        return abs(x - self.x) + abs(y - self.y)
    
    def isInsideArea(self, minX: int, maxX: int, minY: int, maxY: int) -> bool:
        return not (self.x == minX or self.x == maxX or self.y == minY or self.y == maxY)
    
    @staticmethod
    def parse(coordinatesString: str) -> Coordinates:
        regex = "(\d+), (\d+)"
        match = re.findall(regex, coordinatesString)

        if match:
            return Coordinates(int(match[0][0]), int(match[0][1]))