import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys, math
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dict = []
for _ in range(n):
    a, b = input().strip().split()
    dict.append([a, int(b)])

for _ in range(m):
    left, right = 0, n-1
    target = int(input())
    while (left <= right):  
        mid = (left + right) // 2
        if left == right:
            print(dict[mid][0])
            break
        
        if target > dict[mid][1]:
            left = mid +1 
        elif target <= dict[mid][1]:
            right = mid
        


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")