# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

lines = np.loadtxt("day_1.txt")

increases1 = (lines[1:] > lines[:-1]).sum()
print("challenge 1 solution: ",increases1)

increases2 = (lines[3:] > lines[:-3]).sum()
print("challengen 2 solution : ",increases2)