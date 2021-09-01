import sys

n = int(sys.stdin.readline())
rgb = [[0]*3 for _ in range(n)]
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    if i == 0:
        rgb[0][0] = r
        rgb[0][1] = g
        rgb[0][2] = b
    else:
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + r
        rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + g
        rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + b

print(min(rgb[n-1]))
