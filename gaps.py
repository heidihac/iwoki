import numpy as np

class SmallGap:
    """
    Class that represents a gap in the game board reserved for a small tile.
    """
    def __init__(self, vertices):
        self.vertices = vertices # list in which each element corresponds to an interior vertex of the tile gap
        idAux = ''
        for vertix in vertices:
            idAux = idAux + vertix[0] if idAux == '' else idAux + '_' + vertix[0]
        self.id = idAux


class HexagonalGap:
    """ Class that represents a gap in the game board reserved for a hexagonal tile.
        The gap identifier and the order number of the vertex define the common coordinates of the vertex which connect a hexagonal and a small tile.
    """
    def __init__(self, idHexagonal):
        self.id = idHexagonal
        # 'vertices' is a list in which each element corresponds to a vertex of the hexagon and includes the following:
        # - Hexagonal gap identifier.
        # - Vertex order number (from 1 to 6).
        # - Number assigned to that vertex when a hexagonal tile is placed in this gap. '_' indicates that the vertex has not yet been assigned a value .
        # - 'V' --> Vacant; 'O' --> Occupied.
        self.vertices = np.array([[idHexagonal, 1, '_', 'V'], [idHexagonal, 2, '_', 'V'], [idHexagonal, 3, '_', 'V'],
                         [idHexagonal, 4, '_', 'V'], [idHexagonal, 5, '_', 'V'], [idHexagonal, 6, '_', 'V']])

        