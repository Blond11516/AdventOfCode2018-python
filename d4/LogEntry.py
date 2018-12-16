from __future__ import annotations
import re
from enum import Enum

class EventType(Enum):
    START_SHIFT = 1
    ASLEEP = 2
    WAKE_UP = 3

class LogEntry:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, entry: str) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        
        regex = "Guard #(\d*) begins shift"
        match = re.match(regex, entry)
        if match != None:
            self.eventType = EventType.START_SHIFT
            self.id = int(match.group(1))
        elif entry == "falls asleep":
            self.eventType = EventType.ASLEEP
        else:
            self.eventType = EventType.WAKE_UP

    @staticmethod
    def generateSortingKey(entry: LogEntry):
        return int(f"{'{:02d}'.format(entry.month)}{'{:02d}'.format(entry.day)}{'{:02d}'.format(entry.hour)}{'{:02d}'.format(entry.minute)}") 
    
    @staticmethod
    def parse(entryString: str) -> LogEntry:
        regex = "\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)"
        match = re.findall(regex, entryString)

        if match:
            return LogEntry(
                int(match[0][0]),
                int(match[0][1]),
                int(match[0][2]),
                int(match[0][3]),
                int(match[0][4]),
                match[0][5],
            )