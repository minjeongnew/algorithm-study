from pprint import pprint
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int, input().split())) for _ in range(m)]


directions = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
cross = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
cloud_board = [[0]*n for _ in range(n)]
cloud_board[n-2][0] = 1
cloud_board[n-2][1] = 1
cloud_board[n-1][0] = 1
cloud_board[n-1][1] = 1

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]
def go(d, s):
    global clouds
    new_cloud = []
    for cloud in clouds:
        cx = (cloud[0] + directions[d][0]*s) % n
        cy = (cloud[1] + directions[d][1]*s) % n
        cloud_board[cx][cy] = 1
        cloud_board[cloud[0]][cloud[1]] = 0
        board[cx][cy] += 1
        new_cloud.append([cx, cy])
    for cloud in new_cloud:
        tmp = 0
        for k in range(4):
            nx = cloud[0] + cross[k][0]
            ny = cloud[1] + cross[k][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                tmp += 1
        board[cloud[0]][cloud[1]] += tmp
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and [i, j] not in new_cloud:
                cloud_board[i][j] = 1
                board[i][j] -= 2
                new_clouds.append([i, j])
    for cloud in clouds:
        cloud_board[cloud[0]][cloud[1]] = 0
    clouds = new_clouds


for d, s in ds:
    go(d, s)
answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            answer += board[i][j]
print(answer)