import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())

g = {}
for _ in range(m):
    x, y = map(int, input().strip().split())
    if x not in g.keys():
        g[x] = [y]
    else:
        g[x].append(y)
        g[x].sort()
    if y not in g.keys():
        g[y] = [x]
    else:
        g[y].append(x)
        g[y].sort()

def dfs(g, root):
    queue = deque()
    visited = []
    queue.append(root)
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            if node in g.keys():
                queue.extend(sorted(g[node], reverse = True))
        else:
            pass
    return visited

def bfs(g, root):
    queue = deque()
    visited = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in g.keys():
               queue.extend(g[node]) 
        else:
            pass
    return visited
            
print(*dfs(g,v))
print(*bfs(g,v))


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")