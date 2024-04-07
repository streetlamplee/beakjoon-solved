import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys

input = sys.stdin.readline

n = int(input().strip())

li = list(map(int, input().strip().split()))

res = list()
for i in range(len(li)-1, -1, -1):
    
    if li[i] == 0:
        left = []
        right = res
    else:
        left = res[0:li[i]]
        right = res[li[i]:]
    
    left.append(i+1)
    left.extend(right)
    res = left

print(*res)




##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")