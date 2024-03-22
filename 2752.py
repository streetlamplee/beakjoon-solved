import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

li = list(map(int, input().strip().split()))

li.sort()

print(*li)
        


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")