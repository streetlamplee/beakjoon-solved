import sys
from collections import deque

inp = sys.stdin.readline
q = deque()
n = int(inp())

for r in range(n):
    tmp = list(inp().rstrip().split())
    cmd = tmp[0]
    if cmd == 'push':
        q.append(tmp[1])
    elif cmd == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) != 0:
            x = q.popleft()
            print(x)
            q.appendleft(x)
        else:
            print(-1)
    elif cmd == 'back':
        if len(q) != 0:
            x = q.pop()
            print(x)
            q.append(x)
        else:
            print(-1)

