import sys

n, c = map(int, sys.stdin.readline().split())
house = list(int(sys.stdin.readline()) for _ in range(n))
house.sort()

def router_count(distance):
    cnt = 1
    cur_house = house[0]
    for i in range(1, n):
        if cur_house + distance <= house[i]:
            cnt += 1
            cur_house = house[i]
    return cnt

answer = 0
start = house[0]
end = house[-1] - house[0]
while start <= end:
    mid = (start+end) // 2
    print(mid, router_count(mid))
    if router_count(mid) >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)