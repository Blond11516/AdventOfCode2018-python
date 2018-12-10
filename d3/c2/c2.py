import os
import Utils
from Claim import Claim
import sys

"""claim1 = Claim(1, 10, 20, 10, 10)
claim2 = Claim(2, 20, 10, 10, 10)

print(len(claim1.calculateConflicts(claim2)))"""

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, Claim.parse)

for claim in inputs:
    conflict = False
    for claim2 in filter((lambda x: x != claim), inputs):
        if len(claim.calculateConflicts(claim2)) > 0:
            conflict = True
            break
    
    if not conflict:
        print(claim.index)
        sys.exit()