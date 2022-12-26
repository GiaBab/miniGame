import dataStructureSystems as ds


class WhatHaveMoreItems():
    def __init__(self) -> None:
        pass

    def play():
        pass 

class Monoky():
    def __init__(self) -> None:
        self.array = ds.Queues()
        ds.generateRandomArray(self.array, 1, 5)

    def get(self):
        return self.array

    def append(self, num):
        self.get().append(num)

    def play(self):
        
        self.send
        pass 

    def send(self, monoky1, monoky2, num):
        aux = self.array.pop()
        if(aux%num==0):
            monoky1.append(aux//3)
        else:
            monoky2.append(aux//2)

'''
##test1
h = Monoky() 
j = Monoky() 
k = Monoky() 

print(f"mono1 {h.get()}")
print(f"mono2 {j.get()}")
print(f"mono3 {k.get()}")

h.send(j, k, 2)

print(f"mono1 {h.get()}")
print(f"mono2 {j.get()}")
print(f"mono3 {k.get()}")
'''