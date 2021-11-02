import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

board = [[0]*n for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
mid = (n//2, n//2)
board[mid[0]][mid[1]] = 1
ax, ay = n//2, n//2 # 찾고자 하는 위치가 1인 경우


def solve():
    global ax, ay
    rng = 0
    num = 2
    x = mid[0]
    y = mid[1]
    while True:
        cnt = 0
        for k in range(4):
            if k == 0 or k == 2:
                rng += 1
            for _ in range(rng):
                nx = x + direction[k][0]
                ny = y + direction[k][1]
                board[nx][ny] = num
                x = nx
                y = ny
                if num == p:
                    ax, ay = x, y
                num += 1
                cnt += 1
                if num > n**2:
                    return
            if cnt == rng:
                cnt = 0
        if num >= n**2:
            break
solve()
for i in range(n):
    print(*board[i])
print(ax+1, ay+1)