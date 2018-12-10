import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils


filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(os.path.join(os.pardir, filePath))

for firstInput in inputs:
    for secondInput in inputs:
        diff = 0
        i = 0
        while i < len(firstInput) and i < len(secondInput):
            if firstInput[i] != secondInput[i]:
                diff += 1
            if diff >= 2:
                break
            i += 1
        
        if diff == 1:
            print(firstInput + '\n' + secondInput)
            sys.exit()