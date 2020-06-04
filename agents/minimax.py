from player import Player
import gameState
from copy import deepcopy
import time

class MinimaxPlayer(Player):
    """ 
    Class to implement the Minimax player, with alpha-beta pruning and suspension in depth and time.
    """
    
    INFINITE = 10000
    DEPTH = 3

    def __init__(self, name):
        super().__init__(name)
        self.maxTime = 90000 # miliseconds. Maximum exploration time of each of the branches hanging from the root node
        self.numNodes = 0 # For metrics.
        self.startTime = None # It sets the initial time value to determine when the search limit is exceeded on a main branch of the root node
        self.Qfile = None
        
        if self.gotTileBefore:
            self.bestAction = [['passTurn', None, None, None, 0]]
        else:
            self.bestAction = ['getSmallTile', None, None, None, 0]
        
        
    def generateChildNode(self, gameState, action, playerType):
        """ 
        Function to generate a clone of the gameState and execute the action on it . 
        PARAMETERS:
            gameState: current game state to be cloned.
            action: action to be executed on the new game state clone.
            playerType: MAX --> Minimax
                        min --> Opponent
        RETURN:
            newGameState: Resulting game state.
        """

        newGameState = deepcopy(gameState) # The gameState is cloned
        if playerType == 'MAX':
            player = [p for p in newGameState.players if p.name == 'Minimax'][0]
        else:
            player = [p for p in newGameState.players if p.name != 'Minimax'][0]
            
        newGameState.move(action, player) # The action is executed on the newGameState
        self.numNodes += 1

        return newGameState
                
    
    def alpha_beta(self, gameState, depth=DEPTH, alpha=-INFINITE, beta=INFINITE, playerType='MAX'):
        """ 
        Function that recursively explores the MINIMAX tree with ALPHA-BETA pruning
        PARAMETERS:
            gameState: current game state.
            depth: depth of exploration. By default DEPTH.
            alpha, beta: values to be updated in each node. By default -INFINITE and INFINITE, respectively.
            playerType: MAX --> Minimax
                        min --> Opponent
        RETURN:
            alfa/beta: updated value for the current node.
            bestAction: selected action.
        """
        if depth == self.DEPTH:
            self.startTime = time.time()
        minimaxPlayer = [p for p in gameState.players if p.name == 'Minimax'][0]
        otherPlayer = [p for p in gameState.players if p.name != 'Minimax'][0]

        if gameState.gameOver or depth == 0: # Terminal node reached either by game over or by depth. The value returned is the difference in scores between the player and its opponent after the final point tally
            return gameState.finalPointTally(minimaxPlayer)[0] - gameState.finalPointTally(otherPlayer)[0], None
        
        if time.time() > self.startTime + self.maxTime/1000: # Terminal node reached by maxTime. It returns the most promising action of those explored so far
            return alpha, self.bestAction

        if playerType == 'MAX':
            # The tree expands to a new level of depth. A child node is generated for every possible action of the gameState
            for action in gameState.getActions(minimaxPlayer):
                newGameState = self.generateChildNode(gameState, action, playerType)
                alpha_prev = alpha
                
                if len(otherPlayer.smallTiles) == 0:
                    newGameState.gameOver = True
                    
                alpha = max(alpha, self.alpha_beta(newGameState, depth-1, alpha, beta, 'min')[0])
                if alpha > alpha_prev and depth == self.DEPTH:
                    self.bestAction = action
                if alpha >= beta:
                    return alpha, self.bestAction # The tree is pruned from this branch

            return alpha, self.bestAction
        
        else: # min
             # The tree expands to a new level of depth. A child node is generated for every possible action of the gameState
            for action in gameState.getActions(otherPlayer):
                newGameState = self.generateChildNode(gameState, action, playerType)
                
                if len(minimaxPlayer.smallTiles) == 0:
                    newGameState.gameOver = True

                beta = min(beta, self.alpha_beta(newGameState, depth-1, alpha, beta, 'MAX')[0])
                if alpha >= beta:
                    return beta, None # The tree is pruned from this branch
                
            return beta, None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Function that plays the turn of Agent Minimax. It starts the MINIMAX tree exploration to select the best action and executes it.
        PARAMETER:
            gameState: current game state.
        """
        if not gameState.gameOver:
            chosenAction = self.alpha_beta(gameState)[1]
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            