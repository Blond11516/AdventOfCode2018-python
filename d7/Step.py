from __future__ import annotations
import re

class Step:
    def __init__(self, stepId: str, nextSteps: [str]) -> None:
        self.id = stepId
        self.next = nextSteps
    
    @staticmethod
    def parse(inputStr: str) -> Step:
        regex = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'
        match = re.findall(regex, inputStr)

        if match:
            return Step(match[0][0], [match[0][1]])
    
    @staticmethod
    def combine(steps: [Step]) -> [Step]:
        combined = dict()
        for step in steps:
            if step.id in combined:
                combined[step.id] += step.next
            else:
                combined[step.id] = step.next
            
            for nextStep in step.next:
                if not nextStep in combined:
                    combined[nextStep] = []
        
        return [Step(key, value) for key, value in combined.items()]