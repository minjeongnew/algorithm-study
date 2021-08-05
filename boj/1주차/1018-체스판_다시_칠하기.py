import sys

n,m = map(int, sys.stdin.readline().split())
chess = [list(input()) for _ in range(n)]
count = []
for i in range(n-7):
    for j in range(m-7):
        first_w = 0
        first_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] != 'W':
                        first_w += 1
                    if chess[k][l] != 'B':
                        first_b += 1
                else:
                    if chess[k][l] != 'B':
                        first_w += 1
                    if chess[k][l] != 'W':
                        first_b += 1
        count.append(first_w)
        count.append(first_b)

print(min(count))