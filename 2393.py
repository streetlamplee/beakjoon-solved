import sys, io, time

with open("input.txt", "r") as f:
    sys.stdin = io.StringIO(f.read())
start = time.time()
#########################################

print('''  ___  ___  ___
  | |__| |__| |
  |           |
   \\_________/
    \\_______/
     |     |
     |     |
     |     |
     |     |
     |_____|
  __/       \\__
 /             \\
/_______________\\''')
##########################################
end = time.time()
print(f"time : {end - start:.5f} sec")