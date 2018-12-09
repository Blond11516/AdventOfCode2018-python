from functools import reduce
import os

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
file = open(filePath, "r")
inputs = [int(line) for line in file.read().split('\n')]

print(reduce((lambda x, y: x + y), inputs))