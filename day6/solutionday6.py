import numpy as np

lines = np.loadtxt("day_6.txt", delimiter=",", dtype="uint32")
fish = np.zeros(9)
age, count = np.unique(lines, return_counts=True)
fish[age] = count

gen = np.copy(fish)
for _ in range(80):
    gen[7] += gen[0]
    gen = np.roll(gen, -1)
result = sum(gen)
print("Part 1 result:", result)

gen = np.copy(fish)
for _ in range(256):
    gen[7] += gen[0]
    gen = np.roll(gen, -1)
result = sum(gen)
print("Part 2 result:", result)
