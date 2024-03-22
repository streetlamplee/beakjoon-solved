import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

target = int(input().strip())

bar_li = [64,32,16,8,4,2,1]
res = 0
for bar in bar_li:
    if target >= bar:
        target -= bar
        res += 1
    if target == 0:
        break
print(res)



##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")