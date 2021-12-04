lines = [line.split() for line in open('day_2.txt').readlines()]

moves = dict(forward=1, down=1j, up=-1j)
pos = sum(map(lambda line: moves[line[0]]*int(line[1]), lines))
result = pos.real * pos.imag
print("Part 1 result:", result )

from collections import defaultdict
from functools import reduce
import numpy as np

moves = defaultdict(lambda: np.zeros([4, 4]))
moves["down"][2, 3] = 1
moves["up"][2, 3] = -1
moves["forward"][0:2, 2:4] = [[0,1],[1,0]]

pos = reduce(lambda pos, line: (np.identity(4)+moves[line[0]]*int(line[1])).dot(pos), lines, [0, 0, 0, 1])
result = pos[0]*pos[1]
print("Part 2 result:", result )