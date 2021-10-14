import sys


def solve(n, l, arr):
    slopes = [False] * n
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            continue
        elif abs(arr[i] - arr[i+1]) > 1:
            return False
        if arr[i] > arr[i+1]:
            tmp = arr[i+1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if arr[j] != tmp:
                        return False
                    if slopes[j]:
                        return False
                    slopes[j] = True
                else:
                    return False
        else:
            tmp = arr[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if arr[j] != tmp:
                        return False
                    if slopes[j]:
                        return False
                    slopes[j] = True
                else:
                    return False
    return True


n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    if solve(n, l, graph[i]):
        cnt += 1
for i in range(n):
    tmp = [graph[j][i] for j in range(n)]
    if solve(n, l, tmp):
        cnt += 1
print(cnt)