import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline
a,b,c,d,e = map(int, input().strip().split())
print( (a**2 + b**2 + c**2 + d**2 + e**2) % 10)

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")