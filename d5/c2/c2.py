import os
import sys
from string import ascii_letters, ascii_lowercase

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils

def filterPolymer(polymer: str, letter: str) -> str:
    filteredPolymer = polymer.replace(letter, '')
    return filteredPolymer.replace(letter.swapcase(), '')

def reducePolymer(polymer: str) -> str:
    reactionsLeft = True
    while reactionsLeft:
        reactionsLeft = False
        i = 1
        while i < len(polymer):
            if polymer[i - 1] in reactions and reactions[polymer[i - 1]] == polymer[i]:
                polymer = polymer[:i - 1] + polymer[i + 1:]
                i -= 2
                if i < 1:
                    i = 1
                reactionsLeft = True

            i += 1
    return polymer

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath)
polymer = inputs[0]

reactions = dict()
for letter in ascii_letters:
    reactions[letter] = letter.swapcase()

minLength = sys.maxsize
for letter in ascii_lowercase:
    filteredPolymer = filterPolymer(polymer, letter)
    reducedPolymer = reducePolymer(filteredPolymer)
    del filteredPolymer

    if len(reducedPolymer) < minLength:
        minLength = len(reducedPolymer)
    
    del reducedPolymer

print(minLength)