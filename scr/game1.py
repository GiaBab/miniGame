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

    def drawCondition(self, user, cpu):
        return cpu == self.get(user)

    def play(self):
        print("Welcom Rock Paper Siccors")
        self.opcions()
        user = int(input("select"))
        cpu = self.getCup()
        if (self.winCondition(user, cpu)):
            print(f"user={self.get(user)} vs cpu={cpu} - win User")
        elif(self.drawCondition(user, cpu)):
            print(f"user={self.get(user)} vs cpu={cpu} - draw")
        else:
            print(f"user={self.get(user)} vs cpu={cpu} - lose User")
            
    def opcions(self):
        for i in range(len(self.dic)):
            print(f"[{i+1}]- {self.get(i+1)}")
