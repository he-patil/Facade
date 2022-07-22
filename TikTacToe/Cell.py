class Cell():
    def __init__(self, mark = ""):
        self.mark = mark
    
    def isMarked(self):
        if self.mark in ["X","O"]:
            return True
        return False