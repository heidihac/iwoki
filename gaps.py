import numpy as np

class SmallGap:
    """
    Clase que representa un hueco del tablero de juego reservado para una ficha pequeña.
    """
    def __init__(self, vertices):
        self.vertices = vertices # lista en la que cada elemento corresponde con un vértice interior del hueco de la ficha
        idAux = ''
        for vertix in vertices:
            idAux = idAux + vertix[0] if idAux == '' else idAux + '_' + vertix[0]
        self.id = idAux


class HexagonalGap:
    """ Clase que representa un hueco del tablero de juego reservado para una ficha hexagonal.
        El identificador del hueco y el número de orden del vértice definen las coordenadas comunes del vértice que une a una ficha hexagonal y otra pequeña.
    """
    def __init__(self, idHexagonal):
        self.id = idHexagonal
        # 'vertices' es una lista en la que cada elemento corresponde con un vértice del hexágono e incluye lo siguiente:
        # - Identificador del hueco hexagonal.
        # - Número de orden del vértice (del 1 al 6).
        # - Número asignado a ese vértice cuando se coloca en ese hueco una ficha hexagonal. '_' indica que el vértice aún no tiene valor asignado. 
        # - 'V' --> Vacant; 'O' --> Occupied.
        self.vertices = np.array([[idHexagonal, 1, '_', 'V'], [idHexagonal, 2, '_', 'V'], [idHexagonal, 3, '_', 'V'],
                         [idHexagonal, 4, '_', 'V'], [idHexagonal, 5, '_', 'V'], [idHexagonal, 6, '_', 'V']])

        