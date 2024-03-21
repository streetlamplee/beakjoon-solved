import sys
from collections import deque

inp = sys.stdin.readline
q = deque()

n, k = map(int, inp().rstrip().split())
tmp_li = []
res = []
for i in range(1,n+1):
    tmp_li.append(i)
q.extend(tmp_li)
repeat = True
while repeat:
    for r in range(k-1):
        q.popleft()
    x = q.popleft()
    tmp_li.remove(x)
    res.append(x)

    while len(q) < k:
        if len(tmp_li) == 0:
            break
        q.extend(tmp_li)
    if len(res) == n:
        repeat = False

print(str(res).replace('[','<').replace(']','>'))

