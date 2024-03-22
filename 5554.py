import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

total = a + b + c + d

min = total // 60
sec = total % 60

print(min)
print(sec)

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")