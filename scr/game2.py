import random as rm

class RandomNumers:
    def __init__(self, minInt:int, maxInt:int):
        self.minInt = minInt
        self.maxInt = maxInt
    
    def generate(self) -> int:
        return rm.randint(self.minInt, self.maxInt)

    def play(self):
        print("Welcom random numers")
        num = int(input("input int: "))
        num2 = self.generate()
        i=0
        while num != num2:
            i+=1
            if(num > num2) :
                print("is max that X")
            else:
                print("is min that X")
            num = int(input("input int: "))
        print("ACCURATE, intent= " + str(i))
        