def solution(dirs):
    dd = {'U':(0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    ans = set()
    cx, cy = (0, 0)
    for d in dirs:
        nx, ny = cx + dd[d][0], cy+ dd[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            ans.add((cx, cy, nx, ny))
            ans.add((nx, ny, cx, cy))
            cx, cy = nx, ny
    return len(ans) // 2