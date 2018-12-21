import os
import sys
from string import ascii_uppercase

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from Step import Step

def findRoots(steps: [Step], workedOn: [Step]):
    notRoot = set()
    for step in steps:
        notRoot.update(set(step.next))
    
    return [step for step in steps if not step.id in notRoot and not step in list(map(lambda x: x[0], workedOn))]
    

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, Step.parse)

remaining = Step.combine(inputs)
workedOn = []
duration = 0

while len(remaining) > 0:
    duration += 1
    notCompleted = []
    for workedStep in workedOn:
        if duration - workedStep[1] + 1 < 60 + ascii_uppercase.index(workedStep[0].id) + 1:
            notCompleted.append(workedStep)
        else:
            remaining = [step for step in remaining if step.id != workedStep[0].id]    

    workedOn = notCompleted

    if len(workedOn) < 4:
        roots = findRoots(remaining, workedOn)
        if len(roots) > 0:
            roots.sort(key=lambda x: x.id)
            workedOn.append((roots[0], duration))

print(duration)