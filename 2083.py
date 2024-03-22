import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

while True:
    name, age, weight = input().strip().split()
    if name == '#':
        break
    age = int(age)
    weight = int(weight)

    if age > 17 or weight >= 80:
        res = 'Senior'
    else:
        res = 'Junior'
    
    print(f"{name} {res}")

        


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")