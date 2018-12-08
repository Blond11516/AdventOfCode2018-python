from functools import reduce

file = open("input.txt", "r")
inputs = [int(line) for line in file.read().split('\n')]

print(reduce((lambda x, y: x + y), inputs))