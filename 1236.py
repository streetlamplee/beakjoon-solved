# 1236
import sys, io, time

f = '''5 8
....XXXX
........
XX.X.XX.
........
........
'''
sys.stdin = io.StringIO(f)

#------------------
import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
castle = []
for _ in range(n):
    castle.append(list(input().strip()))
row_res = 0
col_res = 0
for row in range(n):
    if 'X' not in castle[row]:
        row_res += 1
    else:
        continue
for col in range(m):
    if 'X' not in list(map(lambda x: x[col], castle)):
        col_res += 1
    else:
        continue
print(max(row_res, col_res))

