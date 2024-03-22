import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys

input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())

print(f"{a+b}\n{a-b}\n{a*b}")

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")