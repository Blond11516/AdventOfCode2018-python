import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from Claim import Claim

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, Claim.parse)

conflicts = set()
for claim in inputs:
    for claim2 in filter((lambda x: x != claim), inputs):
        for conflict in claim.calculateConflicts(claim2):
            conflicts.add(conflict)

print(len(conflicts))