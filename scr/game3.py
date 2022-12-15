import random as rm, numpy as np

class Queues:
    def __init__(self, min:int, max:int):
        self.array = []

    def generateRandomStack(self, maxLen, minLen):
        for i in range(rm.randint(minLen, maxLen)):
            self.array[i] = rm.randint(1,999)

    def get(self, num:int):
        return self.get()[num]
    
    def get(self):
        return self.array[::-1]
    
    def pop(self):
        return self.array.pop(0)

    def append(self, num:int):
        return self.array.append(num)
