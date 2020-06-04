from player import Player
import gameState

class HumanPlayer(Player):
    """ 
    Class to implement the Human player.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Function that implements a simple API to allow the human player to play his turn.
        PARAMETER:
            gameState: current game state.
        """
        if not gameState.gameOver:
            actions = gameState.getActions(self)
            while True:  
                print ("\nEnter your play number:")
                num = 1
                for action in actions:
                    print ("{} - {}".format(num, action))
                    num += 1
                optionMenu = input()
                if int(optionMenu) > 0 and int(optionMenu) <= num:
                    chosenAction = actions[int(optionMenu)-1]
                    break
                else:
                    print("Wrong option")
                    continue
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            