import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

from datetime import datetime, timedelta
import sys

input = sys.stdin.readline

y, m, d = map(int, input().strip().split())
yy, mm, dd = map(int, input().strip().split())

time1 = datetime(y, m, d,0,0,0,0)
time2 = datetime(yy,mm,dd,0,0,0,0)

res = (time2-time1).days
if yy-y == 1000 and mm >= m and dd >= d:
    print('gg')
elif yy-y >= 1001:
    print('gg')
else:
    print(f"D-{res}")




##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")