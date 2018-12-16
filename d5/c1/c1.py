import os
import sys
from string import ascii_letters

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath)
polymer = inputs[0]

reactions = dict()
for letter in ascii_letters:
    reactions[letter] = letter.swapcase()

reactionsLeft = True
while reactionsLeft:
    reactionsLeft = False
    i = 1
    while i < len(polymer):
        if polymer[i - 1] in reactions and reactions[polymer[i - 1]] == polymer[i]:
            polymer = polymer[:i - 1] + polymer[i + 1:]
            i -= 2
            reactionsLeft = True
        i += 1

print(len(polymer))