import sys
n = int(sys.stdin.readline())
x_li = list(map(int,sys.stdin.readline().rstrip().split(' ')))
unq_li = list(set(x_li))


def merge_sort(list):
    if len(list) <2:
        return list

    mid = len(list) //2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr


sorted_li = merge_sort(x_li)
tmp = dict()
res = []
k = 0
for idx, v in enumerate(sorted_li):
    if v not in tmp.keys():
        tmp[v] = k
        k += 1
    else:
        pass

for v in x_li:
    res.append(tmp[v])

print(*res)