from functools import reduce
import os

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
file = open(filePath, "r")
inputs = [int(line) for line in file.read().split('\n')]
file.close()

i = 0
frequency = 0
reachedFrequencies = []
while not frequency in reachedFrequencies:
    reachedFrequencies.append(frequency)
    frequency += inputs[i]
    i += 1
    i %= len(inputs)

print(frequency)