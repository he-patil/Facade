from Player import Player
from Cell import Cell

player = Player("Player1","X")
cell = Cell()

class TestPlayer():
    def test_markCell1(self):
        player = Player("Player1","X")
        cell = Cell()
        player.markCell(cell)
        print(player.symbol)
        print(cell.mark)
        print(cell.mark == "X")
        assert cell.mark == "X"

    def test_markCell2(self):
        player.symbol = "O"
        player.markCell(cell)
        assert cell.mark == "O"

    def test_markCell3(self):
        player.symbol = "abc"
        player.markCell(cell)
        assert cell.mark == ""

test = TestPlayer()
test.test_markCell1()
test.test_markCell2()
test.test_markCell3()