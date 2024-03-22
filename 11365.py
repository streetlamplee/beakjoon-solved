import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

while True:
    sen = input().strip()
    if sen == 'END':
        break
    print(sen[::-1])

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")