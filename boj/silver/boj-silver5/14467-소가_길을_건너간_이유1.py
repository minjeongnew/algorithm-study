import sys

n = int(sys.stdin.readline())
cows = {}
cows_list = [0]*n
for _ in range(n):
    idx, pos = map(int, sys.stdin.readline().split())
    if idx not in cows:
        cows[idx] = pos
    else:
        if cows[idx] != pos:
            cows_list[idx] += 1
            cows[idx] = pos

print(sum(cows_list))