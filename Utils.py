from functools import reduce
import os
from typing import Callable, TypeVar

T = TypeVar('T')

def readInputs(filePath, converter: Callable[[str], T] = lambda x: x) -> T:
    file = open(filePath, "r")
    inputs = [converter(line) for line in file.read().split('\n')]
    file.close()
    return inputs