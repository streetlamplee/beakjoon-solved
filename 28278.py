import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    req = list(map(int, sys.stdin.readline().rstrip().split()))
    if req[0] == 1:
        stack.append(req[1])
    elif req[0] == 2:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif req[0] == 3:
        print(len(stack))
    elif req[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif req[0] == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
