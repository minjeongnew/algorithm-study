import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))


def bs(x):
    lt = 0
    rt = len(a) - 1
    while lt <= rt:
        mid = (lt+rt) // 2
        if a[mid] == x:
            return 1
        elif a[mid] > x:
            rt = mid - 1
        else:
            lt = mid + 1

    return 0


for elem_b in b:
    print(bs(elem_b))

