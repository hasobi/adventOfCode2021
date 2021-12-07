import numpy as np
import re

lines = open("day_5.txt").readlines()
coords = np.array([re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in lines]).astype(int)
size = np.max(coords)+1

def rrange(start, stop):
    return range(start, stop+1) if stop >= start else range(start, stop-1, -1)

grid = np.zeros((size, size))
hv = coords[(coords[:, 0] == coords[:, 2]) + (coords[:, 1] == coords[:, 3])]
for x1, y1, x2, y2 in hv:
    grid[rrange(y1, y2), rrange(x1, x2)] += 1
result = (grid >= 2).sum()
print("Part 1 result:", result)

grid = np.zeros((size, size))
for x1, y1, x2, y2 in coords:
    grid[rrange(y1, y2), rrange(x1, x2)] += 1
result = (grid >= 2).sum()
print("Part 2 result:", result)
