from functools import reduce
import os
import Utils

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, lambda x: int(x))

print(reduce((lambda x, y: x + y), inputs))