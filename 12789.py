import sys

repeat = int(sys.stdin.readline())


stack1 = list(map(int, sys.stdin.readline().rstrip().split()))
stack2 = []



stack1.reverse()
order = 1
possible = False
while True:
    if len(stack1) == 0 and len(stack2) == 0:
        possible = True
        break
    elif len(stack1) == 0 and stack2[-1] != order:
        possible = False
        break
    elif len(stack1) != 0 and stack1[-1] == order:
        stack1.pop()
        order += 1
    elif len(stack2) != 0 and stack2[-1] == order:
        stack2.pop()
        order += 1
    else:
        stack2.append(stack1[-1])
        stack1.pop()

if possible:
    print("Nice")
else:
    print("Sad")