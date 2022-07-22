
from Player import Player
from Board import Board


singleton = None
class Game():
    def __init__(self, playerNameO, playerNameX):
        self.playerO = Player(playerNameO,"O")
        self.playerX = Player(playerNameX,"X")
        self.board = Board()
        self.activePlayer = 1
        self.isFinished = False

    @staticmethod
    def createGame(playerNameO, playerNameX):
        global singleton
        if singleton == None:
            singleton = Game(playerNameO, playerNameX)
        return singleton

    def play(self, cellIndex):
        if self.isFinished:
            return "This Game is Already Finished"

        if cellIndex>9 or cellIndex<1:
            return "Wrong Cell Number"

        cellIndex-=1

        if self.activePlayer == 1:
            isMarked, message = self.playerO.markCell(self.board.cells[cellIndex])
            if not isMarked:
                return message
            self.activePlayer = 2
            playerName = self.playerX.name
        else:
            isMarked, message = self.playerX.markCell(self.board.cells[cellIndex])
            if not isMarked:
                return message
            self.activePlayer = 1
            playerName = self.playerO.name

        self.board.printBoard()
        result = self.board.resultAnalyser()
        if result != "":
            return self.stopGame(result)
        return str(playerName)+ "'s Turn"

    def stopGame(self, result):
        self.isFinished = True
        if result == "Draw":
            return "Match Drawn!"
        return getattr(self,"player"+result).name+"("+result+")"+" Wins!"

def main():
    game1 = Game.createGame("Player1", "Player2")
    game2 = Game.createGame("P3","P4")

    print(str(game1 == game2), game2.playerO.name)
    return

    print(game1.play(3))
    print(game1.play(2))
    print(game1.play(4))
    print(game1.play(5))
    print(game1.play(8))
    print(game1.play(6))
    print(game1.play(1))
    print(game1.play(1))
    print(game1.play(9))
    print(game1.play(7))

if __name__ == "__main__":
    main()

################################## Output 1 #############################
# - - O 
# - - - 
# - - - 
# ------------------------------------
# Player2's Turn
# - X O 
# - - - 
# - - - 
# ------------------------------------
# Player1's Turn
# - X O 
# O - - 
# - - - 
# ------------------------------------
# Player2's Turn
# - X O 
# O X - 
# - - - 
# ------------------------------------
# Player1's Turn
# - X O 
# O X -
# - O -
# ------------------------------------
# Player2's Turn
# - X O
# O X X
# - O -
# ------------------------------------
# Player1's Turn
# O X O
# O X X
# - O -
# ------------------------------------
# Player2's Turn
# Cell Already Marked! Attempt Again
# O X O
# O X X
# - O X
# ------------------------------------
# Player1's Turn
# O X O
# O X X
# O O X
# ------------------------------------
# Player1(O) Wins!
#########################################################################