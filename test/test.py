import unittest
import scr.dataStructureSystems as ds, scr.game1 as g1, scr.game2 as g2

rps = g1.RockPaperSiccors()
rng = g2.RandomNumers(1, 10)

class Test(unittest.TestCase):

    def test_RSPCaseDrawTrue(self):
        self.assertTrue(rps.drawCondition(1, rps.get(1)))
        self.assertTrue(rps.drawCondition(2, rps.get(2)))
        self.assertTrue(rps.drawCondition(3, rps.get(3)))
    
    def test_RSPCaseDrawFalse(self):
        self.assertFalse(rps.drawCondition(1, rps.get(2)))
        self.assertFalse(rps.drawCondition(2, rps.get(3)))
        self.assertFalse(rps.drawCondition(3, rps.get(1)))

    def test_RSPCaseWinTrue(self):
        self.assertTrue(rps.winCondition(1, rps.get(3)))
        self.assertTrue(rps.winCondition(3, rps.get(2)))
        self.assertTrue(rps.winCondition(2, rps.get(1)))

    def test_RSPCaseWinFalse(self):
        self.assertFalse(rps.winCondition(1, rps.get(1)))
        self.assertFalse(rps.winCondition(2, rps.get(2)))
        self.assertFalse(rps.winCondition(3, rps.get(3)))
        self.assertFalse(rps.winCondition(1, rps.get(2)))
        self.assertFalse(rps.winCondition(2, rps.get(3)))
        self.assertFalse(rps.winCondition(3, rps.get(1)))

    def test_RNGnumberIn(self):
        self.assertFalse(rng.generate in [1,2,3,4,5,6,7,8,9,10])
        self.assertFalse(rng.generate in [1,2,3,4,5,6,7,8,9,10])
        self.assertFalse(rng.generate in [1,2,3,4,5,6,7,8,9,10])
        self.assertFalse(rng.generate in [1,2,3,4,5,6,7,8,9,10])
        self.assertFalse(rng.generate in [1,2,3,4,5,6,7,8,9,10])