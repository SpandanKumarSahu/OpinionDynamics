'''
Uses a recursive linear-time algorithm (Gabow's algorithm) to find all
strongly connected components of a directed graph.
'''

def strongly_connected_components_path(vertices, edges):
    identified = set()
    stack = []
    index = {}
    boundaries = []

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        boundaries.append(index[v])

        for w in edges[v]:
            if w not in index:
                for scc in dfs(w):
                    yield scc
            elif w not in identified:
                while index[w] < boundaries[-1]:
                    boundaries.pop()

        if boundaries[-1] == index[v]:
            boundaries.pop()
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in vertices:
        if v not in index:
            for scc in dfs(v):
                yield scc

with open('userList.txt', 'r') as file:
    users = file.readlines()
    users = [x.strip() for x in users]

if '' in users:
    users.remove('')

edges = {}
for user in users:
    edges[user] = []

with open('relationList.txt', 'r') as file:
    relations = file.readlines()
    relations = [x.strip() for x in relations]

if '' in relations:
    relations.remove('')

for relation in relations:
    r = relation.split()
    edges[r[0]].append(r[1])

count = 0
for scc in  strongly_connected_components_path(users, edges):
    s = str("SCC-") + str(count) + str(".txt")
    with open(s, 'w') as file:
	if(len(list(scc))> 1):
            for u in list(scc):
                file.write(str(u)+"\n")
	    count += 1
