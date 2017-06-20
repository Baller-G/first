import numpy as np

block = np.ones((4,5))
print(block)

line = np.ones(5)
line[:] = 0
line[0] = 1
print(line)

print(block * line)

block[1, 2] = 10
block *= 2
print(block)

print(block.sum())
print (block.sum(axis=1))
print(block.sum(0))