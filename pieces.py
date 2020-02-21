import numpy as np
from utils import listToString

class HexagonalPiece:
    """ 
    Clase que representa las fichas hexagonales.
    En cada vértice hay un número del 1 al 6 o un comodín (representado por el carácter '*'). Son los mismos valores por ambas caras, por lo que el orden presentado en una cara será el inverso en la otra.
    Se tiene en cuenta todas las 12 posibles variantes de cada ficha hexagonal, según los órdenes que puede presentar (6 por cada una de las caras).
        
        Ejemplo: 
            La representación de la ficha [2, 4, 3, 6, 5, *] tiene estas 12 posiciones distintas:
            
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
        
        # Se tienen en cuenta los distintos órdenes de una ficha hexagonal por una cara:
        order1 = numbers[1:] + [numbers[0]]
        order2 = order1[1:] + [order1[0]]
        order3 = order2[1:] + [order2[0]]
        order4 = order3[1:] + [order3[0]]
        order5 = order4[1:] + [order4[0]]
        
        # Se tienen en cuenta también los diferentes órdenes de una ficha hexagonal por la otra cara:
        numbers_inv = numbers[::-1]
        order1_inv = order1[::-1]
        order2_inv = order2[::-1]
        order3_inv = order3[::-1]
        order4_inv = order4[::-1]
        order5_inv = order5[::-1]
        
        # self.orders contiene los distintos órdenes que pueden tomar los números de la ficha hegagonal, teniendo en cuenta las dos caras
        self.orders = np.array([listToString(numbers), listToString(order1), listToString(order2),
                                listToString(order3), listToString(order4), listToString(order5),
                                listToString(numbers_inv), listToString(order1_inv),  listToString(order2_inv),
                                listToString(order3_inv),  listToString(order4_inv),  listToString(order5_inv,)])
                                                        

class SmallPiece:
    """ 
    Clase que representa las fichas pequeñas.
    En cada una de las 3 esquinas interiores hay un número del 1 al 4. Cada cara de la ficha presenta los 3 mismos números y con el mismo orden. Por una cara viene representada la suma (+) y por la otra su resta (-).
    Se tiene en cuenta todas las 6 posibles variantes de cada ficha pequeña, según los órdenes que puede presentar (3 por cada una de las caras).
        
        Ejemplo: 
            La representación de la ficha [1, 2, 4] tiene estas 6 posibilidades distintas:
            
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
        
        # self.orders contiene las posibles variantes que pueden tomar los números de la ficha pequeña, con los signos '+' y '-' de cada una de las caras
        self.orders = np.array([listToString(order1), listToString(order2), listToString(order3),
                                listToString(order4), listToString(order5), listToString(order6)])

        