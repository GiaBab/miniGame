import dataStructureSystems as ds

class WhoHaveMoreItems():
    def __init__(self) -> None:
        self.monoky1=Monoky()
        self.monoky2=Monoky()
        self.monoky3=Monoky()

    def __repr__(self):
        return f"monky1{self.monoky1.getArray()} monky2{self.monoky2.getArray()} monky3{self.monoky3.getArray()}"

    def play(self):
        for i in range(20):
            self.monoky1.send(self.monoky2,self.monoky3,5)
            self.monoky2.send(self.monoky1,self.monoky3,3)
            self.monoky3.send(self.monoky2,self.monoky1,2)

class Monoky():
    def __init__(self) -> None:
        self.array = ds.Queues()
        ds.generateRandomArray(self.array, 2, 5)

    def getArray(self):
        return self.array

    def append(self, num:int):
        self.getArray().append(num)

    def play(self, monoky1, monoky2, num):
        self.send(monoky1, monoky2, num)

    def send(self, monoky1, monoky2, num):
        if self.getArray().get():
            aux = self.pop()
            if aux%num==0 :
                monoky1.append((aux//3)*(1+num))
            else:
                monoky2.append((aux//2)*(num-1))

    def pop(self):
        return self.getArray().pop()

def operator():
    pass

gTest = WhoHaveMoreItems()
print(gTest)
gTest.play()
print(gTest)