import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################
import sys
inp = sys.stdin.readline

n = int(inp().strip())
num_li = []

for _ in range(n):
    num_li.append(int(inp().strip()))
    num_li.sort()

    if _ % 2 == 1:
        print(num_li[_ // 2])
    if _ % 2 == 0:
        print(num_li[_ // 2])


##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")