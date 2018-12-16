import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

import Utils
from LogEntry import LogEntry
from GuardInfo import GuardInfo

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'input.txt')
inputs = Utils.readInputs(filePath, LogEntry.parse)
inputs.sort(key=LogEntry.generateSortingKey)

groupedEntries = dict()
i = 0
while i < len(inputs):
    guardId = inputs[i].id
    if not guardId in groupedEntries:
        groupedEntries[guardId] = []
    
    groupedEntries[guardId].append(inputs[i])
    i += 1
    
    while i < len(inputs) and not hasattr(inputs[i], 'id'):
        groupedEntries[guardId].append(inputs[i])
        i += 1

guardInfos = []
for guardId, entries in groupedEntries.items():
    guardInfos.append(GuardInfo.fromEntries(guardId, entries))

mostSleptMinutes = list(map(lambda gi: (gi, gi.findMostSleptMinute()), guardInfos))

worstMinute = max(mostSleptMinutes, key=(lambda minute: minute[0].asleepMinutes[minute[1]]))
print(worstMinute[0].id * worstMinute[1])