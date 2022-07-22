from Cell import Cell

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def markCell(self, cell):
        if cell.isMarked():
            return False, "Cell Already Marked! Attempt Again"
        if self.symbol in ["X","O"]:
            cell.mark = self.symbol
        else:
            cell.mark = ""
        
        return True, "Cell Marked"