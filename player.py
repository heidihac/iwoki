import numpy as np
from collections import namedtuple

class Player:
    """
    Clase que representa al agente.
    """
    def __init__(self, name):
        self.name = name # Nombre del jugador (agente)
        self.isTurn = False # Indica si es el turno del agente
        self.smallPieces = [] # Lista de fichas pequeñas que tiene el agente
        self.hexagonalPieces = [] # Lista de fichas hexagonales que tiene el agente
        self.score = 0 # Puntuación
        self.redIndicator = False # Indicador o testigo rojo, que se activa para indicar al oponentede que le queda una única ficha pequeña.
        self.whiteIndicator = 0 # Indicador o testigo blanco, que sirve de contador del número de acciones realizadas para conseguir una nueva ficha hexagonal.
        self.gotPieceBefore = False # Indicador utilizado para impedir al agente robar una ficha pequeña dos veces en un mismo turno.
        self.numWins = 0 # Dato para la obtención de métricas
        self.numTurns = 0 # Dato para la obtención de métricas
        self.accumulatedScore = 0 # Dato para la obtención de métricas
        
        self.PublicState = namedtuple('PublicState',[ # namedtuple representa los atributos públicos del agente
            'hexagonalPieces', # tupla ordenada de strings ('hp1', 'hp2', ....)
            'numSmallPieces', # Integer
            'redIndicator', # Boolean
            'whiteIndicator', # Integer
        ])
        
        self.PrivateState = namedtuple('PrivateState',[ # namedtuple representa los atributos privados del agente
            'smallPieces',  # tupla ordenada de strings ('sp1', 'sp2', ....)
            'publicState' # namedtuple representa los atributos públicos del agente
        ])
        
        
    def getMove(self, gameState, *args, **kwargs):
        
        return None
    
    
    def gameOver(self, score, *args, **kwargs):
        
        return None
    
    
    def getPublicState(self): 
        """
        Función que aglutina los atributos públicos del agente.
        RETURN:
            namedtuple PublicState
        """
        return self.PublicState(
            hexagonalPieces = tuple(sorted([
                piece.id
                for piece in self.hexagonalPieces
            ])), # tupla ordenada de strings ('hp1', 'hp2', ....)
            numSmallPieces = len(self.smallPieces), # Integer
            redIndicator = self.redIndicator, # Boolean
            whiteIndicator = self.whiteIndicator, # Integer
        )
    
        
    def getPrivateState(self):
        """
        Función que aglutina los atributos privados del agente.
        RETURN:
            namedtuple PrivateState
        """
        return self.PrivateState(
            smallPieces = tuple(sorted([
                'sp'+str(int(piece.id[2:])%12) # Para simplificar, se identifica la ficha con alguna de las 12 diferentes que existen
                for piece in self.smallPieces
            ])), # tupla ordenada de strings ('hp1', 'hp2', ....)
            publicState = self.getPublicState()
        )

    