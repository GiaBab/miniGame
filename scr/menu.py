from scr.game1 import RockPaperSiccors
from scr.game2 import RandomNumers

class MenuGame:
    def __init__(self):
        self.opc = ["RPS", "RN"]
    
    def games(self):
        item1 = RockPaperSiccors()
        item2 = RandomNumers(0, 10)
        return item1, item2

    def play(self):
        self.opcions()
        opc = int(input("input: "))
        item1, item2 = self.games()
        match opc :
            case 1 : item1.play()

            case 2 : item2.play()

    def opcions(self):
        for i in range(len(self.opc)) :
            print(f"[{i+1}]-{self.opc[i]}")