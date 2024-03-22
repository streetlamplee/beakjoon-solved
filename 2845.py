import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

L, P = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
for i,v in enumerate(li):
    li[i] = v - (L*P)
print(*li)


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")