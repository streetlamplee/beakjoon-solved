import sys, io

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
#########################################
import sys
inp = sys.stdin.readline

n,k = map(int, inp().split())

items = {}
for _ in range(n):
    w, v = map(int, inp().split())
    items[w] = v


def find_item(items, k, v):
    if k == 0:
        return v
    elif min(items.keys()) > k:
        return v
    else:
        temp_w = min(items.keys())
        temp_v = v + items[min(items.keys())]
        items.pop(min(items.keys()))
        find_item(items, k- temp_w, temp_v)

print(find_item(items, k, 0))







