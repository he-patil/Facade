
from Player import Player
from Deck import Deck
import random

class Game():
    def __init__(self, playerName1, playerName2):
        self.player1 = Player(playerName1,0)
        self.player2 = Player(playerName2,0)
        self.deck = Deck.createDeck()
        self.currentPlayer = "player1"
        self.isAce = False
        self.isLastSkipped = False

    def play(self):
        while True:
            self.displayScore()
            isDraw = random.randint(0, 10) #Input For Draw or Skip

            if not isDraw:
                if self.isLastSkipped:
                    _, message = self.skipTurn()
                    print(message)
                    return self.finishGame()

                _, message = self.skipTurn()
                print(message)
                
            else:   
                index = random.randint(0,len(self.deck.cards)-1) #Input for card index
                isDrawn, message, isAce = self.drawCard(index)
                print(message)
                if isAce:
                    isDrawn, message = self.inputAceValue(random.choice([1,11])) #Input Ace Value
                    print(message)
            
                if self.player1.points>=21 or self.player2.points>=21:
                    return self.finishGame()

    def finishGame(self):
        self.displayScore()
        if self.isLastSkipped:
            if self.player1.points == self.player2.points:
                print("Match Drawn!")
            elif self.player1.points > self.player2.points:
                print(self.player1.name+ " Wins!")
            else:
                print(self.player2.name+ " Wins!")
            
        else:
            if self.player1.points == 21:
                print(self.player1.name+ " Wins!")
            else:
                print(self.player2.name+ " Wins!")

        return 0

    def drawCard(self, index): #Returns isDrawn, Message, isAce
        if self.isAce:
            return False, "Input Ace Value First", False

        if index<0 or index>=len(self.deck.cards):
            return False, "Index Out of Bounds", False
        
        self.isLastSkipped = False
        value = self.deck.cards[index].value
        self.deck.cards.remove(self.deck.cards[index])

        playerName = getattr(self, self.currentPlayer).name
        if value == 1:
            self.isAce = True
            return False, playerName+" Drawn Ace", True

        
        getattr(self, self.currentPlayer).drawCard(value)
        if self.currentPlayer == "player1":
            self.currentPlayer = "player2"
        else:
            self.currentPlayer = "player1"
        
        return True, playerName+" drawn value "+ str(value), False
        
    def displayScore(self):
        print("--------------")
        print(self.player1.name+": "+str(self.player1.points))
        print(self.player2.name+": "+str(self.player2.points))
        print("--------------")

    def inputAceValue(self, value):
        if value!= 1 and value != 11:
            return False, "Input either 1 or 11"

        playerName = getattr(self, self.currentPlayer).name
        getattr(self, self.currentPlayer).drawCard(value)
        if self.currentPlayer == "player1":
            self.currentPlayer = "player2"
        else:
            self.currentPlayer = "player1"
        self.isAce = False
        return True, playerName+" drawn value "+ str(value)

    def skipTurn(self):
        if self.isAce:
            return False, "Input Ace Value First", False

        playerName = getattr(self, self.currentPlayer).name
        
        if self.currentPlayer == "player1":
            self.currentPlayer = "player2"
        else:
            self.currentPlayer = "player1"
        
        self.isLastSkipped = True

        return True, playerName+" Skipped Turn"

def main():
    game1 = Game("Player1", "Player2")
    game1.play()

if __name__ == "__main__":
    main()

################################## Output 1 #############################
# --------------
# Player1: 0
# Player2: 0
# --------------        
# Player2 drawn value 9 
# --------------        
# Player1: 0
# Player2: 9
# --------------
# Player1 drawn value 3
# --------------
# Player1: 3
# Player2: 9
# --------------
# Player1 drawn value 5
# --------------
# Player1: 8
# Player2: 9
# --------------
# Player1 drawn value 10
# --------------
# Player1: 18
# Player2: 9
# --------------
# Player2 drawn value 10
# --------------
# Player1: 18
# Player2: 19
# --------------
# Player2 Drawn Ace
# Player2 drawn value 1
# --------------
# Player1: 18
# Player2: 20
# --------------
# Player1 drawn value 2
# --------------
# Player1: 20
# Player2: 20
# --------------
# Player1 drawn value 10
# --------------
# Player1: 30
# Player2: 20
# --------------
# Player2 Wins!
#########################################################################

################################## Output 2 #############################
# --------------
# Player1: 0
# Player2: 0
# --------------
# Player1 Skipped Turn
# --------------
# Player1: 0
# Player2: 0
# --------------
# Player2 Skipped Turn
# --------------
# Player1: 0
# Player2: 0
# --------------
# Match Drawn!
#########################################################################

################################## Output 3 #############################
# --------------
# Player1: 0
# Player2: 0
# --------------
# Player1 drawn value 9
# --------------
# Player1: 9
# Player2: 0
# --------------
# Player2 drawn value 9
# --------------
# Player1: 9
# Player2: 9
# --------------
# Player1 Skipped Turn
# --------------
# Player1: 9
# Player2: 9
# --------------
# Player2 drawn value 5
# --------------
# Player1: 9
# Player2: 14
# --------------
# Player1 Drawn Ace
# Player1 drawn value 11
# --------------
# Player1: 20
# Player2: 14
# --------------
# Player2 drawn value 3
# --------------
# Player1: 20
# Player2: 17
# --------------
# Player1 drawn value 7
# --------------
# Player1: 27
# Player2: 17
# --------------
# Player2 Wins!
#########################################################################

################################## Output 4 #############################
# --------------
# Player1: 0
# Player2: 0
# --------------
# Player1 drawn value 5
# --------------
# Player1: 5
# Player2: 0
# --------------
# Player2 drawn value 5
# --------------
# Player1: 5
# Player2: 5
# --------------
# Player1 drawn value 3
# --------------
# Player1: 8
# Player2: 5
# --------------
# Player2 drawn value 2
# --------------
# Player1: 8
# Player2: 7
# --------------
# Player1 drawn value 6
# --------------
# Player1: 14
# Player2: 7
# --------------
# Player2 drawn value 2
# --------------
# Player1: 14
# Player2: 9
# --------------
# Player1 drawn value 7
# --------------
# Player1: 21
# Player2: 9
# --------------
# Player1 Wins!
#########################################################################