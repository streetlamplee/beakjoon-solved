import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

young = int(input().strip())
mid = int(input().strip())

print(mid + (mid- young))

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")