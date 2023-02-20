import scr.game1 as g1, scr.game2 as g2, scr.game3 as g3

class MenuGame:
    def __init__(self):
        self.opc = ["RockPaperScissor", "RandomNumber", "WhoHaveMoreItems"]
        self.game1 = g1.RockPaperSiccors()
        self.game2 = g2.RandomNumers(0, 10)
        self.game3 = g3.WhoHaveMoreItems()

    def play(self):
        self.opcions()
        opc = int(input("input: "))
        match opc :
            case 1 : self.game1.play()

            case 2 : self.game2.play()

            case 3 : self.game3.play()

            case _ : raise Exception("no more opcions")

    def opcions(self):
        [print(f"[{i}]-{opc}") for i, opc in enumerate(self.opc,1)]