import os
import Utils

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'input.txt')
inputs = Utils.readInputs(os.path.join(os.pardir, filePath))

trios = 0
duos = 0
for input in inputs:
    letterCounts = dict()
    for letter in input:
        if letter in letterCounts.keys():
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1
    
    if 2 in letterCounts.values():
        duos += 1
    if 3 in letterCounts.values():
        trios += 1

print(duos * trios)