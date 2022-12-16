import random as rm, numpy as np

class Queues:
    def __init__(self, array = []):
        self.array = array

    def __repr__(self):
        return str(self.get())

    def generateRandomQueues(self, minLen, maxLen):
        for i in range(rm.randint(minLen, maxLen)):
            self.append(rm.randint(1, 999))

    def getP(self, num:int):
        return self.get()[num]
    
    def get(self):
        return self.array[::-1]
    
    def pop(self):
        return self.array.pop(0)

    def append(self, num:int):
        return self.array.append(num)