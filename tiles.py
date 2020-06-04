import numpy as np
from utils import listToString

class HexagonalTile:
    """ 
    Class that represents the hexagonal tiles.
    At each vertex there is a number from 1 to 6 or a wildcard (represented by the character '*'). They are the same values on both sides, so the order presented on one side will be the opposite on the other.
    All 12 possible variants of each hexagonal tile are taken into account, according to the orders they can present (6 for each side).
        
        Example: 
            The representation of the tile [2, 4, 3, 6, 5, *] has these 12 different positions:
            
            [2, 4, 3, 6, 5, *]
            [4, 3, 6, 5, *, 2]
            [3, 6, 5, *, 2, 4]
            [6, 5, *, 2, 4, 3]
            [5, *, 2, 4, 3, 6]
            [*, 2, 4, 3, 6, 5]
            [*, 5, 6, 3, 4, 2]
            [2, *, 5, 6, 3, 4]
            [4, 2, *, 5, 6, 3]
            [3, 4, 2, *, 5, 6]
            [6, 3, 4, 2, *, 5]
            [5, 6, 3, 4, 2, *]

    """    
    def __init__(self, name, numbers):
        self.id = name
        
        # Different orders of a hexagonal tile on one side:
        order1 = numbers[1:] + [numbers[0]]
        order2 = order1[1:] + [order1[0]]
        order3 = order2[1:] + [order2[0]]
        order4 = order3[1:] + [order3[0]]
        order5 = order4[1:] + [order4[0]]
        
        # Different orders of a hexagonal tile on the other side:
        numbers_inv = numbers[::-1]
        order1_inv = order1[::-1]
        order2_inv = order2[::-1]
        order3_inv = order3[::-1]
        order4_inv = order4[::-1]
        order5_inv = order5[::-1]
        
        # self.orders contains the different orders the numbers on the hexagonal tile can have, taking into account both sides
        self.orders = np.array([listToString(numbers), listToString(order1), listToString(order2),
                                listToString(order3), listToString(order4), listToString(order5),
                                listToString(numbers_inv), listToString(order1_inv),  listToString(order2_inv),
                                listToString(order3_inv),  listToString(order4_inv),  listToString(order5_inv,)])
                                                        

class SmallTile:
    """ 
    Class that represents the small tiles.
    In each of the 3 inner corners there is a number from 1 to 4. Each side of the tile has the same 3 numbers and in the same order. The addition (+) is represented on one side and the subtraction (-) on the other.
    All the 6 possible variants of each small tile are taken into account, according to the orders that it can present (3 for each side).
        
        Example: 
            The representation of the tile [1, 2, 4] tiene estas 6 has these 6 different possibilities:
            
            [1, 2, 4, +]
            [2, 4, 1, +]
            [4, 1, 2, +]
            [1, 4, 2, -]
            [2, 1, 4, -]
            [4, 2, 1, -]
        
    """
    def __init__(self, name, numbers):
        self.id = name

        order1 = [numbers[0], numbers[1], numbers[2], '+']
        order2 = [numbers[1], numbers[2], numbers[0], '+']
        order3 = [numbers[2], numbers[0], numbers[1], '+']
        order4 = [numbers[0], numbers[2], numbers[1], '-']
        order5 = [numbers[1], numbers[0], numbers[2], '-']
        order6 = [numbers[2], numbers[1], numbers[0], '-']
        
        # self.orders contains the possible variants the numbers on the small tile may have, with the '+' and '-' signs on each of the faces
        self.orders = np.array([listToString(order1), listToString(order2), listToString(order3),
                                listToString(order4), listToString(order5), listToString(order6)])

        