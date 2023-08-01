import random as rm, numpy as np

class Queues:
    def __init__(self, array = None):
        if array == None : array = []
        self.array = array

    def __repr__(self) -> str:
        return str(self.get())

    def getP(self, num:int):
        return self.get()[num]

    def iterator(self):
        [print(i) for i in self.get()]

    def get(self):
        return self.array[::-1]
    
    def pop(self):
        if self.array:
            return self.array.pop(0)

    def append(self, num:int):
        return self.array.append(num)

    def sum(self):
        return np.sum(self.get())

    def len(self):
        return len(self.array)

def generateRandomArray(array, minLen:int, maxLen:int):
        for i in range(rm.randint(minLen, maxLen)):
            array.append(rm.randint(1, 999))

def allEqual(iterator):
    if not any(iterator):
        return False
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

def rawToColumn(iterartor):
    x,y = np.shape(iterartor)
    arrayAux = np.zeros((x,y), str)
    for i in range(x) :
        for j in range(y): 
            arrayAux[i][j] = iterartor[j][i]
    return arrayAux

def anyWhen(f, xs) -> bool:
    return any([f(x) for x in xs])            