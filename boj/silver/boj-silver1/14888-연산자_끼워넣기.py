import sys
# sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())


def solve(a, idx, add, sub, multi, div, sum_):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, sum_)
        min_ans = min(min_ans, sum_)
        return
    else:
        if add:
            solve(a, idx+1, add-1, sub, multi, div, sum_+a[idx])
        if sub:
            solve(a, idx+1, add, sub-1, multi, div, sum_-a[idx])
        if multi:
            solve(a, idx+1, add, sub, multi-1, div, sum_*a[idx])
        if div:
            solve(a, idx+1, add, sub, multi, div-1, int(sum_/a[idx]))


max_ans = -sys.maxsize + 1
min_ans = sys.maxsize
a = list(map(int, sys.stdin.readline().split()))
add, sub, multi, div = map(int, sys.stdin.readline().split())
solve(a, 1, add, sub, multi, div, a[0])
print(max_ans)
print(min_ans)