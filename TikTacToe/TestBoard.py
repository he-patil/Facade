from Player import Player
from Cell import Cell
from Board import Board

# player = Player("Player1","X")
# cell = Cell()

board = Board()

def fillBoard(board, list):
    for i in range(9):
        board.cells[i].mark = list[i]

class TestBoard():
    def test_resultAnalyser1(self):
        board = Board()
        assert board.resultAnalyser() == ""

    def test_resultAnalyser2(self):
        fillBoard(board,["X","X","X",
                        "O","O","",
                        "O","",""])

        assert board.resultAnalyser() == "X"
        
    def test_resultAnalyser3(self):
        fillBoard(board,["X","O","O",
                        "X","O","",
                        "X","",""])

        assert board.resultAnalyser() == "X"

    def test_resultAnalyser4(self):
        fillBoard(board,["X","O","O",
                        "","X","",
                        "","O","X"])

        assert board.resultAnalyser() == "X"

    def test_resultAnalyser5(self):
        fillBoard(board,["","X","",
                        "","X","",
                        "O","O","O"])
                        
        assert board.resultAnalyser() == "O"

    def test_resultAnalyser6(self):
        fillBoard(board,["X","","O",
                        "","X","O",
                        "","","O"])
                        
        assert board.resultAnalyser() == "O"

    def test_resultAnalyser7(self):
        fillBoard(board,["X","X","O",
                        "","O","",
                        "O","",""])

        assert board.resultAnalyser() == "O"
    
    def test_resultAnalyser8(self):
        fillBoard(board,["X","O","O",
                        "","","",
                        "","","X"])

        assert board.resultAnalyser() == ""

    def test_resultAnalyser9(self):
        fillBoard(board,["O","O","X",
                        "X","X","O",
                        "O","O","X"])

        assert board.resultAnalyser() == "Draw"
    
        
test = TestBoard()
test.test_resultAnalyser1()
test.test_resultAnalyser2()
test.test_resultAnalyser3()
test.test_resultAnalyser4()
test.test_resultAnalyser5()
test.test_resultAnalyser6()
test.test_resultAnalyser7()
test.test_resultAnalyser8()
test.test_resultAnalyser9()