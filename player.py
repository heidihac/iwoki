import numpy as np
from collections import namedtuple

class Player:
    """
    Class that represents the agent.
    """
    def __init__(self, name):
        self.name = name # Player's name (agent)
        self.isTurn = False # Indicates if it is the agent's turn
        self.smallTiles = [] # List of small tiles owned by the agent
        self.hexagonalTiles = [] # List of heagonal tiles owned by the agent
        self.score = 0 # Score
        self.redIndicator = False # Red token. It is activated to indicate to the opponent that he has only one small tile left
        self.whiteIndicators = 0 # White tokens. It is the counter of the number of actions performed to get a new hexagonal tile
        self.gotTileBefore = False # Flag used to avoid the agent drawing a small tile twice in the same turn
        self.numWins = 0 # For metrics
        self.numTurns = 0 # For metrics
        self.accumulatedScore = 0 # For metrics
        
        self.PublicState = namedtuple('PublicState',[ # namedtuple representing the public attributes of the agent
            'hexagonalTiles', # ordered tuple of strings ('ht1', 'ht2', ....)
            'numSmallTiles', # Integer
            'redIndicator', # Boolean
            'whiteIndicators', # Integer
        ])
        
        self.PrivateState = namedtuple('PrivateState',[ # namedtuple representing the private attributes of the agent
            'smallTiles',  # ordered tuple of strings ('st1', 'st2', ....)
            'publicState' # namedtuple representing the public attributes of the agent
        ])
        
        
    def getMove(self, gameState, *args, **kwargs):
        
        return None
    
    
    def gameOver(self, score, *args, **kwargs):
        
        return None
    
    
    def getPublicState(self): 
        """
        Function that gathers the public attributes of the agent.
        RETURN:
            namedtuple PublicState
        """
        return self.PublicState(
            hexagonalTiles = tuple(sorted([
                tile.id
                for tile in self.hexagonalTiles
            ])), # ordered tuple of strings ('ht1', 'ht2', ....)
            numSmallTiles = len(self.smallTiles), # Integer
            redIndicator = self.redIndicator, # Boolean
            whiteIndicators = self.whiteIndicators, # Integer
        )
    
        
    def getPrivateState(self):
        """
        Function that gathers the private attributes of the agent.
        RETURN:
            namedtuple PrivateState
        """
        return self.PrivateState(
            smallTiles = tuple(sorted([
                'st'+str(int(tile.id[2:])%12) # To simplify, the tile is identified with one of 12 different existing ones
                for tile in self.smallTiles
            ])), # ordered tuple of strings ('ht1', 'ht2', ....)
            publicState = self.getPublicState()
        )

    