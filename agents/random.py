from player import Player
import gameState
import random

class RandomPlayer(Player):
    """ 
    Clase para implementar al jugador Random.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Función que juega el turno del agente Random. Elige de forma aleatoria la acción a ejecutar.
        PARAMETER:
            gameState: estado actual del juego.
        """
        if not gameState.gameOver:
            actions = gameState.getActions(self)
            chosenAction = random.choice(actions)
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            