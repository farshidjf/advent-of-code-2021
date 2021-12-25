from copy import deepcopy
aa = [1, 1, 1, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26, 26]
bb = [12, 13, 12, -13, 11, 15, -14, 12, -8, 14, -9, -11, -6, -5]
cc = [1, 9, 11, 6, 6, 13, 13, 5, 7, 2, 10, 14, 7, 1]
block = lambda a, b, c, z, w: z // a if z % 26 + b == w else 26 * (z // a) + w + c
for puzzle in (1, 2):
      final_z = {0: tuple()}
      for a, b, c in zip(aa, bb, cc):
            _final_z = dict()
            for w in range(1, 10) if puzzle == 1 else range(9, 0, -1):
                  for z in final_z.keys():
                        if (fz := block(a, b, c, z, w)) < 1000000:
                              _final_z[fz] = (*final_z[z], w)
            final_z = deepcopy(_final_z)
      print(f'Puzzle {puzzle}: ' + ''.join(map(str,final_z[0])))
      
# The input is 14 copies of the same instruction block with some different constants I store in aa, bb, and cc.
# I coded these instructions in block lambda.
# Each block starts by reading w from input and only carries the value of z from the previous block.
# At the end of each block I store which highest/lowest value combinations of inputs that lead to the same final z in final_z.
# I discarded values of z higher than 1000000 to speed up the code. Apparently, that's good enough!
      
#     1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |    9    |   10    |   11    |   12    |   13    |   14    |
# --------------------------------------------------------------------------------------------------------------------------------------------
# inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |inp w    |
# mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |mul x 0  |
# add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |add x z  |
# mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |mod x 26 |
# div z 1  |div z 1  |div z 1  |div z 26 |div z 1  |div z 1  |div z 26 |div z 1  |div z 26 |div z 1  |div z 26 |div z 26 |div z 26 |div z 26 |
# add x 12 |add x 13 |add x 12 |add x -13|add x 11 |add x 15 |add x -14|add x 12 |add x -8 |add x 14 |add x -9 |add x -11|add x -6 |add x -5 |
# eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |eql x w  |
# eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |eql x 0  |
# mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |
# add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |add y 25 |
# mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |
# add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |add y 1  |
# mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |mul z y  |
# mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |mul y 0  |
# add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |add y w  |
# add y 1  |add y 9  |add y 11 |add y 6  |add y 6  |add y 13 |add y 13 |add y 5  |add y 7  |add y 2  |add y 10 |add y 14 |add y 7  |add y 1  |
# mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |mul y x  |
# add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |add z y  |
# --------------------------------------------------------------------------------------------------------------------------------------------
