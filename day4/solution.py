import numpy as np
from itertools import product

with open("day_4.txt") as fp:
    draws = list(map(int, fp.readline().split(",")))
    boards = [np.mat(board.replace("\n", ";")) for board in fp.read()[1:-1].split("\n\n")]

for draw, board in product(draws, [np.ma.masked_array(board) for board in boards]):
    board.mask |= board.data == draw
    if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
        result = board.sum()*draw
        break
print("Part 1 result:", result)

won_boards = set()
for draw, (idx, board) in product(draws, enumerate([np.ma.masked_array(board) for board in boards])):
    board.mask |= board.data == draw
    if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
        if idx not in won_boards and len(won_boards) == len(boards) -1:
            result = board.sum()*draw
            break
        won_boards.add(idx)
print("Part 2 result:", result)
