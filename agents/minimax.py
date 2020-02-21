from player import Player
import gameState
from copy import deepcopy
import time

class MinimaxPlayer(Player):
    """ 
    Clase para implementar al jugador Minimax, con con poda alfa-beta y suspensión en profundidad y en tiempo.
    """
    
    INFINITE = 10000
    DEPTH = 3

    def __init__(self, name):
        super().__init__(name)
        self.maxTime = 90000 # milisegundos. Tiempo máximo de exploración de cada una de las ramas que cuelgan del nodo raíz
        self.numNodes = 0 # Dato para la obtención de métricas.
        self.startTime = None # Establece el valor de tiempo inicial para determinar el momento en que se 
                              # sobrepasa el límite de búsqueda en una rama principal del nodo raíz
        self.Qfile = None
        
        if self.gotPieceBefore:
            self.bestAction = [['passTurn', None, None, None, 0]]
        else:
            self.bestAction = ['getSmallPiece', None, None, None, 0]
        
        
    def generateChildNode(self, gameState, action, playerType):
        """ 
        Genera un clon del gameState y se ejecuta la acción sobre él. 
        PARAMETERS:
            gameState: estado actual del juego que se va a clonar.
            action: acción que se va a ejecutar sobre el nuevo clon del gameState.
            playerType: MAX --> Minimax
                        min --> oponente
        RETURN:
            newGameState: estado del juego resultante.
        """

        newGameState = deepcopy(gameState) # Se clona el gameState 
        if playerType == 'MAX':
            player = [p for p in newGameState.players if p.name == 'Minimax'][0]
        else:
            player = [p for p in newGameState.players if p.name != 'Minimax'][0]
            
        newGameState.move(action, player) # Se ejecuta la acción sobre newGameState
        self.numNodes += 1

        return newGameState
                
    
    def alpha_beta(self, gameState, depth=DEPTH, alpha=-INFINITE, beta=INFINITE, playerType='MAX'):
        """ 
        Función que explora de forma recursiva el árbol MINIMAX con poda ALFA-BETA.
        PARAMETERS:
            gameState: estado actual del juego.
            depth: profundidad de exploración. Por defecto DEPTH.
            alpha, beta: valores a actualizar en cada nodo. Por defecto -INFINITE y INFINITE, respectivamente.
            playerType: MAX --> Minimax
                        min --> oponente
        RETURN:
            alfa/beta: valor actualizado para el nodo actual.
            bestAction: acción seleccionada.
        """
        if depth == self.DEPTH:
            self.startTime = time.time()
        minimaxPlayer = [p for p in gameState.players if p.name == 'Minimax'][0]
        otherPlayer = [p for p in gameState.players if p.name != 'Minimax'][0]

        if gameState.gameOver or depth == 0: # Nodo terminal alcanzado por fin de partida o por límite de profundidad. El valor que devuelve es la diferencia de puntos entre el jugador y su oponente tras el recuento final de ambos
            return gameState.finalPointCount(minimaxPlayer)[0] - gameState.finalPointCount(otherPlayer)[0], None
        
        if time.time() > self.startTime + self.maxTime/1000: # Nodo terminal alcanzado por límite de tiempo. Devuelve la acción que mejor perspectivas tiene de las exploradas hasta el momento
            return alpha, self.bestAction

        if playerType == 'MAX':
            # Se expande el árbol a un nuevo nivel de profundidad. Por cada acción posible del gameState se genera un nodo hijo.
            for action in gameState.getActions(minimaxPlayer):
                newGameState = self.generateChildNode(gameState, action, playerType)
                alpha_prev = alpha
                
                if len(otherPlayer.smallPieces) == 0:
                    newGameState.gameOver = True
                    
                alpha = max(alpha, self.alpha_beta(newGameState, depth-1, alpha, beta, 'min')[0])
                if alpha > alpha_prev and depth == self.DEPTH:
                    self.bestAction = action
                if alpha >= beta:
                    return alpha, self.bestAction # Se poda el árbol a partir de esta rama

            return alpha, self.bestAction
        
        else: # min
             # Se expande el árbol a un nuevo nivel de profundidad. Por cada acción posible del gameState se genera un nodo hijo.
            for action in gameState.getActions(otherPlayer):
                newGameState = self.generateChildNode(gameState, action, playerType)
                
                if len(minimaxPlayer.smallPieces) == 0:
                    newGameState.gameOver = True

                beta = min(beta, self.alpha_beta(newGameState, depth-1, alpha, beta, 'MAX')[0])
                if alpha >= beta:
                    return beta, None # Se poda el árbol a partir de esta rama
                
            return beta, None

    
    def getMove(self, gameState, *args, **kwargs):
        """ 
        Función que juega el turno del agente Minimax. Inicia la exploración del árbol MINIMAX para seleccionar la mejora acción y la ejecuta.
        PARAMETER:
            gameState: estado actual del juego.
        """
        if not gameState.gameOver:
            chosenAction = self.alpha_beta(gameState)[1]
            gameState.move(chosenAction, self)
        else:
            gameState.changeTurn(self)

            