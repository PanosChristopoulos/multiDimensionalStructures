from collections import namedtuple
from operator import itemgetter
from pprint import pformat

dict32 = {0: [(2, 4, 3, 7), (3, 3, 5, 4), (2, 4, 3, 2), (5, 12, 3, 9), (7, 37, 3, 2), (24, 21, 42, 1), (23, 24, 1, 5), (42, 4, 4, 1), (3, 5, 2, 4), (72, 3, 3, 89)], 1: ([(2, 4, 3, 7), (3, 3, 5, 4), (2, 4, 3, 2), (5, 12, 3, 9), (7, 37, 3, 2), (24, 21, 42, 1), (23, 24, 1, 5)], [(42, 4, 4, 1), (3, 5, 2, 4), (72, 3, 3, 89)])}

for k, v in dict32.items():
    print(k, v)
