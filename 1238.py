import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

n, m, x = map(int, input().strip().split())

roadmap = dict()
for _ in range(m):
    start, end, t = map(int, input().strip().split())
    if start not in roadmap.keys():
        roadmap[start] = [(end,t)]
    else:
        roadmap[start].append((end,t))

print(roadmap)




##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")