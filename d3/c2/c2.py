import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from Claim import Claim


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