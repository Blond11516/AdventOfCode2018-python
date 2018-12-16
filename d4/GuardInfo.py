from __future__ import annotations
from LogEntry import LogEntry, EventType
from functools import reduce

class GuardInfo:
    def __init__(self, guardId: int) -> None:
        self.id = guardId
        self.asleepMinutes = dict()
        self.awakeMinutes = dict()
    
    def findMostSleptMinute(self) -> int:
        if not self.asleepMinutes.keys():
            self.asleepMinutes[0] = 0
        return max(self.asleepMinutes.keys(), key=(lambda key: self.asleepMinutes[key]))
    
    @staticmethod
    def calculateTotalSleepMinutes(info: GuardInfo) -> int:
        return reduce(lambda acc, value: acc + value, info.asleepMinutes.values(), 0)
    
    @staticmethod
    def fromEntries(guardId: int, entries: [LogEntry]) -> GuardInfo:
        guardInfo = GuardInfo(guardId)
        
        prevTime = 0
        for entry in entries:
            if entry.eventType == EventType.WAKE_UP:
                dictionary = guardInfo.asleepMinutes
            else:
                dictionary = guardInfo.awakeMinutes

            for minute in range(prevTime, entry.minute):
                if minute in dictionary:
                    dictionary[minute] += 1
                else:
                    dictionary[minute] = 1
            
            prevTime = entry.minute
        
        return guardInfo