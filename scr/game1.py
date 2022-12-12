import random as rm

class RockPaperSiccors :
    def __init__(self):
        self.dic = {1:'Rock', 2:'Paper', 3:'Siccor'}
    
    def get(self, opc):
        return self.dic[opc]
    
    def getCup(self):
        cpuOpc = rm.choice([1, 2, 3])
        return self.get(cpuOpc)

    def winCondition(self, user, cpu):
        return (self.get(user) == 'Rock' and cpu == 'Siccor') or (self.get(user) == 'Paper' and cpu == 'Rock') or (self.get(user) == 'Siccor' and cpu == 'Paper')

    def play(self):
        print("Welcom Rock Paper Siccors")
        for i in range(len(self.dic)):
            print(f"[{i+1}]- {self.get(i+1)}")
        user = int(input("select"))
        cpu = self.getCup()
        if (self.winCondition(user, cpu)):
            print(f"user={self.get(user)} vs cpu={cpu} - win User")
        elif(cpu == self.get(user)):
            print(f"user={self.get(user)} vs cpu={cpu} - draw")
        else:
            print(f"user={self.get(user)} vs cpu={cpu} - lose User")