import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

jh = input().strip()
doctor = input().strip()

if len(jh) >= len(doctor):
    print('go')
else:
    print('no')



##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")