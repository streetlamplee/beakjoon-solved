import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

while True:
    sen = input().strip()
    if sen == '#':
        break
    sen = sen.lower()
    target = ['a','e','i','o','u']
    res = 0
    for i in sen:
        if i in target:
            res += 1
        else:
            continue
    print(res)
    
        


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")