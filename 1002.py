import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().strip().split())
    distance = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**(1/2)
    sum_r = r_1 + r_2
    diff_r = abs(r_1 - r_2)
    if distance == 0 and r_1 == r_2:
        print(-1)
    elif distance == 0 and r_1 != r_2:
        print(0)
    elif diff_r == distance or sum_r == distance:
        print(1)
    elif r_1 < distance and r_2 < distance:
        if sum_r < distance:
            print(0)
        elif sum_r > distance:
            print(2)
    elif r_1 > distance or r_2 > distance:
        if diff_r > distance:
            print(0)
        elif diff_r < distance:
            print(2)
    

##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")