import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

res = []
for _ in range(n):
    inp = input().strip()
    res.append(inp)

for _ in range(n):
    print(res[_][::-1])

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")