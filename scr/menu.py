import scr.game1 as g1, scr.game2 as g2, scr.game3 as g3

class MenuGame:
    def __init__(self):
        self.opc = ["RockPaperScissor", "RandomNumber", "WhoHaveMoreItems"]
        self.item1 = g1.RockPaperSiccors()
        self.item2 = g2.RandomNumers(0, 10)
        self.item3 = g3.WhoHaveMoreItems()

    def play(self):
        self.opcions()
        opc = int(input("input: "))
        match opc :
            case 1 : self.item1.play()

            case 2 : self.item2.play()

            case 3 : self.item3.play()

    def opcions(self):
        [print(f"[{i+1}]-{opc}") for i, opc in enumerate(self.opc)]