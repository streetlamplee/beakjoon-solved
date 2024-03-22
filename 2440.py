import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

num = int(input().strip())

for i in range(num,0,-1):
    print("*"*i)


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")