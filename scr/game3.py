import scr.dataStructureSystems as ds

class WhoHaveMoreItems():
    def __init__(self) -> None:
        self.monoky1=Monoky()
        self.monoky2=Monoky()
        self.monoky3=Monoky()

    def __repr__(self) -> str:
        return f"monky1{self.monoky1.get()} monky2{self.monoky2.get()} monky3{self.monoky3.get()}"

    def play(self):
        self.rule()
        i=0
        while i < 5:
            self.monoky1.send(self.monoky2,self.monoky3,5)
            self.monoky2.send(self.monoky1,self.monoky3,3)
            self.monoky3.send(self.monoky2,self.monoky1,2)
            i+=1
        self.winCondition()

    def rule(self):
        print("You have 3 monoky in lab, monoky have items what is going to pass and you must do guess who monoky have more items.")
        print("monoky1 if item is divisibility for 5, divide for 3 also sum 1, and pass to monoky2, else divide for 2 also take 1 and pass to monoky3")
        print("monoky2 if item is divisibility for 3, divide for 3 also sum 1, and pass to monoky1, else divide for 2 also take 1 and pass to monoky3")
        print("monoky3 if item is divisibility for 2, divide for 3 also sum 1, and pass to monoky1, else divide for 2 also take 1 and pass to monoky3")
        print("this process repeat to 5 times")
        print("ALERT: division don't have decimal")
        print(self)

    def allLen(self):
        return [self.monoky1.len(), self.monoky2.len(), self.monoky3.len()]
    
    def whoHaveMoreItems(self) -> int:
        for i in range(len(self.allLen())):
            if self.allLen()[i] == max(self.allLen()) :
                return i

    def winCondition(self):
        num = int(input()) 
        if self.whoHaveMoreItems() == num-1 :
            print("you win :)")
        else :
            print("you lose :(")

class Monoky():
    def __init__(self) -> None:
        self.items = ds.Queues()
        ds.generateRandomArray(self.items, 2, 5)

    def append(self, num:int) -> int:
        return self.items.append(num)

    def send(self, monoky1, monoky2, num):
        if self.items.get():
            aux = self.pop()
            if aux%num==0 :
                monoky1.append((aux//3)*(1+num))
            else:
                monoky2.append((aux//2)*(num-1))

    def get(self):
        return self.items.get()

    def pop(self) -> int:
        return self.items.pop()

    def len(self) -> int:
        return self.items.len()

'''def testing():
    gTest = WhoHaveMoreItems()
    print(gTest)
    gTest.play()
    print(gTest)
    print(gTest.allLen())

testing()'''