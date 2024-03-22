import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys, math
input = sys.stdin.readline

t = int(input().strip())

def bridge(left, right):
    return int(math.factorial(right) / (math.factorial(left) * math.factorial(right-left)))

for _ in range(t):
    n, m = map(int, input().strip().split())
    print(bridge(n, m))


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")