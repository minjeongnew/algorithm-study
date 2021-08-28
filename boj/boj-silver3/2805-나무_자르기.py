import sys


n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
lt = 0
rt = max(trees)
while lt <= rt:
    h = (lt + rt) // 2
    # 내장함수 sum은 c로 구현되어 있어 for 문을 사용해 일일이 더하는 것보다 빠르다
    answer = sum(tree-h for tree in trees if tree > h)

    if answer >= m:
        lt = h + 1
    else:
        rt = h - 1
print(rt)