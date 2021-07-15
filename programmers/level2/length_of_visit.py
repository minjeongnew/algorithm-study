def solution(dirs):
    v = set()
    dd = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    cx, cy = (0, 0)
    for d in dirs:
        nx, ny = cx + dd[d][0] + dd[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            v.add((cx, cy, nx, ny))
            v.add((nx, ny, cx, cy))
    return len(v) // 2
