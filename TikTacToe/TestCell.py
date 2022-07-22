from Cell import Cell
cell = Cell()

class TestCell():
    def test_isMarked1(self):
        assert cell.isMarked() == False

    def test_isMarked2(self):
        cell.mark = "X"
        assert cell.isMarked() == True

    def test_isMarked3(self):
        cell.mark = "O"
        assert cell.isMarked() == True

    def test_isMarked4(self):
        cell.mark = "abc"
        assert cell.isMarked() == False

test = TestCell()
test.test_isMarked1()
test.test_isMarked2()
test.test_isMarked3()
test.test_isMarked4()