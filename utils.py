import numpy as np

def drawPlayersOrder(players):
    """
    Function that randomly sets the order of the players' turns. 
    PARAMETERS:
        players: players list.
    RETURN:
        players: list of players with new established order.
    """
    np.random.shuffle(players)
    print("By random drawing, the order of the players is: ", end = '')
    i = 1
    for player in players:
        player.isTurn = False
        if i == 1:
            player.isTurn = True
            print(player.name, end = '')
        elif i == len(players):
            print(" and " + str(player.name))
        else:
            print(", " + str(player.name), end = '' )
        i += 1
    
    return players


def listToString(s):
    """ 
    Function that converts a list to a string. 
    PARAMETERS:
        s: list.
    RETURN:
        str1: string.
    """
    str1 = ""    
    for element in s:  
        str1 += element   
  
    return str1  

