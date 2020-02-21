import numpy as np
import player
from collections import namedtuple
from datetime import datetime

class GameState:
    """ 
    Clase que representa el estado de juego al completo.
    """
    def __init__(self, players, hexagonalPiecesAvailable, smallPiecesAvailable, hexagonalGaps, smallGaps,
                 fittableHexagonalGaps, fittableSmallGaps):
        self.players = np.array(players) # lista de jugadores (agentes)
        self.hexagonalPiecesAvailable = hexagonalPiecesAvailable # fichas hexagonales disponibles
        self.smallPiecesAvailable = smallPiecesAvailable # fichas pequeñas disponibles
        self.hexagonalGaps = hexagonalGaps # huecos hexagonales del espacio de juego
        self.smallGaps = smallGaps # huecos pequeños del espacio de juego
        self.fittableHexagonalGaps = fittableHexagonalGaps # huecos hexagonales en los que se puede colocar alguna ficha hexagonal
        self.fittableSmallGaps = fittableSmallGaps # huecos pequeños en los que se puede colocar alguna ficha pequeña
        self.initialAction = True # indica si es el primer movimiento de la partida
        self.turnPassed = 0 # número de turnos consecutivos que los jugdores han pasado. Evita un blucle infinito cuando ninguno de los jugadores puede hacer otra acción que no sea pasar el turno
        self.gameOver = False # indicador de fin de la partida
        self.endProperly = False # indicador del modo de finalización de la partida
        
        self.State = namedtuple('State',[ # namedtuple representa el estado del mundo para un jugador
            # Tablero
            'fittableHexagonalGaps', # tupla ordenada de strings ('hg1', 'hg2', ....)
            'fittableSmallGaps', # tupla ordenada de strings ('hg1', 'hg2', ....)
            # Informnación pública de los jugadores
            'opponentsInfo', # Tupla del los estados de los oponentes
            # Informnación privada del jugador
            'playerInfo'#, # Tupla del los estados del jugador
        ])
        
        
    def __hash__(self):
        return hash(self.State)
    

    def __eq__(self, other):
        return other.State == self.State

    
    def getAllInitialPieces(self, numSmall=9, numHexagonal=3):
        """ 
        Función que reparte al inicio de la partida todas las fichas pequeñas y hexagonales a los jugadores.
        PARAMETERS:
            numSmall: número de fichas pequeñas que se reparten.
            numHexagonal: número de fichas hexagonales que se reparten.
        """
        print("Se reparten {} fichas pequeñas y {} fichas hexagonales a cada jugador.".format(numSmall, numHexagonal))
        for i in range(len(self.players)):
            self.getSmallPieces(self.players[i], numSmall)
            self.getHexagonalPieces(self.players[i], numHexagonal)

            
    def getActions(self, player):
        """ 
        Función que devuelve todas las posibles acciones a realizar para el jugador especificado como parámetro.
        """
        actions = []
        if self.initialAction: # Movimiento inicial de la partida
            # Fichas pequeñas por el lado de la resta
            for smallPiece in player.smallPieces:
                smallPieceOrder = [spo for spo in smallPiece.orders if spo[3] == '-'][0]
                smallPieceOrderSorted = sorted(smallPieceOrder[:3], reverse=True)
                score = int(smallPieceOrderSorted[0]) - int(smallPieceOrderSorted[2])
                actions = actions + [['', smallPiece.id, smallPieceOrder, 'H1_H4_H5', score]]

            # Fichas pequeñas por el lado de la suma
            for smallPiece in player.smallPieces:
                smallPieceOrder = [spo for spo in smallPiece.orders if spo[3] == '+'][0]
                smallPieceOrderSorted = sorted(smallPieceOrder[:3], reverse=True)
                score = int(smallPieceOrderSorted[0]) + int(smallPieceOrderSorted[1])
                actions = actions + [['', smallPiece.id, smallPieceOrder, 'H1_H4_H5', score]]

            # Fichas hexagonales
            for hexagonalPiece in player.hexagonalPieces:
                score = max([i for i in hexagonalPiece.orders[0] if i != '*'])
                actions = actions + [['', hexagonalPiece.id, hexagonalPiece.orders[0], 'H1', int(score)]]

        else: # Movimiento no incial de la partida
            
            # Fichas pequeñas por el lado de la resta
            for smallPiece in player.smallPieces:
                for smallGapF in self.fittableSmallGaps:
                    sgVertices = [vertixSmallGap[2] for vertixSmallGap in self.fittableSmallGaps[smallGapF].vertices]

                    for spOrder in smallPiece.orders:
                        if (spOrder[3] == '-'):
                            auxVertices = np.array([], dtype=int)
                            for i in range(3):
                                if i == 0:
                                    auxVertices = np.append(auxVertices, abs(int(spOrder[i]) - int(spOrder[i+2])))
                                else: # i == 1 or i == 2
                                    auxVertices = np.append(auxVertices, abs(int(spOrder[i]) - int(spOrder[i-1])))
                                i += 1
                            score = -1

                            for i in range(3):
                                if str(sgVertices[i]) == str(auxVertices[i]):
                                    if int(sgVertices[i]) == 0:
                                        score = 0
                                    elif score == -1:
                                        score += int(sgVertices[i]) + 1
                                    else:
                                        score += int(sgVertices[i])
                                elif str(sgVertices[i]) != '_' and str(sgVertices[i]) != '*':
                                    score = -1
                                    break

                            if score > -1:
                                actions = actions + [['', smallPiece.id, spOrder, smallGapF, score]]

            # Fichas pequeñas por el lado de la suma
            for smallPiece in player.smallPieces:
                for smallGapF in self.fittableSmallGaps:
                    sgVertices = [vertixSmallGap[2] for vertixSmallGap in self.fittableSmallGaps[smallGapF].vertices]

                    for spOrder in smallPiece.orders:
                        if (spOrder[3] == '+'):
                            auxVertices = np.array([], dtype=int)
                            for i in range(3):
                                if i == 0:
                                    auxVertices = np.append(auxVertices, int(spOrder[i]) + int(spOrder[i+2]))
                                else: # i == 1 or i == 2
                                    auxVertices = np.append(auxVertices, int(spOrder[i]) + int(spOrder[i-1]))
                                i += 1
                            score = -1

                            for i in range(3):
                                if str(sgVertices[i]) == str(auxVertices[i]):
                                    if int(sgVertices[i]) == 0:
                                        score = 0
                                    elif score == -1:
                                        score += int(sgVertices[i]) + 1
                                    else:
                                        score += int(sgVertices[i])
                                elif str(sgVertices[i]) != '_' and str(sgVertices[i]) != '*':
                                    score = -1
                                    break

                            if score > -1:
                                actions = actions + [['', smallPiece.id, spOrder, smallGapF, score]]

            # Fichas hexagonales
            for hexagonalPiece in player.hexagonalPieces:
                for hexGapF in self.fittableHexagonalGaps:
                    hgVertices = [vertixHexGap[2] for vertixHexGap in self.fittableHexagonalGaps[hexGapF].vertices]
                    for hpOrder in hexagonalPiece.orders:
                        score = -1
                        
                        for i in range(6):
                            if str(hgVertices[i]) == str(hpOrder[i]) and str(hpOrder[i]) != '*':
                                if int(hgVertices[i]) == 0:
                                    score = 0
                                elif score == -1:
                                    score += int(hgVertices[i]) + 1
                                else:
                                    score += int(hgVertices[i])
                            elif (str(hgVertices[i]) != '_' and str(hpOrder[i]) != '*'):
                                score = -1
                                break

                        if score > -1:
                            actions = actions + [['', hexagonalPiece.id, hpOrder, hexGapF, int(score)]]

            # Robar una ficha si no se ha robado otra antes en el mismo turno
            if not player.gotPieceBefore and len(self.smallPiecesAvailable) > 0:
                actions = actions + [['getSmallPiece', None, None, None, 0]]
            if player.gotPieceBefore and len(actions) == 0:
                actions = actions + [['passTurn', None, None, None, 0]]
                
            if len(actions) == 0:
                actions = actions + [['passTurn', None, None, None, 0]]

        return actions
    
    
    def getHexagonalPieces(self, player, numPieces=1):
        """ 
        Función que selecciona al azar fichas hexagonales sin reemplazamiento. 
        Es válida tanto para obtener las fichas hexagonales al inicio del juego como para robar una nueva.
        PARAMETERS:
            player: jugador que obtiene las fichas hexagonales.
            numPieces: número de fichas que se obtienen. Por defecto 1. 
        """
        hexagonalPiecesSelected = []
        
       # Inicialización de la semilla para partidas con el agente QLearner
#        if numPieces == 1: # Las fichas se roban aleatoriamente
#            np.random.seed(int(datetime.now().strftime("%f")))
#        else:  # Se establece una semilla para repartir inicialmente
#            np.random.seed(20200104)
    
        # Inicialización de la semilla para partidas con el agente Minimax
#        if numPieces == 1: # Se establece una semilla para robar fichas
#            np.random.seed(20200121)
#        else: # Se reparte inicialmente de forma aleatoria
#            np.random.seed(int(datetime.now().strftime("%f")))
        
        
        if len(self.hexagonalPiecesAvailable) >= numPieces:
            hexagonalPiecesSelected = np.random.choice(self.hexagonalPiecesAvailable, numPieces, replace=False)
            
            # Se eliminan las fichas hexagonales asignadas de la lista de las que quedan disponibles
            self.hexagonalPiecesAvailable = [piece for piece in self.hexagonalPiecesAvailable if piece not in hexagonalPiecesSelected]
            
            # Se incluye la nueva ficha hexagonal en la lista de las fichas del jugador
            player.hexagonalPieces = np.append(player.hexagonalPieces, hexagonalPiecesSelected)
            
            print("[{}]: Roba {} ".format(player.name, numPieces), end = '')
            print("fichas hexagonales.") if numPieces > 1 else print("ficha hexagonal.")
        elif len(self.hexagonalPiecesAvailable) == 0:
            print("No existen fichas hexagonales disponibles.")
        elif len(self.hexagonalPiecesAvailable) == 1:
            print("Solamente existe 1 ficha hexagonal disponible.")
        else:
            print("Solamente existen {} fichas hexagonales disponibles.".format(len(self.hexagonalPiecesAvailable)))

    
    def getSmallPieces(self, player, numPieces=1):
        """ 
        Función que selecciona al azar fichas pequeñas sin reemplazamiento. 
        Es válida tanto para obtener las fichas pequeñas al inicio del juego como para robar una nueva.
        PARAMETERS:
            player: jugador que obtiene las fichas pequeñas.
            numPieces: número de fichas que se obtienen. Por defecto 1.
        """
        player.gotPieceBefore = False
        smallPiecesSelected = []

        # Inicialización de la semilla para partidas con el agente QLearner
#        if numPieces == 1: # Las fichas se roban aleatoriamente
#            np.random.seed(int(datetime.now().strftime("%f")))
#        else:  # Se establece una semilla para repartir inicialmente
#            np.random.seed(20200104)
    
        # Inicialización de la semilla para partidas con el agente Minimax
#        if numPieces == 1: # Se establece una semilla para robar fichas
#            np.random.seed(20200121)
#        else: # Se reparte inicialmente de forma aleatoria
#            np.random.seed(int(datetime.now().strftime("%f")))

        
        if len(self.smallPiecesAvailable) >= numPieces:
            smallPiecesSelected = np.random.choice(self.smallPiecesAvailable, numPieces, replace=False)
            self.setRedIndicator(player, value=False) # Si estuviera activo el testigo rojo se desactiva
            if numPieces == 1:
                print("[{}]: Roba 1 ficha pequeña.".format(player.name))
                self.changeWhiteIndicator(player)
                player.gotPieceBefore = True
            else:
                print("[{}]: Roba {} fichas pequeñas.".format(player.name, numPieces))
            
            # Se eliminan las fichas pequeñas asignadas de la lista de las que quedan disponibles
            self.smallPiecesAvailable = [piece for piece in self.smallPiecesAvailable if piece not in smallPiecesSelected]

            # Se incluye la nueva ficha pequeña en la lista de las fichas del jugador
            player.smallPieces = np.append(player.smallPieces, smallPiecesSelected)
        
        elif len(self.smallPiecesAvailable) == 0:
            print("[{}]: Intenta robar una ficha pequeña. No hay ninguna disponible.".format(player.name))
        elif len(self.smallPiecesAvailable) == 1:
            print("Solamente existe 1 ficha pequeña disponible.")
        else:
            print("Solamente existen {} fichas pequeñas disponibles.".format(len(self.smallPiecesAvailable)))

        
    def addScore(self, player, score):
        """
        Función que incrementa la puntuación acumulada del jugador con un nuevo valor.
        PARAMETERS:
            player: jugador.
            score: número de puntos que se incrementan.
        """
        player.score += score
        
    
    def changeWhiteIndicator(self, player):
        """ 
        Función que actualiza el número de testigos blancos y, en caso de llegar a tres, roba una ficha hexagonal.
        PARAMETER:
            player: jugador.
        """
        player.whiteIndicator += 1
        if player.whiteIndicator == 1:
            print("[{}]: {} testigo blanco activo.".format(player.name, player.whiteIndicator))
        else:
            if player.whiteIndicator == 3: # Se roba una ficha hexagonal
                self.getHexagonalPieces(player)
                player.whiteIndicator = 0
            print("[{}]: {} testigos blancos activos.".format(player.name, player.whiteIndicator))
    

    def setRedIndicator(self, player, value): 
        """
        Función que modifica el estado del testigo rojo.
        PARAMETERS:
            player: jugador.
            value: nuevo estado al que se actualiza el testigo rojo.
        """
        if player.redIndicator or value:
            player.redIndicator = value
            if player.redIndicator:
                print("[{}]: Testigo rojo activo. Última ficha pequeña.".format(player.name))
            else:
                print("[{}]: Testigo rojo desactivado.".format(player.name))

    
    def fitSmallPiece(self, player, piece, order, gap, score):
        """
        Función que coloca una ficha pequeña en uno de los huecos libres del espacio de juego.
        PARAMETERS:
            player: jugador.
            piece: identificador de la ficha pequeña que se va a colocar.
            order: lista que contiene el orden de los números de la ficha pequeña que se va a colocar, junto con el signo '+' o '-'.
            gap: identificador del hueco donde se va a colocar la ficha pequeña.
        """
        i = 0

        for vertixSmall in self.smallGaps[gap].vertices:
            if order[3] == '+':
                if i == 0:
                    vertixSmall[2] = int(order[i]) + int(order[i+2])
                else:
                    vertixSmall[2] = int(order[i]) + int(order[i-1])
            if order[3] == '-':
                if i == 0:
                    vertixSmall[2] = abs(int(order[i]) - int(order[i+2]))
                else:
                    vertixSmall[2] = abs(int(order[i]) - int(order[i-1]))

            for hexagonalGap in self.hexagonalGaps:
                for vertixHex in self.hexagonalGaps[hexagonalGap].vertices:
                    if vertixHex[0] == vertixSmall[0] and int(vertixHex[1]) == int(vertixSmall[1]): # Coinciden las coordenadas
                        if vertixHex[2] == '_': # El hueco de la ficha hexagonal está sin ocupar
                            if order[3] == '+':
                                if i == 0:
                                    vertixHex[2] = int(order[i]) + int(order[i+2])
                                else:
                                    vertixHex[2] = int(order[i]) + int(order[i-1])
                            if order[3] == '-':
                                if i == 0:
                                    vertixHex[2] = abs(int(order[i]) - int(order[i+2]))
                                else:
                                    vertixHex[2] = abs(int(order[i]) - int(order[i-1]))

                            self.fittableHexagonalGaps[hexagonalGap] = self.hexagonalGaps[hexagonalGap]
                            if gap in self.fittableSmallGaps:
                                del self.fittableSmallGaps[gap]

                        else: # Si el hueco ya está ocupado por una ficha hexagonal se suman los puntos del vértice
                            vertixSmall[3] = 'O'
                            vertixHex[3] = 'O'
            i += 1

        player.smallPieces = [sp for sp in player.smallPieces if sp.id != piece]
        self.addScore(player, score)

        if order[3] == '-': # Si se pone la ficha por el lado de la resta se añade un testigo blanco
            self.changeWhiteIndicator(player)
            
        if len(player.smallPieces) == 1: # Última ficha pequeña
            self.setRedIndicator(player, value=True)
            
        
    def fitHexagonalPiece(self, player, piece, order, gap, score):
        """ 
        Función que coloca una ficha hexagonal en uno de los huecos libres del espacio de juego.
        PARAMETERS:
            player: jugador.
            piece: identificador de la ficha hexagonal que se va a colocar.
            gap: identificador del hueco donde se va a colocar la ficha hexagonal.
            order: lista que contiene el orden de los números de la ficha hexagonal que se va a colocar, incluyendo el comodín ('*').
        """
        i = 0

        for vertixHex in self.hexagonalGaps[gap].vertices:
            vertixHex[2] = order[i]
            for smallGap in self.smallGaps:
                for vertixSmall in self.smallGaps[smallGap].vertices:
                    if vertixSmall[0] == vertixHex[0] and int(vertixSmall[1]) == int(vertixHex[1]): # Coinciden las coordenadas
                        if vertixSmall[2] == '_': # El hueco de la ficha pequeña está sin ocupar
                            vertixSmall[2] = order[i]
                            self.fittableSmallGaps[smallGap] = self.smallGaps[smallGap]
                            if gap in self.fittableHexagonalGaps:
                                del self.fittableHexagonalGaps[gap]

                        else: # Si el hueco ya está ocupado por una ficha pequeña, se suman los puntos del vértice
                            vertixSmall[3] = 'O'
                            vertixHex[3] = 'O'
            i += 1
        
        player.hexagonalPieces = [hp for hp in player.hexagonalPieces if hp.id != piece]
        self.addScore(player, score)
    
    
    def move(self, chosenAction, player):
        """
        Función que ejecuta la acción que decide el jugador (agente).
        PARAMATERS:
            chosenAction: acción elegida.
            player: jugador
        """
        if len(player.smallPieces) == 0 or self.turnPassed == 2: # Si el jugador se ha quedado sin fichas pequeñas o ambos jugadores han pasado en su turno, termina la partida
            self.printFinalScore()
            self.gameOver = True
            self.changeTurn(player)
        else:
            if chosenAction[0] == "getSmallPiece": # El jugador roba una ficha pequeña y juega de nuevo
                self.getSmallPieces(player)
                self.turnPassed = 0
            elif chosenAction[0] == "passTurn": # Pasa el turno al siguiente jugador
                print("[{}]: Pasa el turno".format(player.name))
                self.changeWhiteIndicator(player)
                self.turnPassed += 1
                self.changeTurn(player)
            else:
                if chosenAction[1][:2]=='hp': # El jugador coloca una ficha hexagonal
                    self.fitHexagonalPiece(player, chosenAction[1], chosenAction[2], 
                                                chosenAction[3], chosenAction[4])
                    self.changeTurn(player)
                else: # El jugador coloca una ficha pequeña
                    self.fitSmallPiece(player, chosenAction[1], chosenAction[2], 
                                            chosenAction[3], chosenAction[4])
                    self.changeTurn(player)
                self.turnPassed = 0

                print('[{}]: Coloca la ficha {}, con orden {} en el hueco {}.'.format(player.name, 
                                                                                     chosenAction[1], 
                                                                                     chosenAction[2], 
                                                                                     chosenAction[3]))
            player.accumulatedScore += chosenAction[4]
            self.initialAction = False

    
    def finalPointCount(self, player):
        """
        Función que realiza el recuento final de puntos.
        A la cantidad de puntos que el jugador ha ido acumulando se le resta la suma de los números más altos de cada una de las fichas pequeñas que le hayan quedado sin colocar.
        PARAMETER:
            player: jugador.
        RETURNS:
            score: puntuación definitiva.
            subtraction: puntos que se le resta a la puntuación que tenía antes del recuento final.
        """
        subtraction = 0
        for piece in player.smallPieces:            
            subtraction += max([int(i) for i in piece.orders[0] if i != '-' and i != '+'])
        player.score -= subtraction
        player.accumulatedScore -= subtraction
            
        return player.score, subtraction
    
    
    def printFinalScore(self):
        """
        Función que presenta el resultado final de la partida.
        """
        print("\nPuntuaciones finales de la partida:\n")
        winners = []
        winnerScore = 0
        maxScore = -1000

        for player in self.players:
            player.score, subtraction = self.finalPointCount(player)
            if player.score > maxScore:
                maxScore = player.score

            print("{}: {} puntos".format(player.name, player.score), end = '')
            if subtraction != 0:
                print(" (se le han restado {} puntos a los {} que tenía acumulados)".format(subtraction, 
                                                                                             player.score + subtraction))
            else:
                print('\n')

        # Se comprueba si ha habido empate:
        for player in self.players: 
            if player.score == maxScore:
                winners = np.append(winners, player)

   #     CBOLD = '\33[1m'
   #     CEND = '\033[0m'
        CBOLD = ''
        CEND = ''
        if len(winners) > 1:
            print(CBOLD + "Ha habido empate. LOS GANADORES SON: \n")
            i = 1
            for winner in winners:
                if i == 1:
                    print(winner.name, end = '')
                elif len(winners) == i:
                    print(" y " + str(winner.name))
                else:
                    print(", " + str(winner.name), end = '')
                i += 1
        else:
            print(CBOLD + "GANADOR:  {}".format(winners[0].name) + CEND)
            winners[0].numWins += 1

        print(CEND)
        print("\n-- Fin de la partida --")

    
    def summary(self):
        """ 
        Función que muestra el resumen del estado actual del juego. 
        """
        print('-------------------------------------')
        for player in self.players:
            print("\nPuntuación de {}: {}".format(player.name, player.score))
            print("Fichas pequeñas de {}: ".format(player.name), end = '')
            for sp in player.smallPieces:
                print(str(sp.orders[0]) + " ", end = '')
            print("\nFichas hexagonales de {}: ".format(player.name), end = '')
            for hp in player.hexagonalPieces:
                print(str(hp.orders[0]) + " ", end = '')
            print("\nTestigos blancos: " + str(player.whiteIndicator))
            print("Testigo rojo: " + str(player.redIndicator))

        print("Número de fichas pequeñas disponibles sin repartir: " + str(len(self.smallPiecesAvailable)))
        print("Número de fichas hexagonales disponibles sin repartir: " + str(len(self.hexagonalPiecesAvailable)))

        print("Huecos habilitados para poder colocar alguna ficha hexagonal: ", end = '')
        for fhg in self.fittableHexagonalGaps:
            print(str(fhg) + "  ", end = '')
        print("\nHuecos habilitados para poder colocar alguna ficha pequeña: ")
        for fsg in self.fittableSmallGaps:
            print(str(fsg) + "  ", end = '')

        print('\n-------------------------------------')
        
    
    def changeTurn(self, player):
        """ 
        Función que cambia de turno para dar paso al siguiente jugador. 
        """
        for p in self.players:
            if p == player:
                p.isTurn = False
            else:
                p.isTurn = True
            player.gotPieceBefore = False


    def getState(self, player):
        """
        Función que obtiene información del espacio de juego en un estado determinado.
        PARAMATER:
            player: jugador.
        RETUNR:
            El estado se devuelve transformado por una función hash.
        """
        s = self.State(
            # Tablero
            fittableHexagonalGaps = tuple(sorted([
                piece
                for piece in self.fittableHexagonalGaps
            ])), # tupla ordenada de strings ('hg1', 'hg2', ....)
            fittableSmallGaps =  tuple(sorted([
                piece
                for piece in self.fittableSmallGaps
            ])), # tupla ordenada de strings ('h1_h2_h3', 'h1_h3_h4', ....)
            
            # Informnación pública de los oponentes
            opponentsInfo = tuple([ # Tupla del los estados de los oponentes
                p.getPublicState()
                for p in self.players
                if p != player
            ]),
            # Informnación privada del jugador
            playerInfo = player.getPrivateState()#,
        )
        return s.__hash__()
        
        