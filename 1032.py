import sys, io, time

f = '''3
config.sys
config.inf
configures
'''
sys.stdin = io.StringIO(f)

import sys

input=sys.stdin.readline

n = int(input())
tmp_li = []
for _ in range(n):
    tmp_li.append(input().strip())

res = ''

for idx in range(len(tmp_li[0])):
    tmp = list(map(lambda x: x[idx], tmp_li))
    test = True
    for i in range(len(tmp)-1):
        if tmp[i] == tmp[i+1]:
            pass
        else:
            test = False
            break
    if test:
        res += tmp[0]
    else:
        res += '?'
print(res)