import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

picture = list()
for _ in range(n):
    tmp = list(map(int, input().strip().split()))
    picture.append(tmp)

visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
move = [(1,0),(-1,0),(0,1),(0,-1)]
group = 1
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            queue.appendleft((i, j, group))
            while queue:
                i_q, j_q, group = queue.pop()
                visited[i_q][j_q] = group
                for mv in move:
                    i_next, j_next = (i_q, j_q) + mv
                    if i_next < 0 and i_next >= n:
                        continue
                    if j_next < 0 and j_next > m:
                        continue
                    if picture[i_next][j_next] == 0:
                        continue
                    if visited[i_next][j_next] != 0:
                        continue
            group += 1

print(group)


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")