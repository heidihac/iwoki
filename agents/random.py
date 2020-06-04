from player import Player
import gameState
import random

class RandomPlayer(Player):
    """ 
    Class to implement the Random player.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Function that plays agent Random's turn. It chooses randomly the action to be executed.
        PARAMETER:
            gameState: current game state.
        """
        if not gameState.gameOver:
            actions = gameState.getActions(self)
            chosenAction = random.choice(actions)
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            