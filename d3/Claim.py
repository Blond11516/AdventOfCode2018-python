from __future__ import annotations
from typing import Tuple
import re

class Claim:
    def __init__(self, index: int, left: int, top: int, width: int, height: int) -> None:
        self.index = index
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def calculateConflicts(self, other: Claim) -> [Tuple[int, int]]:
        if other.left + other.width <= self.left:
            return []
        if other.left >= self.left + self.width:
            return []
        if other.top + other.height <= self.top:
            return []
        if other.top >= self.top + self.height:
            return []
        
        if self.left < other.left:
            minX = other.left + 1
        else:
            minX = self.left + 1
        
        if self.left + self.width < other.left + other.width:
            maxX = self.left + self.width
        else:
            maxX = other.left + other.width

        if self.top < other.top:
            minY = other.top + 1
        else:
            minY = self.top + 1
        
        if self.top + self.height < other.top + other.height:
            maxY = self.top + self.height
        else:
            maxY = other.top + other.height
        
        conflicts = []
        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                conflicts.append((i, j))
        
        return conflicts
    
    @staticmethod
    def parse(claimString: str) -> Claim:
        regex = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
        match = re.findall(regex, claimString)
        if match:
            return Claim(
                int(match[0][0]),
                int(match[0][1]),
                int(match[0][2]),
                int(match[0][3]),
                int(match[0][4])
            )