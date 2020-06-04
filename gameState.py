import numpy as np
import player
from collections import namedtuple
from datetime import datetime

class GameState:
    """ 
    Class that represents the full game state.
    """
    def __init__(self, players, hexagonalTilesAvailable, smallTilesAvailable, hexagonalGaps, smallGaps,
                 fittableHexagonalGaps, fittableSmallGaps):
        self.players = np.array(players) # List of players (agents)
        self.hexagonalTilesAvailable = hexagonalTilesAvailable # Available hexagonal tiles
        self.smallTilesAvailable = smallTilesAvailable # Available small tiles
        self.hexagonalGaps = hexagonalGaps # Hexagonal gaps in the game space
        self.smallGaps = smallGaps # Small gaps in the game space
        self.fittableHexagonalGaps = fittableHexagonalGaps # Hexagonal gaps where a hexagonal tile can be placed
        self.fittableSmallGaps = fittableSmallGaps # Small gaps where a small tile can be placed
        self.initialAction = True # Flag indicating whether this is the first move of the game
        self.turnPassed = 0 # Number of consecutive turns the players have passed. Avoid an infinite loop when none of the players can do any action except pass the turn
        self.gameOver = False # End-of-game flag
        self.endProperly = False # Ending mode indicator
        
        self.State = namedtuple('State',[ # namedtuple representing the state of the world for a player
            # Board
            'fittableHexagonalGaps', # ordered tuple of strings ('hg1', 'hg2', ....)
            'fittableSmallGaps', # ordered tuple of strings ('hg1', 'hg2', ....)
            # Public information of the players
            'opponentsInfo', # Tuple of the states of the opponents
            # Private information of the players
            'playerInfo' # Tuple of the states of the player
        ])
        
        
    def __hash__(self):
        return hash(self.State)
    

    def __eq__(self, other):
        return other.State == self.State

    
    def getAllInitialTiles(self, numSmall=9, numHexagonal=3):
        """ 
        Function that deals all the small and hexagonal tiles to the players at the beginning of the game.
        PARAMETERS:
            numSmall: number of small tiles that are handed out.
            numHexagonal: number of hexagonal tiles that are handed out.
        """
        print("{} small tiles and {} hexagonal tiles are dealt to each player.".format(numSmall, numHexagonal))
        for i in range(len(self.players)):
            self.getSmallTiles(self.players[i], numSmall)
            self.getHexagonalTiles(self.players[i], numHexagonal)

            
    def getActions(self, player):
        """ 
        Function that returns all possible actions to do for the player specified as parameter.
        """
        actions = []
        if self.initialAction: # Initial movement of the game
            # Small tiles on the subtraction side
            for smallTile in player.smallTiles:
                smallTileOrder = [sto for sto in smallTile.orders if sto[3] == '-'][0]
                smallTileOrderSorted = sorted(smallTileOrder[:3], reverse=True)
                score = int(smallTileOrderSorted[0]) - int(smallTileOrderSorted[2])
                actions = actions + [['', smallTile.id, smallTileOrder, 'H1_H4_H5', score]]

            # Small tiles on the sum side
            for smallTile in player.smallTiles:
                smallTileOrder = [sto for sto in smallTile.orders if sto[3] == '+'][0]
                smallTileOrderSorted = sorted(smallTileOrder[:3], reverse=True)
                score = int(smallTileOrderSorted[0]) + int(smallTileOrderSorted[1])
                actions = actions + [['', smallTile.id, smallTileOrder, 'H1_H4_H5', score]]

            # Hexagonal tiles
            for hexagonalTile in player.hexagonalTiles:
                score = max([i for i in hexagonalTile.orders[0] if i != '*'])
                actions = actions + [['', hexagonalTile.id, hexagonalTile.orders[0], 'H1', int(score)]]

        else: # Non-initial movement of the game
            
            # Small tiles on the subtraction side
            for smallTile in player.smallTiles:
                for smallGapF in self.fittableSmallGaps:
                    sgVertices = [vertixSmallGap[2] for vertixSmallGap in self.fittableSmallGaps[smallGapF].vertices]

                    for stOrder in smallTile.orders:
                        if (stOrder[3] == '-'):
                            auxVertices = np.array([], dtype=int)
                            for i in range(3):
                                if i == 0:
                                    auxVertices = np.append(auxVertices, abs(int(stOrder[i]) - int(stOrder[i+2])))
                                else: # i == 1 or i == 2
                                    auxVertices = np.append(auxVertices, abs(int(stOrder[i]) - int(stOrder[i-1])))
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
                                actions = actions + [['', smallTile.id, stOrder, smallGapF, score]]

            # Small tiles on the sum side
            for smallTile in player.smallTiles:
                for smallGapF in self.fittableSmallGaps:
                    sgVertices = [vertixSmallGap[2] for vertixSmallGap in self.fittableSmallGaps[smallGapF].vertices]

                    for stOrder in smallTile.orders:
                        if (stOrder[3] == '+'):
                            auxVertices = np.array([], dtype=int)
                            for i in range(3):
                                if i == 0:
                                    auxVertices = np.append(auxVertices, int(stOrder[i]) + int(stOrder[i+2]))
                                else: # i == 1 or i == 2
                                    auxVertices = np.append(auxVertices, int(stOrder[i]) + int(stOrder[i-1]))
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
                                actions = actions + [['', smallTile.id, stOrder, smallGapF, score]]

            # Hexagonal tiles
            for hexagonalTile in player.hexagonalTiles:
                for hexGapF in self.fittableHexagonalGaps:
                    hgVertices = [vertixHexGap[2] for vertixHexGap in self.fittableHexagonalGaps[hexGapF].vertices]
                    for htOrder in hexagonalTile.orders:
                        score = -1
                        
                        for i in range(6):
                            if str(hgVertices[i]) == str(htOrder[i]) and str(htOrder[i]) != '*':
                                if int(hgVertices[i]) == 0:
                                    score = 0
                                elif score == -1:
                                    score += int(hgVertices[i]) + 1
                                else:
                                    score += int(hgVertices[i])
                            elif (str(hgVertices[i]) != '_' and str(htOrder[i]) != '*'):
                                score = -1
                                break

                        if score > -1:
                            actions = actions + [['', hexagonalTile.id, htOrder, hexGapF, int(score)]]

            # Draw a tile if another tile has not been drawn before in the same turn
            if not player.gotTileBefore and len(self.smallTilesAvailable) > 0:
                actions = actions + [['getSmallTile', None, None, None, 0]]
            if player.gotTileBefore and len(actions) == 0:
                actions = actions + [['passTurn', None, None, None, 0]]
                
            if len(actions) == 0:
                actions = actions + [['passTurn', None, None, None, 0]]

        return actions
    
    
    def getHexagonalTiles(self, player, numTiles=1):
        """ 
        Función que selecciona al azar fichas hexagonales sin reemplazamiento. 
        Es válida tanto para obtener las fichas hexagonales al inicio del juego como para robar una nueva.
        PARAMETERS:
            player: jugador que obtiene las fichas hexagonales.
            numTiles: número de fichas que se obtienen. Por defecto 1. 
        """
        hexagonalTilesSelected = []
        
       # Seed initialization for games with the QLearner agent
#        if numTiles == 1: # The tiles are drawn randomly
#            np.random.seed(int(datetime.now().strftime("%f")))
#        else:  # A seed is set up to deal the tiles at the beginning
#            np.random.seed(20200104)
    
        # Seed initialization for games with the Minimax agent
#        if numTiles == 1: # A seed is set up to draw tiles
#            np.random.seed(20200121)
#        else: # The tiles are initially dealt randomly
#            np.random.seed(int(datetime.now().strftime("%f")))
        
        
        if len(self.hexagonalTilesAvailable) >= numTiles:
            hexagonalTilesSelected = np.random.choice(self.hexagonalTilesAvailable, numTiles, replace=False)
            
            # Assigned hexagonal tiles are removed from the list of those remaining available
            self.hexagonalTilesAvailable = [tile for tile in self.hexagonalTilesAvailable if tile not in hexagonalTilesSelected]
            
            # The new hexagonal tile is added to the player's tile list
            player.hexagonalTiles = np.append(player.hexagonalTiles, hexagonalTilesSelected)
            
            print("[{}]: Draw {} hexagonal ".format(player.name, numTiles), end = '')
            print("tiles.") if numTiles > 1 else print("tile.")
        elif len(self.hexagonalTilesAvailable) == 0:
            print("No hexagonal tiles available.")
        elif len(self.hexagonalTilesAvailable) == 1:
            print("There is only 1 hexagonal tile available.")
        else:
            print("There are only {} hexagonal tiles available.".format(len(self.hexagonalTilesAvailable)))

    
    def getSmallTiles(self, player, numTiles=1):
        """ 
        Function that randomly selects small tiles without replacement.
        It is valid both to get the small tiles at the beginning of the game and to draw a new one.
        PARAMETERS:
            player: player who gets the small chips.
            numTiles: number of tiles obtained. By default 1
        """
        player.gotTileBefore = False
        smallTilesSelected = []

        # Seed initialization for games with the QLearner agent
#        if numTiles == 1: # The tiles are drawn randomly
#            np.random.seed(int(datetime.now().strftime("%f")))
#        else:  # A seed is set up to deal the tiles at the beginning
#            np.random.seed(20200104)
    
        # Seed initialization for games with the Minimax agent
#        if numTiles == 1: # A seed is set up to draw tiles
#            np.random.seed(20200121)
#        else: # The tiles are initially dealt randomly
#            np.random.seed(int(datetime.now().strftime("%f")))

        
        if len(self.smallTilesAvailable) >= numTiles:
            smallTilesSelected = np.random.choice(self.smallTilesAvailable, numTiles, replace=False)
            self.setRedIndicator(player, value=False) # If the red light is active, it deactivates.
            if numTiles == 1:
                print("[{}]: Draw 1 small tile.".format(player.name))
                self.changeWhiteIndicators(player)
                player.gotTileBefore = True
            else:
                print("[{}]: Draw {} small tiles.".format(player.name, numTiles))
            
            # Assigned small tiles are removed from the list of those remaining available
            self.smallTilesAvailable = [tile for tile in self.smallTilesAvailable if tile not in smallTilesSelected]

            # The new small tile is added to the player's tile list
            player.smallTiles = np.append(player.smallTiles, smallTilesSelected)
        
        elif len(self.smallTilesAvailable) == 0:
            print("[{}]: Try to draw a small tile. None available.".format(player.name))
        elif len(self.smallTilesAvailable) == 1:
            print("There is only 1 small tile available.")
        else:
            print("There are only {} small tiles available.".format(len(self.smallTilesAvailable)))

        
    def addScore(self, player, score):
        """
        Function that increases the player's accumulated score with a new value.
        PARAMETERS:
            player.
            score: points to increase.
        """
        player.score += score
        
    
    def changeWhiteIndicators(self, player):
        """ 
        Function that updates the number of white tokens and, in case of reaching three, draws a hexagonal tile.
        PARAMETER:
            player.
        """
        player.whiteIndicators += 1
        if player.whiteIndicators == 1:
            print("[{}]: {} active white tokens.".format(player.name, player.whiteIndicators))
        else:
            if player.whiteIndicators == 3: # A hexagonal tile is drawn
                self.getHexagonalTiles(player)
                player.whiteIndicators = 0
            print("[{}]: {} active white tokens.".format(player.name, player.whiteIndicators))
    

    def setRedIndicator(self, player, value): 
        """
        Function that changes the red token status.
        PARAMETERS:
            player.
            value: new status that the red token is updated to.
        """
        if player.redIndicator or value:
            player.redIndicator = value
            if player.redIndicator:
                print("[{}]: Red token active. Last small tile.".format(player.name))
            else:
                print("[{}]: Red token inactive.".format(player.name))

    
    def fitSmallTile(self, player, tile, order, gap, score):
        """
        Function that places a small tile in one of the free gaps in the game space.
        PARAMETERS:
            player.
            tile: identifier of the small tile to be placed.
            order: list containing the order of the numbers of the small tile to be placed, including the '+' or '-' sign.
            gap: identifier of the gap where the small tile is to be placed.
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
                    if vertixHex[0] == vertixSmall[0] and int(vertixHex[1]) == int(vertixSmall[1]): # The coordinates coincide
                        if vertixHex[2] == '_': # The gap of the hexagonal tile is vacant
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

                        else: # If the gap is already occupied by a hexagonal tile, the points of the vertex are added
                            vertixSmall[3] = 'O'
                            vertixHex[3] = 'O'
            i += 1

        player.smallTiles = [st for st in player.smallTiles if st.id != tile]
        self.addScore(player, score)

        if order[3] == '-': # If the tile is placed on the side of the subtraction a white token is added
            self.changeWhiteIndicators(player)
            
        if len(player.smallTiles) == 1: # Last small tile
            self.setRedIndicator(player, value=True)
            
        
    def fitHexagonalTile(self, player, tile, order, gap, score):
        """ 
        Function that places a hexagonal tile in one of the free gaps of the game space.
        PARAMETERS:
            player.
            tile: identifier of the hexagonal tile to be placed.
            gap: identifier of the gap where the hexagonal tile is to be placed.
            order: list containing the order of the numbers of the hexagonal tile to be placed, including by the '+' or '-' sign.
        """
        i = 0

        for vertixHex in self.hexagonalGaps[gap].vertices:
            vertixHex[2] = order[i]
            for smallGap in self.smallGaps:
                for vertixSmall in self.smallGaps[smallGap].vertices:
                    if vertixSmall[0] == vertixHex[0] and int(vertixSmall[1]) == int(vertixHex[1]): # The coordinates coincide
                        if vertixSmall[2] == '_': # The gap of the small tile is vacant
                            vertixSmall[2] = order[i]
                            self.fittableSmallGaps[smallGap] = self.smallGaps[smallGap]
                            if gap in self.fittableHexagonalGaps:
                                del self.fittableHexagonalGaps[gap]

                        else: # If the gap is already occupied by a small tile, the points of the vertex are added
                            vertixSmall[3] = 'O'
                            vertixHex[3] = 'O'
            i += 1
        
        player.hexagonalTiles = [ht for ht in player.hexagonalTiles if ht.id != tile]
        self.addScore(player, score)
    
    
    def move(self, chosenAction, player):
        """
        Function that executes the action decided by the player (agent).
        PARAMATERS:
            chosenAction.
            player.
        """
        if len(player.smallTiles) == 0 or self.turnPassed == 2: # If the player has run out of small tiles or both players have passed in their turn, the game is over.
            self.printFinalScore()
            self.gameOver = True
            self.changeTurn(player)
        else:
            if chosenAction[0] == "getSmallTile": # The player draws a small tile and plays again
                self.getSmallTiles(player)
                self.turnPassed = 0
            elif chosenAction[0] == "passTurn": # the player passes the turn to the next player
                print("[{}]: Pass the turn".format(player.name))
                self.changeWhiteIndicators(player)
                self.turnPassed += 1
                self.changeTurn(player)
            else:
                if chosenAction[1][:2]=='ht': # The player places a hexagonal tile
                    self.fitHexagonalTile(player, chosenAction[1], chosenAction[2], 
                                                chosenAction[3], chosenAction[4])
                    self.changeTurn(player)
                else: # The player places a small tile
                    self.fitSmallTile(player, chosenAction[1], chosenAction[2], 
                                            chosenAction[3], chosenAction[4])
                    self.changeTurn(player)
                self.turnPassed = 0

                print('[{}]: Places the tile {}, with order {} in the gap {}.'.format(player.name, 
                                                                                     chosenAction[1], 
                                                                                     chosenAction[2], 
                                                                                     chosenAction[3]))
            player.accumulatedScore += chosenAction[4]
            self.initialAction = False

    
    def finalPointTally(self, player):
        """
        Function that performs the final point tally.
        The score the player have accumulated must be subtracted from the highest number on each of the small tiles left.
        PARAMETER:
            player.
        RETURNS:
            score: final score.
            subtraction: points to be subtracted.
        """
        subtraction = 0
        for tile in player.smallTiles:            
            subtraction += max([int(i) for i in tile.orders[0] if i != '-' and i != '+'])
        player.score -= subtraction
        player.accumulatedScore -= subtraction
            
        return player.score, subtraction
    
    
    def printFinalScore(self):
        """
        Function that shows the final result of the game.
        """
        print("\nFinal game scores:\n")
        winners = []
        winnerScore = 0
        maxScore = -1000

        for player in self.players:
            player.score, subtraction = self.finalPointTally(player)
            if player.score > maxScore:
                maxScore = player.score

            print("{}: {} points".format(player.name, player.score), end = '')
            if subtraction != 0:
                print(" ({} points have been subtracted from the accumulated {})".format(subtraction, 
                                                                                         player.score + subtraction))
            else:
                print('\n')

        # It is checked if there has been a draw
        for player in self.players: 
            if player.score == maxScore:
                winners = np.append(winners, player)

   #     CBOLD = '\33[1m'
   #     CEND = '\033[0m'
        CBOLD = ''
        CEND = ''
        if len(winners) > 1:
            print(CBOLD + "There has been a draw. THE WINNERS ARE: \n")
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
            print(CBOLD + "THE WINNER IS: {}".format(winners[0].name) + CEND)
            winners[0].numWins += 1

        print(CEND)
        print("\n-- Game over --")

    
    def summary(self):
        """ 
        Function that shows the summary of the current state of the game. 
        """
        print('-------------------------------------')
        for player in self.players:
            print("\n{}'s score: {}".format(player.name, player.score))
            print("{}'s small tiles: ".format(player.name), end = '')
            for st in player.smallTiles:
                print(str(st.orders[0]) + " ", end = '')
            print("\n{}'s hexagonal tiles: ".format(player.name), end = '')
            for ht in player.hexagonalTiles:
                print(str(ht.orders[0]) + " ", end = '')
            print("\nWhite tokens: " + str(player.whiteIndicators))
            print("Red token: " + str(player.redIndicator))

        print("Number of small tiles available without dealing: " + str(len(self.smallTilesAvailable)))
        print("Number of hexagonal tiles available without dealing: " + str(len(self.hexagonalTilesAvailable)))

        print("Enabled gaps to place any hexagonal tile: ", end = '')
        for fhg in self.fittableHexagonalGaps:
            print(str(fhg) + "  ", end = '')
        print("\nEnabled gaps to place any small tile: ")
        for fsg in self.fittableSmallGaps:
            print(str(fsg) + "  ", end = '')

        print('\n-------------------------------------')
        
    
    def changeTurn(self, player):
        """ 
        Function that changes turns to make way for the next player. 
        """
        for p in self.players:
            if p == player:
                p.isTurn = False
            else:
                p.isTurn = True
            player.gotTileBefore = False


    def getState(self, player):
        """
        Function that obtains information from the game space in a determined state.
        PARAMATER:
            player.
        RETUNR:
            The status is returned transformed by a hash function.
        """
        s = self.State(
            # Board
            fittableHexagonalGaps = tuple(sorted([
                tile
                for tile in self.fittableHexagonalGaps
            ])), # ordered tuple of strings ('hg1', 'hg2', ....)
            fittableSmallGaps =  tuple(sorted([
                tile
                for tile in self.fittableSmallGaps
            ])), # ordered tuple of strings ('h1_h2_h3', 'h1_h3_h4', ....)
            
            # Public information of the players
            opponentsInfo = tuple([ # Tupla del los estados de los oponentes
                p.getPublicState()
                for p in self.players
                if p != player
            ]),
            # Private information of the players
            playerInfo = player.getPrivateState()
        )
        return s.__hash__()
        
        