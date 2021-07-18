from collections import deque


def solution(maps):
    l1 = len(maps)
    l2 = len(maps[1])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    v = [[-1] * l2 for _ in range(l1)]
    q = deque()
    q.append((0, 0))
    v[0][0] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < l1 and 0 <= ny < l2 and maps[nx][ny] == 1:
                if v[nx][ny] == -1:
                    v[nx][ny] = v[cx][cy] + 1
                    q.append((nx, ny))
    return v[-1][-1]


if __name__ == '__main__':
    a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(a))