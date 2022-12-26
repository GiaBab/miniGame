import random as rm, numpy as np

class Queues:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return str(self.get())

    def getP(self, num:int):
        return self.get()[num]

    def get(self):
        return self.array[::-1]
    
    def pop(self):
        return self.array.pop(0)

    def append(self, num:int):
        return self.array.append(num)

def generateRandomArray(array, minLen, maxLen):
        for i in range(rm.randint(minLen, maxLen)):
            array.append(rm.randint(1, 999))