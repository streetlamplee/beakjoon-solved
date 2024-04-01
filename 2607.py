import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = list(input().strip())
    globals()[f"word_{_}"] = {}
    for i in word:
        if i not in globals()[f"word_{_}"].keys():
            globals()[f"word_{_}"][i] = word.count(i)
        else:
            pass
    globals()[f"word_{_}"]=sorted(globals()[f"word_{_}"].items(), key = lambda x : x[0])

res = 0

for _ in range(n):
    print(globals()[f"word_{_}"])
print("----------------------------------------------------------------")

for j in range(1,n):
    origin = word_0
    alter = globals()[f"word_{j}"]
    same = []
    differ_o = []
    differ_a = []
    for k in alter:
        if k not in origin:
            differ_a.append(k)
        else:
            same.append(k)
    for l in origin:
        if l not in same:
            differ_o.append(l)
    
    print(same)
    print(differ_o)
    print(differ_a)
    print("----------------------------------------------------------------")

    if len(differ_a) == 0 and len(differ_o) == 0:
        res += 1
    elif len(differ_o) == 1 and differ_a[0][0] == differ_o[0][0] and (abs(differ_a[0][1] - differ_o[0][1]) == 1):
        res += 1
    elif len(differ_o) == 1 and differ_a[0][0] != differ_o[0][0] and differ_a[0][1] == differ_o[0][1] == 1:
        res += 1
    else:
        continue

            


print(res)
    
    
    








##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")