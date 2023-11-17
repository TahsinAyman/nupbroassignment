import numpy as np


file = open("input1a.txt", "r")
f = open("output1a.txt", "w")

lst = file.readline().split()

vertices = int(lst[0]) + 1
edges = int(lst[1])

arr = np.zeros((vertices,vertices), dtype=int)
row,col = arr.shape
for i in range(edges):
  direction = [int(y) for y in file.readline().split()]
  for j in range(row):
    for k in range(col):
      if j==direction[0] and k==direction[1]:
        arr[j][k] = direction[2]

for i in range(row):
  for j in range(col):
    f.write(str(arr[i][j])+' ')
  f.write("\n")

file.close()
f.close()
