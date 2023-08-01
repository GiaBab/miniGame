import dataStructureSystems as ds, numpy as np

class TicTacToe :
    def __init__(self):
        self.array = [['','',''],['','',''],['','','']]
    
    def __repr__(self) -> str:
        return f"{self.array[0]}\n{self.array[1]}\n{self.array[2]}"  

    def condictionInRow(self) -> bool:
        return ds.anyWhen(ds.allEqual, self.array)

    def condictionInDiagonal(self) -> bool:
        arrayAux = np.array(self.array)
        return ds.allEqual(arrayAux.diagonal()) or ds.allEqual(np.flip(arrayAux,0).diagonal())

    def conditcionInColumns(self) -> bool:
        return ds.anyWhen(ds.allEqual, ds.rawToColumn(self.array))
    
    def winConditcion(self) -> bool:
        return self.condictionInDiagonal() or self.condictionInRow() or self.conditcionInColumns()

    def put(self, x:int, y:int, elemn:str):
        self.array[x][y] = elemn

    def play(self):
        print(self)
        while(not (self.winConditcion or all(self.array))):
            self.put(int(input("x:")),int(input("y:")),str(input("elemn")))
            print(self)

