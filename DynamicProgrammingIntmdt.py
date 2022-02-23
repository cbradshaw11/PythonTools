# Intermediate Dynamic Programming Problem Practice

import random

m = 10
n = 10
matrix = []

for i in range(m):
    l = []
    for j in range(n):
        l.append(random.randint(0,100))
    print(l)
    matrix.append(l)


print("***")

class node:
    def __init__(self, val, bigPath):
        self.val = val
        self.bigPath = bigPath

newMatrix = [None] * m
for i in range(m):
    l = [None] * n
    newMatrix[i] = l

for i in range(m):
    if i == 0:
        for j in range(n):
            if j == 0:
                newMatrix[i][j] = matrix[i][j]
            else:
                newMatrix[i][j] = matrix[i][j] + newMatrix[i][j-1]
        continue
    for j in range(n):
        if j == 0:
            newMatrix[i][j] = matrix[i][j] + newMatrix[i-1][j]
        else:
            if newMatrix[i-1][j] > newMatrix[i][j-1]:
                newMatrix[i][j] = newMatrix[i-1][j] + matrix[i][j]
            else:
                newMatrix[i][j] = newMatrix[i][j-1] + matrix[i][j]
for i in newMatrix:
    print i
