k, n = map(int, input().split())
lans = list(int(input()) for _ in range(k))
lt, rt = 1, max(lans)
while lt <= rt:
    mid = (lt+rt) // 2
    answer = 0
    for lan in lans:
        answer += lan // mid
    if answer >= n:
        lt = mid + 1
    elif answer < n:
        rt = mid - 1

print(rt)