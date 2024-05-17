import sys, io, time

f = '''14
14 26456 2 28 13228 3307 7 23149 8 6614 46298 56 4 92596
'''
sys.stdin = io.StringIO(f)

#------------------

import sys

input = sys.stdin.readline

num = int(input())

li = list(map(int, input().strip().split()))

li.sort()

print(li[0] * li[-1])