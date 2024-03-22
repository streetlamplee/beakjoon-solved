import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

res = ''

for i in input().strip():
    if i.islower():
        res = res + i.upper()
    else:
        res = res + i.lower()
    
print(res)
        


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")