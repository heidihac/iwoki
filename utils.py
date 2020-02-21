import numpy as np

def drawPlayersOrder(players):
    """
    Función que establece al azar el orden de intervención de los jugadores. 
    PARAMETERS:
        players: lista de jugadores.
    RETURN:
        players: lista de jugadores con nuevo orden establecido.
    """
    np.random.shuffle(players)
    print("Por sorteo, el orden de los jugadores es: ", end = '')
    i = 1
    for player in players:
        player.isTurn = False
        if i == 1:
            player.isTurn = True
            print(player.name, end = '')
        elif i == len(players):
            print(" y " + str(player.name))
        else:
            print(", " + str(player.name), end = '' )
        i += 1
    
    return players


def listToString(s):
    """ 
    Función que convierte una lista a string. 
    PARAMETERS:
        s: lista.
    RETURN:
        str1: string.
    """
    str1 = ""    
    for element in s:  
        str1 += element   
  
    return str1  

