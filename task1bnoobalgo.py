file = open("input1b.txt", "r")
f = open("output1b.txt", "w")

lst = file.readline().split()

vertices = int(lst[0])
edges = int(lst[1])

dic = {}
f.write(f'0:\n')
for i in range(1,vertices):
  direction = [int(y) for y in file.readline().split()]
  if not dic.get(direction[0]):
    dic[direction[0]] = [] 
  if not dic.get(direction[1]):
    dic[direction[1]] = [] 
  dic[direction[0]].append((direction[1], direction[2]))
dic = dict(sorted(dic.items()))


for key, value in dic.items():
  v = ""
  for i in value:
    v += str(i) + " "
  f.write(f"{key}: {v}\n")
print(dic)