import numpy as np
from gaps import HexagonalGap, SmallGap
from tiles import HexagonalTile, SmallTile
import player
import gameState

def initializeTiles():
    """ 
    Función that creates/initializes all hexagonal and small tiles.
    RETURNS:
        hexagonalTiles, smallTiles: lists of hexagonal and small tiles that will be available throughout the game.
    """
    # Hexagonal tiles:
    ht1 = HexagonalTile('ht1', ['*', '5', '2', '4', '6', '6'])
    ht2 = HexagonalTile('ht2', ['*', '2', '0', '4', '4', '6'])
    ht3 = HexagonalTile('ht3', ['*', '3', '6', '2', '4', '2'])
    ht4 = HexagonalTile('ht4', ['*', '4', '0', '3', '4', '6'])
    ht5 = HexagonalTile('ht5', ['*', '5', '3', '4', '2', '1'])
    ht6 = HexagonalTile('ht6', ['*', '2', '3', '4', '6', '5'])
    ht7 = HexagonalTile('ht7', ['*', '6', '0', '5', '2', '4'])
    ht8 = HexagonalTile('ht8', ['*', '6', '3', '0', '3', '5'])
    ht9 = HexagonalTile('ht9', ['*', '2', '0', '1', '4', '5'])
    ht10 = HexagonalTile('ht10', ['*', '6', '4', '2', '0', '3'])
    ht11 = HexagonalTile('ht11', ['*', '0', '1', '2', '3', '4'])
    ht12 = HexagonalTile('ht12', ['*', '6', '1', '4', '4', '3'])
    ht13 = HexagonalTile('ht13', ['*', '4', '1', '6', '3', '5'])
    ht14 = HexagonalTile('ht14', ['*', '4', '5', '2', '1', '4'])
    ht15 = HexagonalTile('ht15', ['*', '4', '1', '0', '2', '2'])
    ht16 = HexagonalTile('ht16', ['*', '6', '5', '5', '4', '3'])
    ht17 = HexagonalTile('ht17', ['*', '6', '5', '1', '0', '3'])
    ht18 = HexagonalTile('ht18', ['*', '5', '0', '4', '2', '6'])
    ht19 = HexagonalTile('ht19', ['*', '5', '4', '4', '2', '0'])
    ht20 = HexagonalTile('ht20', ['*', '4', '2', '3', '5', '6'])
    
    hexagonalTiles = [ht1,ht2,ht3,ht4,ht5,ht6,ht7,ht8,ht9,ht10,ht11,ht12,ht13,ht14,ht15,ht16,ht17,ht18,ht19,ht20]
    
    # Small tiles:
    st1 = SmallTile('st1', ['1','2','3'])
    st2 = SmallTile('st2', ['1','1','2'])
    st3 = SmallTile('st3', ['1','1','3'])
    st4 = SmallTile('st4', ['1','1','4'])
    st5 = SmallTile('st5', ['1','2','2'])
    st6 = SmallTile('st6', ['1','3','3'])
    st7 = SmallTile('st7', ['1','2','4'])
    st8 = SmallTile('st8', ['2','2','2'])
    st9 = SmallTile('st9', ['2','2','3'])
    st10 = SmallTile('st10', ['2','2','4'])
    st11 = SmallTile('st11', ['2','3','3'])
    st12 = SmallTile('st12', ['3','3','3'])

    st13 = SmallTile('st13', ['1','2','3'])
    st14 = SmallTile('st14', ['1','1','2'])
    st15 = SmallTile('st15', ['1','1','3'])
    st16 = SmallTile('st16', ['1','1','4'])
    st17 = SmallTile('st17', ['1','2','2'])
    st18 = SmallTile('st18', ['1','3','3'])
    st19 = SmallTile('st19', ['1','2','4'])
    st20 = SmallTile('st20', ['2','2','2'])
    st21 = SmallTile('st21', ['2','2','3'])
    st22 = SmallTile('st22', ['2','2','4'])
    st23 = SmallTile('st23', ['2','3','3'])
    st24 = SmallTile('st24', ['3','3','3'])

    st25 = SmallTile('st25', ['1','2','3'])
    st26 = SmallTile('st26', ['1','1','2'])
    st27 = SmallTile('st27', ['1','1','3'])
    st28 = SmallTile('st28', ['1','1','4'])
    st29 = SmallTile('st29', ['1','2','2'])
    st30 = SmallTile('st30', ['1','3','3'])
    st31 = SmallTile('st31', ['1','2','4'])
    st32 = SmallTile('st32', ['2','2','2'])
    st33 = SmallTile('st33', ['2','2','3'])
    st34 = SmallTile('st34', ['2','2','4'])
    st35 = SmallTile('st35', ['2','3','3'])
    st36 = SmallTile('st36', ['3','3','3'])

    st37 = SmallTile('st37', ['1','2','3'])
    st38 = SmallTile('st38', ['1','1','2'])
    st39 = SmallTile('st39', ['1','1','3'])
    st40 = SmallTile('st40', ['1','1','4'])
    st41 = SmallTile('st41', ['1','2','2'])
    st42 = SmallTile('st42', ['1','3','3'])
    st43 = SmallTile('st43', ['1','2','4'])
    st44 = SmallTile('st44', ['2','2','2'])
    st45 = SmallTile('st45', ['2','2','3'])
    st46 = SmallTile('st46', ['2','2','4'])
    st47 = SmallTile('st47', ['2','3','3'])
    st48 = SmallTile('st48', ['3','3','3'])
    
    smallTiles = [st1,st2,st3,st4,st5,st6,st7,st8,st9,st10,st11,st12,st13,st14,st15,st16,
                   st17,st18,st19,st20,st21,st22,st23,st24,st25,st26,st27,st28,st29,st30,st31,st32,
                   st33,st34,st35,st36,st37,st38,st39,st40,st41,st42,st43,st44,st45,st46,st47,st48]
    
    return hexagonalTiles, smallTiles


def initializeGaps():
    """ 
    Function that creates/initializes al the gaps in the virtual board.
    RETURNS:
        hexagonalGaps, smallGaps: lists of gaps for hexagonal and small tiles.
        fittableHexagonalGaps, fittableSmallGaps: lists of gaps in which hexagonal and small tiles can be placed. 
    """
    # Gaps for hexagonal tiles:
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

    # Gaps for small tiles. Each item on the list consists of the following values:
    #    - id of the hexagonal gap in the board. 
    #    - Number assigned to that vertex. '_' indicates that the vertex has not yet been assigned a value. 
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
    Function that initializes all tiles, gaps and players.
    PARAMETER:
        players: list of players.
    RETURN:
        bameSpace.
    """
    print("All tiles are initialized.")
    hexagonalTilesAvailable, smallTilesAvailable = initializeTiles()

    print("All gaps are initialized.")
    hexagonalGaps, smallGaps, fittableHexagonalGaps, fittableSmallGaps = initializeGaps()
    
    print("All players are initialized.")
    for player in players:
        player.isTurn = False
        player.smallTiles = []
        player.hexagonalTiles = []
        player.score = 0
        player.redIndicator = False
        player.whiteIndicators = 0
        player.gotTileBefore = False
        
    print("Game space is created.")
    gameSpace = gameState.GameState(players, hexagonalTilesAvailable, smallTilesAvailable, hexagonalGaps, smallGaps,
                                    fittableHexagonalGaps, fittableSmallGaps)
    return gameSpace

