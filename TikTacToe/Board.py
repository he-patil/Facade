from pytest import mark
from Cell import Cell

class Board():
    def __init__(self):
        self.cells = [Cell() for i in range(9)]

    def printBoard(self):
        for i in range(9):
            if self.cells[i].isMarked():
                print(self.cells[i].mark, end=" ")
            else:
                print("-", end=" ")
            if not (i+1)%3:
                print()
        print("------------------------------------")

    def resultAnalyser(self):
        horizontalCheck, symbol = self.horizontalCheck()
        if horizontalCheck:
            return symbol
        
        verticalCheck, symbol = self.verticalCheck()
        if verticalCheck:
            return symbol
        
        diagonalCheck, symbol = self.diagonalCheck()
        if diagonalCheck:
            return symbol

        for cell in self.cells:
            if cell.mark == "":
                return ""
        
        return "Draw"

    def horizontalCheck(self):
        if self.cells[0].mark != "" and self.cells[0].mark == self.cells[1].mark and self.cells[0].mark == self.cells[2].mark:
            return True, self.cells[0].mark
        if self.cells[3].mark != "" and self.cells[3].mark == self.cells[4].mark and self.cells[3].mark == self.cells[5].mark:
            return True, self.cells[3].mark
        if self.cells[6].mark != "" and self.cells[6].mark == self.cells[7].mark and self.cells[6].mark == self.cells[8].mark:
            return True, self.cells[6].mark
        return False, ""

    def verticalCheck(self):
        if self.cells[0].mark != "" and self.cells[0].mark == self.cells[3].mark and self.cells[0].mark == self.cells[6].mark:
            return True, self.cells[0].mark
        if self.cells[1].mark != "" and self.cells[1].mark == self.cells[4].mark and self.cells[1].mark == self.cells[7].mark:
            return True, self.cells[1].mark
        if self.cells[2].mark != "" and self.cells[2].mark == self.cells[5].mark and self.cells[2].mark == self.cells[8].mark:
            return True, self.cells[2].mark
        return False, ""

    def diagonalCheck(self):
        if self.cells[0].mark != "" and self.cells[0].mark == self.cells[4].mark and self.cells[0].mark == self.cells[8].mark:
            return True, self.cells[0].mark
        if self.cells[2].mark != "" and self.cells[2].mark == self.cells[4].mark and self.cells[2].mark == self.cells[6].mark:
            return True, self.cells[2].mark
        return False, ""
