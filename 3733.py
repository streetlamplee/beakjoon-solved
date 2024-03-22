import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

while True:
    temp = input().strip()
    if temp == '':
        break
    n, m = map(int, temp.split())
    print(m // (n+1))



##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")