def get_input():
    vertices, edges = [int(x) for x in input().strip().split()]
    lst = []
    for i in range(edges):
        x, y = [int(z) for z in input().strip().split()]
        lst.append((x, y))
    lst = sorted(lst, key=lambda x: x[0])
    return lst


def store_vertex():
    # this function stores the vertices and edges in a dictionary
    store = {}
    for x, y in lst:
        if x in store.keys():
            store[x].append(y)
        else:
            store[x] = [y]
    return store


def show(key=None):
    # this function prints the vertex and edges
    if not key:
        key = list(store.keys())[0]
    if key in store.keys():
        if not key in printed:
            print(key)
        printed.append(key)
        if store[key]:
            for x in store[key]:
                if not x in printed:
                    print(x)
                printed.append(x)
            for y in store[key]:
                show(y)

lst = get_input()
store = store_vertex()
printed = []
show()
"""
Test Case 1:
Input:
5 5
1 2
1 3
2 7
3 5
3 6
Output:
1
2
7
3
5
6
"""
