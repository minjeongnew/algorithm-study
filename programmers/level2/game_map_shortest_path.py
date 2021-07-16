from collections import deque


def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    r = len(maps)
    c = len(maps[0])
    q = deque()
    q.append([0, 0])
    v = [[-1]*c for _ in range(r)]
    v[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                if v[nx][ny] == -1:
                    v[nx][ny] = v[x][y] + 1
                    q.append([nx, ny])
    return v[-1][-1]





if __name__ == '__main__':
    m = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(m))