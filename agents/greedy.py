from player import Player
import gameState

class GreedyPlayer(Player):
    """ 
    Class to implement the Greedy player. It chooses the best short-term move on each turn.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

        
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Function that play agent Greedy's turns.
        All possible actions are reviewed and the one that provides the highest score is selected.
        It will never choose to voluntarily draw a small tile if there is a possibility of placing another one, either small or hexagonal.
        At equal points, the method will choose the option of placing a small tile before a hexagonal one.
        PARAMETER:
            gameState: current game state.
        """
        if not gameState.gameOver:
            actions = gameState.getActions(self)
            chosenAction = []
            maxScore = -1
            for action in actions:
                if int(action[4]) > maxScore:
                    maxScore = action[4]
                    chosenAction = action
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            