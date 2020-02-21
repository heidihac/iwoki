from player import Player
import gameState

class HumanPlayer(Player):
    """ 
    Clase para implementar al jugador Human.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Qfile = None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Función que implementa una API sencilla para permitir al jugador humano ejecutar su turno.
        PARAMETER:
            gameState: estado actual del juego.
        """
        if not gameState.gameOver:
            actions = gameState.getActions(self)
            while True:  
                print ("\nIndica el número de tu jugada:")
                num = 1
                for action in actions:
                    print ("{} - {}".format(num, action))
                    num += 1
                optionMenu = input()
                if int(optionMenu) > 0 and int(optionMenu) <= num:
                    chosenAction = actions[int(optionMenu)-1]
                    break
                else:
                    print("Opción incorrecta")
                    continue
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            