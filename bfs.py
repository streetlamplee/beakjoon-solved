#BFS
from collections import deque
n,m,v = map(int,input().split())
graph = {}
for _ in range(m):
  p,q = map(int, input().split())
  if p not in graph:
    graph[p] = [q]
  elif p in graph:
    graph[p].append(q)
    graph[p].sort()
print(graph)

def bfs(gph,root):
  visited = []
  queue = deque()
  queue.append(root)
  while queue:
    a = queue.popleft()
    visited.append(a)
    tmp = []
    if a in graph:
      for i in range(len(graph[a])):
        if graph[a][i] not in queue:
          tmp.append(graph[a][i])
      queue += tmp
  return visited

result_bfs = bfs(graph, v)
print(result_bfs)