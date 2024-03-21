import sys

inp = sys.stdin.readline

while True:
    sentence = inp().rstrip()
    if sentence =='.':
        break

    tmpli = list(sentence)
    for i,v in enumerate(tmpli):
        if v == '(':
            for j in range(len(tmpli)-1,-1,-1):
                if tmpli[j] == ')':
                    del tmpli[j]
                    del tmpli[i]
                elif tmpli[j] == ']':
                    print('no')
                    break
        elif v == '[':
            for j in range(len(tmpli)-1,-1,-1):
                if tmpli[j] == ']':
                    del tmpli[j]
                    del tmpli[i]
                elif tmpli[j] == ')':
                    print('no')
                    break
    
    print('yes')