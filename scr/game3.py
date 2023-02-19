import dataStructureSystems as ds

class WhoHaveMoreItems():
    def __init__(self) -> None:
        self.monoky1=Monoky()
        self.monoky2=Monoky()
        self.monoky3=Monoky()

    def __repr__(self):
        return f"monky1{self.monoky1.getArray()} monky2{self.monoky2.getArray()} monky3{self.monoky3.getArray()}"

    def play(self):
        i=0
        while i < 5:
            self.monoky1.send(self.monoky2,self.monoky3,5)
            self.monoky2.send(self.monoky1,self.monoky3,3)
            self.monoky3.send(self.monoky2,self.monoky1,2)
            i+=1

    def len(self):
        return [self.monoky1.len(), self.monoky2.len(), self.monoky3.len()]
    
    def whoHaveMoreItems(self):
        for i in range(self.len()):
            if self.len()[i] == max(self.len()) :
                return i

    def winCondition(self):
        num = int(input()) 
        if self.whoHaveMoreItems() == num :
            print("you win :)")


class Monoky():
    def __init__(self) -> None:
        self.items = ds.Queues()
        ds.generateRandomArray(self.items, 2, 5)

    def append(self, num:int):
        return self.getArray().append(num)

    def send(self, monoky1, monoky2, num):
        if self.getArray().get():
            aux = self.pop()
            if aux%num==0 :
                monoky1.append((aux//3)*(1+num))
            else:
                monoky2.append((aux//2)*(num-1))

    def pop(self):
        return self.getArray().pop()

    def len(self):
        return self.items.len()

