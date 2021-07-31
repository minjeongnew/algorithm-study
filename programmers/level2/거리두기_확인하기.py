from collections import deque
from pprint import pprint


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(p):
    start = []
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    for s in start:
        q = deque([s])
        v = [[-1]*5 for _ in range(5)]
        i, j = s
        v[i][j] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and v[nx][ny] == -1:
                    # pprint(v)
                    if p[nx][ny] == 'O':
                        v[nx][ny] = v[x][y] + 1
                        q.append([nx, ny])
                    if p[nx][ny] == 'P' and v[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for p in places:
        answer.append(bfs(p))
    return answer


if __name__ == '__main__':
    ps = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(ps))
