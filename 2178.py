import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().strip().split())
g = []
cost_map =  []
for _ in range(n):
    tmp = []
    for _ in range(m):
        tmp.append(10001)
    cost_map.append(tmp)

for _ in range(n):
    row = input().strip()
    g.append(row)


s = [0,0,1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
queue.append(s)
visit_map = []
for _ in range(n):
    tmp = []
    for _ in range(m):
        tmp.append(0)
    visit_map.append(tmp)
while queue:
    row, col, cost = queue.popleft()
    cost_map[row][col] = cost
    visit_map[row][col] = 1
    for i in range(4):
        next_row, next_col, next_cost = row + dx[i], col + dy[i], cost + 1
        
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
            continue
        elif visit_map[next_row][next_col] == 1:
            continue
        elif g[next_row][next_col] == '0':
            continue
        else:
            queue.append([next_row, next_col, next_cost])


print(cost_map[n-1][m-1])



##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")