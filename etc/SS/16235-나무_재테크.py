import sys
from collections import deque

n, m, kk = map(int, sys.stdin.readline().split())
a = [[5]*n for _ in range(n)]
values = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = {}
for i in range(n):
    for j in range(n):
        trees[(i, j)] = deque()
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[(x-1, y-1)].append(z)

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def solve(): # 1년
    # 봄
    for i in range(n):
        for j in range(n):
            if trees[(i, j)]:
                survive = deque()
                sumv = 0
                for tree in trees[(i, j)]:
                    if tree <= a[i][j]:
                        a[i][j] -= tree
                        survive.append(tree+1)
                    else:
                        sumv += (tree//2)
                trees[(i, j)] = survive
                a[i][j] += sumv # 여름
    # 가을
    for i in range(n):
        for j in range(n):
            if trees[(i, j)]:
                # 5의 배수인지
                for tree in trees[(i, j)]:
                    if tree % 5 == 0:
                        for k in range(8):
                            ni = i + d[k][0]
                            nj = j + d[k][1]
                            if 0 <= ni < n and 0 <= nj < n:
                                trees[(ni, nj)].appendleft(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            a[i][j] += values[i][j]
    # print(trees)
for _ in range(kk):
    solve()
answer = 0
for tree_v in trees.values():
    answer += len(tree_v)
print(answer)