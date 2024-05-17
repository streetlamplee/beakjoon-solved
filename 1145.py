# 1145
import sys, io, time

f = '''30 42 70 35 90
'''
sys.stdin = io.StringIO(f)

#------------------
import sys
input = sys.stdin.readline
li = list(map(int, input().strip().split()))
li.sort()
num = li[0]
while True:
    num += 1
    tmp = list(map(lambda x:num % x, li))
    if tmp.count(0) >= 3:
        break
    else:
        continue
print(num)