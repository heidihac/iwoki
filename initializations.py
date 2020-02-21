import numpy as np
from gaps import HexagonalGap, SmallGap
from pieces import HexagonalPiece, SmallPiece
import player
import gameState

def initializePieces():
    """ 
    Función que crea/inicializa todas las fichas hexagonales y pequeñas.
    RETURNS:
        hexagonalPieces, smallPieces: listas de fichas hexagonales y pequeñas que van a estar disponibles a lo largo de la partida.
    """
    # Fichas Hexagonales:
    hp1 = HexagonalPiece('hp1', ['*', '5', '2', '4', '6', '6'])
    hp2 = HexagonalPiece('hp2', ['*', '2', '0', '4', '4', '6'])
    hp3 = HexagonalPiece('hp3', ['*', '3', '6', '2', '4', '2'])
    hp4 = HexagonalPiece('hp4', ['*', '4', '0', '3', '4', '6'])
    hp5 = HexagonalPiece('hp5', ['*', '5', '3', '4', '2', '1'])
    hp6 = HexagonalPiece('hp6', ['*', '2', '3', '4', '6', '5'])
    hp7 = HexagonalPiece('hp7', ['*', '6', '0', '5', '2', '4'])
    hp8 = HexagonalPiece('hp8', ['*', '6', '3', '0', '3', '5'])
    hp9 = HexagonalPiece('hp9', ['*', '2', '0', '1', '4', '5'])
    hp10 = HexagonalPiece('hp10', ['*', '6', '4', '2', '0', '3'])
    hp11 = HexagonalPiece('hp11', ['*', '0', '1', '2', '3', '4'])
    hp12 = HexagonalPiece('hp12', ['*', '6', '1', '4', '4', '3'])
    hp13 = HexagonalPiece('hp13', ['*', '4', '1', '6', '3', '5'])
    hp14 = HexagonalPiece('hp14', ['*', '4', '5', '2', '1', '4'])
    hp15 = HexagonalPiece('hp15', ['*', '4', '1', '0', '2', '2'])
    hp16 = HexagonalPiece('hp16', ['*', '6', '5', '5', '4', '3'])
    hp17 = HexagonalPiece('hp17', ['*', '6', '5', '1', '0', '3'])
    hp18 = HexagonalPiece('hp18', ['*', '5', '0', '4', '2', '6'])
    hp19 = HexagonalPiece('hp19', ['*', '5', '4', '4', '2', '0'])
    hp20 = HexagonalPiece('hp20', ['*', '4', '2', '3', '5', '6'])
    
    hexagonalPieces = [hp1,hp2,hp3,hp4,hp5,hp6,hp7,hp8,hp9,hp10,hp11,hp12,hp13,hp14,hp15,hp16,hp17,hp18,hp19,hp20]
    
    # Fichas Pequeñas:
    sp1 = SmallPiece('sp1', ['1','2','3'])
    sp2 = SmallPiece('sp2', ['1','1','2'])
    sp3 = SmallPiece('sp3', ['1','1','3'])
    sp4 = SmallPiece('sp4', ['1','1','4'])
    sp5 = SmallPiece('sp5', ['1','2','2'])
    sp6 = SmallPiece('sp6', ['1','3','3'])
    sp7 = SmallPiece('sp7', ['1','2','4'])
    sp8 = SmallPiece('sp8', ['2','2','2'])
    sp9 = SmallPiece('sp9', ['2','2','3'])
    sp10 = SmallPiece('sp10', ['2','2','4'])
    sp11 = SmallPiece('sp11', ['2','3','3'])
    sp12 = SmallPiece('sp12', ['3','3','3'])

    sp13 = SmallPiece('sp13', ['1','2','3'])
    sp14 = SmallPiece('sp14', ['1','1','2'])
    sp15 = SmallPiece('sp15', ['1','1','3'])
    sp16 = SmallPiece('sp16', ['1','1','4'])
    sp17 = SmallPiece('sp17', ['1','2','2'])
    sp18 = SmallPiece('sp18', ['1','3','3'])
    sp19 = SmallPiece('sp19', ['1','2','4'])
    sp20 = SmallPiece('sp20', ['2','2','2'])
    sp21 = SmallPiece('sp21', ['2','2','3'])
    sp22 = SmallPiece('sp22', ['2','2','4'])
    sp23 = SmallPiece('sp23', ['2','3','3'])
    sp24 = SmallPiece('sp24', ['3','3','3'])

    sp25 = SmallPiece('sp25', ['1','2','3'])
    sp26 = SmallPiece('sp26', ['1','1','2'])
    sp27 = SmallPiece('sp27', ['1','1','3'])
    sp28 = SmallPiece('sp28', ['1','1','4'])
    sp29 = SmallPiece('sp29', ['1','2','2'])
    sp30 = SmallPiece('sp30', ['1','3','3'])
    sp31 = SmallPiece('sp31', ['1','2','4'])
    sp32 = SmallPiece('sp32', ['2','2','2'])
    sp33 = SmallPiece('sp33', ['2','2','3'])
    sp34 = SmallPiece('sp34', ['2','2','4'])
    sp35 = SmallPiece('sp35', ['2','3','3'])
    sp36 = SmallPiece('sp36', ['3','3','3'])

    sp37 = SmallPiece('sp37', ['1','2','3'])
    sp38 = SmallPiece('sp38', ['1','1','2'])
    sp39 = SmallPiece('sp39', ['1','1','3'])
    sp40 = SmallPiece('sp40', ['1','1','4'])
    sp41 = SmallPiece('sp41', ['1','2','2'])
    sp42 = SmallPiece('sp42', ['1','3','3'])
    sp43 = SmallPiece('sp43', ['1','2','4'])
    sp44 = SmallPiece('sp44', ['2','2','2'])
    sp45 = SmallPiece('sp45', ['2','2','3'])
    sp46 = SmallPiece('sp46', ['2','2','4'])
    sp47 = SmallPiece('sp47', ['2','3','3'])
    sp48 = SmallPiece('sp48', ['3','3','3'])
    
    smallPieces = [sp1,sp2,sp3,sp4,sp5,sp6,sp7,sp8,sp9,sp10,sp11,sp12,sp13,sp14,sp15,sp16,
                   sp17,sp18,sp19,sp20,sp21,sp22,sp23,sp24,sp25,sp26,sp27,sp28,sp29,sp30,sp31,sp32,
                   sp33,sp34,sp35,sp36,sp37,sp38,sp39,sp40,sp41,sp42,sp43,sp44,sp45,sp46,sp47,sp48]
    
    return hexagonalPieces, smallPieces


def initializeGaps():
    """ 
    Función que crea/inicializa todos los huecos del tablero virtual.
    RETURNS:
        hexagonalGaps, smallGaps: listas de huecos para fichas hexagonales y pequeñas.
        fittableHexagonalGaps, fittableSmallGaps: listas de huecos, para fichas hexagonales y pequeñas, en los que se puede colocar alguna ficha. 
    """
    # Huecos para fichas hexagonales:
    h1 = HexagonalGap('H1')
    h2 = HexagonalGap('H2')
    h3 = HexagonalGap('H3')
    h4 = HexagonalGap('H4')
    h5 = HexagonalGap('H5')
    h6 = HexagonalGap('H6')
    h7 = HexagonalGap('H7')
    h8 = HexagonalGap('H8')
    h9 = HexagonalGap('H9')
    h10 = HexagonalGap('H10')
    h11 = HexagonalGap('H11')
    h12 = HexagonalGap('H12')
    h13 = HexagonalGap('H13')
    h14 = HexagonalGap('H14')
    h15 = HexagonalGap('H15')
    h16 = HexagonalGap('H16')
    h17 = HexagonalGap('H17')
    h18 = HexagonalGap('H18')
    h19 = HexagonalGap('H19')
    h20 = HexagonalGap('H20')
    h21 = HexagonalGap('H21')
    h22 = HexagonalGap('H22')
    h23 = HexagonalGap('H23')
    h24 = HexagonalGap('H24')
    h25 = HexagonalGap('H25')
    h26 = HexagonalGap('H26')
    h27 = HexagonalGap('H27')
    h28 = HexagonalGap('H28')
    h29 = HexagonalGap('H29')
    h30 = HexagonalGap('H30')
    h31 = HexagonalGap('H31')
    h32 = HexagonalGap('H32')
    h33 = HexagonalGap('H33')
    h34 = HexagonalGap('H34')
    h35 = HexagonalGap('H35')
    h36 = HexagonalGap('H36')
    h37 = HexagonalGap('H37')
    h38 = HexagonalGap('H38')
    h39 = HexagonalGap('H39')
    h40 = HexagonalGap('H40')
    h41 = HexagonalGap('H41')
    h42 = HexagonalGap('H42')
    h43 = HexagonalGap('H43')
    h44 = HexagonalGap('H44')
    h45 = HexagonalGap('H45')
    h46 = HexagonalGap('H46')
    h47 = HexagonalGap('H47')
    h48 = HexagonalGap('H48')
    h49 = HexagonalGap('H49')
    h50 = HexagonalGap('H50')
    h51 = HexagonalGap('H51')
    h52 = HexagonalGap('H52')
    h53 = HexagonalGap('H53')
    h54 = HexagonalGap('H54')
    h55 = HexagonalGap('H55')

    hexagonalGaps = {'H1': h1, 'H2': h2, 'H3': h3, 'H4': h4, 'H5': h5, 'H6': h6, 'H7': h7, 'H8': h8, 'H9': h9, 
                     'H10': h10, 'H11': h11, 'H12': h12, 'H13': h13, 'H14': h14, 'H15': h15, 'H16': h16, 
                     'H17': h17, 'H18': h18, 'H19': h19, 'H20': h20, 'H21': h21, 'H22': h22, 'H23': h23,
                     'H24': h24, 'H25': h25, 'H26': h26, 'H27': h27, 'H28': h28, 'H29': h29, 'H30': h30,
                     'H31': h31, 'H32': h32, 'H33': h33, 'H34': h34, 'H35': h35, 'H36': h36, 'H37': h37,
                     'H38': h38, 'H39': h39, 'H40': h40, 'H41': h41, 'H42': h42, 'H43': h43, 'H44': h44,
                     'H45': h45, 'H46': h46, 'H47': h47, 'H48': h48, 'H49': h49, 'H50': h50, 'H51': h51,
                     'H52': h52, 'H53': h53, 'H54': h54, 'H55': h55}

    # Huecos para fichas pequeñas. Cada elemento de la lista está formado por los siguientes valores:
    #    - id del hueco hexagonal del tablero. 
    #    - Número asignado a ese vértice. '_' indica que el vértice aún no tiene valor asignado. 
    #    - V --> Vacant; 'O' --> Occupied
    h1_h2_h3 = SmallGap([['H1', '2', '_', 'V'], ['H2', '4', '_', 'V'], ['H3', '6', '_', 'V']])
    h1_h3_h4 = SmallGap([['H1', '3', '_', 'V'], ['H3', '5', '_', 'V'], ['H4', '1', '_', 'V']])
    h1_h4_h5 = SmallGap([['H1', '4', '_', 'V'], ['H4', '6', '_', 'V'], ['H5', '2', '_', 'V']])
    h1_h5_h6 = SmallGap([['H1', '5', '_', 'V'], ['H5', '1', '_', 'V'], ['H6', '3', '_', 'V']])
    h1_h6_h7 = SmallGap([['H1', '6', '_', 'V'], ['H6', '2', '_', 'V'], ['H7', '4', '_', 'V']])
    h1_h7_h2 = SmallGap([['H1', '1', '_', 'V'], ['H7', '3', '_', 'V'], ['H2', '5', '_', 'V']])
    h2_h7_h8 = SmallGap([['H2', '6', '_', 'V'], ['H7', '2', '_', 'V'], ['H8', '4', '_', 'V']])
    h2_h8_h9 = SmallGap([['H2', '1', '_', 'V'], ['H8', '3', '_', 'V'], ['H9', '5', '_', 'V']])
    h2_h9_h10 = SmallGap([['H2', '2', '_', 'V'], ['H9', '4', '_', 'V'], ['H10', '6', '_', 'V']])
    h2_h10_h3= SmallGap([['H2', '3', '_', 'V'], ['H10', '5', '_', 'V'], ['H3', '1', '_', 'V']])
    h3_h10_h11 = SmallGap([['H3', '2', '_', 'V'], ['H10', '4', '_', 'V'], ['H11', '6', '_', 'V']])
    h3_h11_h12 = SmallGap([['H3', '3', '_', 'V'], ['H11', '5', '_', 'V'], ['H12', '1', '_', 'V']])
    h3_h12_h4 = SmallGap([['H3', '4', '_', 'V'], ['H12', '6', '_', 'V'], ['H4', '2', '_', 'V']])
    h4_h12_h13 = SmallGap([['H4', '3', '_', 'V'], ['H12', '5', '_', 'V'], ['H13', '1', '_', 'V']])
    h4_h13_h14 = SmallGap([['H4', '4', '_', 'V'], ['H13', '6', '_', 'V'], ['H14', '2', '_', 'V']])
    h4_h14_h5 = SmallGap([['H4', '5', '_', 'V'], ['H14', '1', '_', 'V'], ['H5', '3', '_', 'V']])
    h5_h14_h15 = SmallGap([['H5', '4', '_', 'V'], ['H14', '6', '_', 'V'], ['H15', '2', '_', 'V']])
    h5_h15_h16 = SmallGap([['H5', '5', '_', 'V'], ['H15', '1', '_', 'V'], ['H16', '3', '_', 'V']])
    h5_h16_h6 = SmallGap([['H5', '6', '_', 'V'], ['H16', '2', '_', 'V'], ['H6', '4', '_', 'V']])
    h6_h16_h17 = SmallGap([['H6', '5', '_', 'V'], ['H16', '1', '_', 'V'], ['H17', '3', '_', 'V']])
    h6_h17_h18 = SmallGap([['H6', '6', '_', 'V'], ['H17', '2', '_', 'V'], ['H18', '4', '_', 'V']])
    h6_h18_h7 = SmallGap([['H6', '1', '_', 'V'], ['H18', '3', '_', 'V'], ['H7', '5', '_', 'V']])
    h7_h18_h19 = SmallGap([['H7', '6', '_', 'V'], ['H18', '2', '_', 'V'], ['H19', '4', '_', 'V']])
    h7_h19_h8 = SmallGap([['H7', '1', '_', 'V'], ['H19', '3', '_', 'V'], ['H8', '5', '_', 'V']])
    h8_h19_h20 = SmallGap([['H8', '6', '_', 'V'], ['H19', '2', '_', 'V'], ['H20', '4', '_', 'V']])
    h8_h20_h21 = SmallGap([['H8', '1', '_', 'V'], ['H20', '3', '_', 'V'], ['H21', '5', '_', 'V']])
    h8_h21_h9 = SmallGap([['H8', '2', '_', 'V'], ['H21', '4', '_', 'V'], ['H9', '6', '_', 'V']])
    h9_h21_h22 = SmallGap([['H9', '1', '_', 'V'], ['H21', '3', '_', 'V'], ['H22', '5', '_', 'V']])
    h9_h22_h23 = SmallGap([['H9', '2', '_', 'V'], ['H22', '4', '_', 'V'], ['H23', '6', '_', 'V']])
    h9_h23_h10 = SmallGap([['H9', '3', '_', 'V'], ['H23', '5', '_', 'V'], ['H10', '1', '_', 'V']])
    h10_h23_h24 = SmallGap([['H10', '2', '_', 'V'], ['H23', '4', '_', 'V'], ['H24', '6', '_', 'V']])
    h10_h24_h11 = SmallGap([['H10', '3', '_', 'V'], ['H24', '5', '_', 'V'], ['H11', '1', '_', 'V']])
    h11_h24_h51 = SmallGap([['H11', '2', '_', 'V'], ['H24', '4', '_', 'V'], ['H51', '6', '_', 'V']])
    h11_h51_h25 = SmallGap([['H11', '3', '_', 'V'], ['H51', '5', '_', 'V'], ['H25', '1', '_', 'V']])
    h11_h25_h12 = SmallGap([['H11', '4', '_', 'V'], ['H25', '6', '_', 'V'], ['H12', '2', '_', 'V']])
    h12_h25_h26 = SmallGap([['H12', '3', '_', 'V'], ['H25', '5', '_', 'V'], ['H26', '1', '_', 'V']])
    h12_h26_h13 = SmallGap([['H12', '4', '_', 'V'], ['H26', '6', '_', 'V'], ['H13', '2', '_', 'V']])
    h13_h26_h27 = SmallGap([['H13', '3', '_', 'V'], ['H26', '5', '_', 'V'], ['H27', '1', '_', 'V']])
    h13_h27_h28 = SmallGap([['H13', '4', '_', 'V'], ['H27', '6', '_', 'V'], ['H28', '2', '_', 'V']])
    h13_h28_h14 = SmallGap([['H13', '5', '_', 'V'], ['H28', '1', '_', 'V'], ['H14', '3', '_', 'V']])
    h14_h28_h29 = SmallGap([['H14', '4', '_', 'V'], ['H28', '6', '_', 'V'], ['H29', '2', '_', 'V']])
    h14_h29_h15 = SmallGap([['H14', '5', '_', 'V'], ['H29', '1', '_', 'V'], ['H15', '3', '_', 'V']])
    h15_h29_h30 = SmallGap([['H15', '4', '_', 'V'], ['H29', '6', '_', 'V'], ['H30', '2', '_', 'V']])
    h15_h30_h31 = SmallGap([['H15', '5', '_', 'V'], ['H30', '1', '_', 'V'], ['H31', '3', '_', 'V']])
    h15_h31_h16 = SmallGap([['H15', '6', '_', 'V'], ['H31', '2', '_', 'V'], ['H16', '4', '_', 'V']])
    h16_h31_h32 = SmallGap([['H16', '5', '_', 'V'], ['H31', '1', '_', 'V'], ['H32', '3', '_', 'V']])
    h16_h32_h17 = SmallGap([['H16', '6', '_', 'V'], ['H32', '2', '_', 'V'], ['H17', '4', '_', 'V']])
    h17_h32_h54 = SmallGap([['H17', '5', '_', 'V'], ['H32', '1', '_', 'V'], ['H54', '3', '_', 'V']])
    h17_h54_h33 = SmallGap([['H17', '6', '_', 'V'], ['H54', '2', '_', 'V'], ['H33', '4', '_', 'V']])
    h17_h33_h18 = SmallGap([['H17', '1', '_', 'V'], ['H33', '3', '_', 'V'], ['H18', '5', '_', 'V']])
    h18_h33_h34 = SmallGap([['H18', '6', '_', 'V'], ['H33', '2', '_', 'V'], ['H34', '4', '_', 'V']])
    h18_h34_h19 = SmallGap([['H18', '1', '_', 'V'], ['H34', '3', '_', 'V'], ['H19', '5', '_', 'V']])
    h19_h34_h35 = SmallGap([['H19', '6', '_', 'V'], ['H34', '2', '_', 'V'], ['H35', '4', '_', 'V']])
    h19_h35_h20 = SmallGap([['H19', '1', '_', 'V'], ['H35', '3', '_', 'V'], ['H20', '5', '_', 'V']])
    h20_h35_h36 = SmallGap([['H20', '6', '_', 'V'], ['H35', '2', '_', 'V'], ['H36', '4', '_', 'V']])
    h20_h36_h37 = SmallGap([['H20', '1', '_', 'V'], ['H36', '3', '_', 'V'], ['H37', '5', '_', 'V']])
    h20_h37_h21 = SmallGap([['H20', '2', '_', 'V'], ['H37', '4', '_', 'V'], ['H21', '6', '_', 'V']])
    h21_h37_h38 = SmallGap([['H21', '1', '_', 'V'], ['H37', '3', '_', 'V'], ['H38', '5', '_', 'V']])
    h21_h38_h22 = SmallGap([['H21', '2', '_', 'V'], ['H38', '4', '_', 'V'], ['H22', '6', '_', 'V']])
    h22_h38_h39 = SmallGap([['H22', '1', '_', 'V'], ['H38', '3', '_', 'V'], ['H39', '5', '_', 'V']])
    h22_h39_h40 = SmallGap([['H22', '2', '_', 'V'], ['H39', '4', '_', 'V'], ['H40', '6', '_', 'V']])
    h22_h40_h23 = SmallGap([['H22', '3', '_', 'V'], ['H40', '5', '_', 'V'], ['H23', '1', '_', 'V']])
    h23_h40_h50 = SmallGap([['H23', '2', '_', 'V'], ['H40', '4', '_', 'V'], ['H50', '6', '_', 'V']])
    h23_h50_h24 = SmallGap([['H23', '3', '_', 'V'], ['H50', '5', '_', 'V'], ['H24', '1', '_', 'V']])
    h26_h25_h52 = SmallGap([['H26', '2', '_', 'V'], ['H25', '4', '_', 'V'], ['H52', '6', '_', 'V']])
    h26_h52_h41 = SmallGap([['H26', '3', '_', 'V'], ['H52', '5', '_', 'V'], ['H41', '1', '_', 'V']])
    h26_h41_h27 = SmallGap([['H26', '4', '_', 'V'], ['H41', '6', '_', 'V'], ['H27', '2', '_', 'V']])
    h27_h41_h42 = SmallGap([['H27', '3', '_', 'V'], ['H41', '5', '_', 'V'], ['H42', '1', '_', 'V']])
    h27_h42_h43 = SmallGap([['H27', '4', '_', 'V'], ['H42', '6', '_', 'V'], ['H43', '2', '_', 'V']])
    h27_h43_h28 = SmallGap([['H27', '5', '_', 'V'], ['H43', '1', '_', 'V'], ['H28', '3', '_', 'V']])
    h28_h43_h44 = SmallGap([['H28', '4', '_', 'V'], ['H43', '6', '_', 'V'], ['H44', '2', '_', 'V']])
    h28_h44_h29 = SmallGap([['H28', '5', '_', 'V'], ['H44', '1', '_', 'V'], ['H29', '3', '_', 'V']])
    h29_h44_h45 = SmallGap([['H29', '4', '_', 'V'], ['H44', '6', '_', 'V'], ['H45', '2', '_', 'V']])
    h29_h45_h30 = SmallGap([['H29', '5', '_', 'V'], ['H45', '1', '_', 'V'], ['H30', '3', '_', 'V']])
    h30_h45_h46 = SmallGap([['H30', '4', '_', 'V'], ['H45', '6', '_', 'V'], ['H46', '2', '_', 'V']])
    h30_h46_h47 = SmallGap([['H30', '5', '_', 'V'], ['H46', '1', '_', 'V'], ['H47', '3', '_', 'V']])
    h30_h47_h31 = SmallGap([['H30', '6', '_', 'V'], ['H47', '2', '_', 'V'], ['H31', '4', '_', 'V']])
    h31_h47_h55 = SmallGap([['H31', '5', '_', 'V'], ['H47', '1', '_', 'V'], ['H55', '3', '_', 'V']])
    h31_h55_h32 = SmallGap([['H31', '6', '_', 'V'], ['H55', '2', '_', 'V'], ['H32', '4', '_', 'V']])
    h34_h33_h53 = SmallGap([['H34', '5', '_', 'V'], ['H33', '1', '_', 'V'], ['H53', '3', '_', 'V']])
    h34_h53_h48 = SmallGap([['H34', '6', '_', 'V'], ['H53', '2', '_', 'V'], ['H48', '4', '_', 'V']])
    h34_h48_h35 = SmallGap([['H34', '1', '_', 'V'], ['H48', '3', '_', 'V'], ['H35', '5', '_', 'V']])
    h35_h48_h49 = SmallGap([['H35', '6', '_', 'V'], ['H48', '2', '_', 'V'], ['H49', '4', '_', 'V']])
    h35_h49_h36 = SmallGap([['H35', '1', '_', 'V'], ['H49', '3', '_', 'V'], ['H36', '5', '_', 'V']])

    smallGaps = {'H1_H2_H3':h1_h2_h3, 'H1_H3_H4':h1_h3_h4, 'H1_H4_H5':h1_h4_h5, 'H1_H5_H6':h1_h5_h6, 
                 'H1_H6_H7':h1_h6_h7, 'H1_H7_H2':h1_h7_h2, 'H2_H7_H8':h2_h7_h8, 'H2_H8_H9':h2_h8_h9, 
                 'H2_H9_H10':h2_h9_h10, 'H2_H10_H3':h2_h10_h3, 'H3_H10_H11':h3_h10_h11, 'H7_H19_H8':h7_h19_h8,
                 'H3_H12_H4':h3_h12_h4, 'H4_H12_H13':h4_h12_h13, 'H4_H13_H14':h4_h13_h14, 
                 'H5_H14_H15':h5_h14_h15, 'H5_H15_H16':h5_h15_h16, 'H5_H16_H6':h5_h16_h6, 
                 'H6_H17_H18':h6_h17_h18, 'H6_H18_H7':h6_h18_h7, 'H7_H18_H19':h7_h18_h19,  
                 'H8_H19_H20':h8_h19_h20, 'H8_H20_H21':h8_h20_h21, 'H8_H21_H9':h8_h21_h9, 
                 'H3_H11_H12':h3_h11_h12, 'H4_H14_H5':h4_h14_h5, 'H6_H16_H17':h6_h16_h17, 
                 'H9_H22_H23':h9_h22_h23, 'H9_H23_H10':h9_h23_h10, 'H10_H23_H24':h10_h23_h24, 
                 'H10_H24_H11':h10_h24_h11, 'H11_H24_H51':h11_h24_h51, 'H11_H51_H25':h11_h51_h25, 
                 'H11_H25_H12':h11_h25_h12, 'H12_H25_H26':h12_h25_h26, 'H12_H26_H13':h12_h26_h13, 
                 'H13_H26_H27':h13_h26_h27, 'H13_H27_H28':h13_h27_h28, 'H13_H28_H14':h13_h28_h14, 
                 'H14_H29_H15':h14_h29_h15, 'H15_H29_H30':h15_h29_h30, 'H15_H30_H31':h15_h30_h31, 
                 'H15_H31_H16':h15_h31_h16, 'H16_H31_H32':h16_h31_h32, 'H16_H32_H17':h16_h32_h17, 
                 'H17_H32_H54':h17_h32_h54, 'H17_H54_H33':h17_h54_h33, 'H17_H33_H18':h17_h33_h18, 
                 'H18_H33_H34':h18_h33_h34, 'H18_H34_H19':h18_h34_h19, 'H19_H34_H35':h19_h34_h35, 
                 'H19_H35_H20':h19_h35_h20, 'H20_H35_H36':h20_h35_h36, 'H20_H36_H37':h20_h36_h37, 
                 'H20_H37_H21':h20_h37_h21, 'H21_H37_H38':h21_h37_h38, 'H21_H38_H22':h21_h38_h22, 
                 'H22_H38_H39':h22_h38_h39, 'H22_H39_H40':h22_h39_h40, 'H22_H40_H23':h22_h40_h23, 
                 'H23_H40_H50':h23_h40_h50, 'H23_H50_H24':h23_h50_h24, 'H26_H25_H52':h26_h25_h52, 
                 'H26_H52_H41':h26_h52_h41, 'H26_H41_H27':h26_h41_h27, 'H27_H41_H42':h27_h41_h42, 
                 'H27_H42_H43':h27_h42_h43, 'H27_H43_H28':h27_h43_h28, 'H28_H43_H44':h28_h43_h44, 
                 'H28_H44_H29':h28_h44_h29, 'H29_H44_H45':h29_h44_h45, 'H29_H45_H30':h29_h45_h30, 
                 'H30_H45_H46':h30_h45_h46, 'H30_H46_H47':h30_h46_h47, 'H30_H47_H31':h30_h47_h31, 
                 'H31_H47_H55':h31_h47_h55, 'H31_H55_H32':h31_h55_h32, 'H34_H33_H53':h34_h33_h53, 
                 'H34_H53_H48':h34_h53_h48, 'H34_H48_H35':h34_h48_h35, 'H35_H48_H49':h35_h48_h49, 
                 'H35_H49_H36':h35_h49_h36, 'H14_H28_H29':h14_h28_h29, 'H9_H21_H22':h9_h21_h22}

    fittableHexagonalGaps = {}
    fittableSmallGaps = {}

    return hexagonalGaps, smallGaps, fittableHexagonalGaps, fittableSmallGaps


def initializeAll(players):
    """
    Función que inicializa todas fichas, los huecos y los jugadores.
    PARAMETER:
        players: lista de jugadores.
    RETURN:
        bameSpace: espacio de juego.
    """
    print("Se incicializan todas las fichas.")
    hexagonalPiecesAvailable, smallPiecesAvailable = initializePieces()

    print("Se incicializan todos los huecos.")
    hexagonalGaps, smallGaps, fittableHexagonalGaps, fittableSmallGaps = initializeGaps()
    
    print("Se inicializan los jugadores.")
    for player in players:
        player.isTurn = False
        player.smallPieces = []
        player.hexagonalPieces = []
        player.score = 0
        player.redIndicator = False
        player.whiteIndicator = 0
        player.gotPieceBefore = False
        
    print("Se crea el espacio de juego.")
    gameSpace = gameState.GameState(players, hexagonalPiecesAvailable, smallPiecesAvailable, hexagonalGaps, smallGaps,
                                    fittableHexagonalGaps, fittableSmallGaps)
    return gameSpace

