import sys

s = int(sys.stdin.readline())
i = 0
while True:
    i += 1
    s1 = (i*(i+1))/2
    s2 = ((i+1)*(i+2))/2
    print(i, s1, s2)
    if s1 <= s <= s2:
        break
print(i)