file = open("input1b.txt", "r")
f = open("output1b.txt", "w")

lst = file.readline().split()

vertices = int(lst[0])
edges = int(lst[1])

combinations = []
for i in range(edges):
  lt = [int(y) for y in file.readline().split()]
  combinations.append(lt)
start = []

print(combinations)

for i in combinations:
  start.append(i[0])

start.sort()
final = []
for i in start:
  for j in combinations:
    if j[0] == i and j not in final:
      final.append(j)

print(final)

for i in range(vertices+1):
  f.write(f'{i}:')
  

file.close()
f.close()
      