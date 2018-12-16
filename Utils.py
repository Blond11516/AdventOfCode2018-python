from functools import reduce
import os
from typing import Callable, TypeVar

T = TypeVar('T')

def readInputs(filePath, converter: Callable[[str], T] = lambda x: x) -> T:
    with open(filePath, "r") as file:
        inputs = [converter(line) for line in file.read().split('\n')]

    return inputs