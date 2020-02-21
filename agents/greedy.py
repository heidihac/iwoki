from player import Player
import gameState

class GreedyPlayer(Player):
    """ 
    Clase para implementar al jugador Greedy. Implementa un algoritmo voraz, que elige la mejor jugada a corto plazo en cada turno.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

        
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Función que juega el turno del agente Greedy. 
        Se recorren las posibles acciones a realizar y se selecciona la que más puntos le aporte.
        Nunca va a optar por robar una ficha pequeña voluntariamente si existe la posibilidad de colocar alguna otra, ya sea pequeña o hexagonal.
        A igualdad de puntos, el método escogerá la opción de colocar una ficha pequeña antes que una hexagonal.
        PARAMETER:
            gameState: estado actual del juego.
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

            