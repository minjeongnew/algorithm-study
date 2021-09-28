import sys


n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))

d = [0]*(n+1) # for memoization
cmp = [-1000000001] # 이진 탐색을 위해 생성
max_v = 0 # 최대값 저장할 변수

def bisect_left(cmp_arr, x):
    start = 0
    end = len(cmp_arr) - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if cmp_arr[mid] >= x:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

for i in range(1, n+1):
    if cmp[-1] < a[i]:
        cmp.append(a[i])
        d[i] = len(cmp) - 1
        max_v = d[i]
    else:
        d[i] = bisect_left(cmp, a[i])
        cmp[d[i]] = a[i]

print(max_v)

