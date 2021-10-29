import sys

n = int(sys.stdin.readline())
fs = list(map(int, sys.stdin.readline().split()))
fs = sorted(fs)
left = 0
right = n-1
al = left
ar = right
answer = fs[left] + fs[right]
while left < right:
    tmp = fs[left] + fs[right]
    if abs(tmp) < abs(answer):
        answer = abs(tmp)
        al = left
        ar = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(fs[al], fs[ar])