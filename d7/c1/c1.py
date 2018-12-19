import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from Step import Step

def findRoots(steps: [Step]):
    notRoot = set()
    for step in steps:
        notRoot.update(set(step.next))
    
    return [step for step in steps if not step.id in notRoot]
    


filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, Step.parse)

combined = Step.combine(inputs)

order = ''
while len(combined) > 0:
    roots = findRoots(combined)
    roots.sort(key=lambda x: x.id)
    order += roots[0].id
    combined = [step for step in combined if step.id != roots[0].id]

print(order)