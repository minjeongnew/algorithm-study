import sys

n, c = map(int, sys.stdin.readline().split())
house = list(int(sys.stdin.readline()) for _ in range(n))
house.sort()
start = 1
end = house[-1] - house[0]


def router_counter(distance):
    count = 1
    cur_house = house[0] # 시작점
    for i in range(1, n):
        if cur_house + distance <= house[i]:
            count += 1
            cur_house = house[i]
    return count

answer = 0
while start <= end:
    mid = (start+end) // 2
    # print('mid', mid)
    # print('count:', router_counter(mid))
    if router_counter(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
