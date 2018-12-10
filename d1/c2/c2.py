import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils


filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, lambda x: int(x))

i = 0
frequency = 0
reachedFrequencies = []
while not frequency in reachedFrequencies:
    reachedFrequencies.append(frequency)
    frequency += inputs[i]
    i += 1
    i %= len(inputs)

print(frequency)