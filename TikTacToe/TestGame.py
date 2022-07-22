from Player import Player
from Cell import Cell
from Board import Board
from Game import Game

# player = Player("Player1","X")
# cell = Cell()

game = Game("Player1", "Player2")

class TestGame():
    def test_play1(self):
        game = Game("Player1", "Player2")
        game.play(1)
        assert game.board.cells[0].mark == "O"
    
    def test_play2(self):
        game = Game("Player1", "Player2")
        assert game.play(11) == "Wrong Cell Number"

    def test_play3(self):
        game = Game("Player1", "Player2")
        game.play(1)
        game.play(3)
        game.play(4)
        game.play(5)
        result = game.play(7)
        assert result == "Player1(O) Wins!"

    def test_play4(self):
        game = Game("Player1", "Player2")
        game.play(1)
        game.play(3)
        game.play(4)
        game.play(5)
        game.play(7)
        assert game.isFinished == True
    
    def test_play5(self):
        game = Game("Player1", "Player2")
        assert game.isFinished == False
    
    def test_play6(self):
        game = Game("Player1", "Player2")
        assert game.activePlayer == 1

    def test_play7(self):
        game = Game("Player1", "Player2")
        game.play(1)
        assert game.activePlayer == 2

    def test_play8(self):
        game = Game("Player1", "Player2")
        game.play(2)
        game.play(1)
        game.play(3)
        game.play(4)
        game.play(5)
        result = game.play(7)
        assert result == "Player2(X) Wins!"

    def test_play9(self):
        game = Game("Player1", "Player2")
        game.play(1)
        game.play(3)
        game.play(2)
        game.play(4)
        game.play(6)
        game.play(5)
        game.play(7)
        game.play(9)
        result = game.play(8)
        assert result == "Match Drawn!"

test = TestGame()

test.test_play1()
test.test_play2()
test.test_play3()
test.test_play4()
test.test_play5()
test.test_play6()
test.test_play7()
test.test_play8()
test.test_play9()
