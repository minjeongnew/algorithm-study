n = int(input())
txy = list(map(int, input().split()) for _ in range(n))

red = [[0]*4 for _ in range(4)]
blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]

# t == 1 -> 1x1
# t == 2 -> 1x2 ㅁㅁ
# t == 3 -> 2x1
def go_blue(t, x, y):
    if t == 1 or t == 2:
        blank_j = 0
        for j in range(6):
            if blue[x][j] == 1:
                break
            blank_j += 1
        blank_j -= 1
        blue[x][blank_j] = 1
        if t == 2:
            blue[x][blank_j-1] = 1
    elif t == 3:
        blank_j = 0
        for j in range(6):
            if blue[x][j] == 1 or blue[x+1][j] == 1:
                break
            blank_j += 1
        blank_j -= 1
        blue[x][blank_j] = 1
        blue[x+1][blank_j] = 1


def go_green(t, x, y):
    if t == 1 or t == 3:
        blank_i = 0
        for i in range(6):
            if green[i][y] == 1:
                break
            blank_i += 1
        blank_i -= 1
        green[blank_i][y] = 1
        if t == 3:
            green[blank_i-1][y] = 1
    elif t == 2:
        blank_i = 0
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            blank_i += 1
        blank_i -= 1
        green[blank_i][y] = 1
        green[blank_i][y+1] = 1
# 2~5 꽉 찼는지 확인
answer = 0
def check():
    global answer
    # blue
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if blue[i][j] == 1:
                cnt += 1
        if cnt == 4:
            blue_remove(j)
            answer += 1
    # green
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                cnt += 1
        if cnt == 4:
            green_remove(i)
            answer += 1


def blue_remove(idx):
    global blue
    for j in range(idx, -1, -1):
        if j == 0:
            for i in range(4):
                blue[i][j] = 0
            return
        for i in range(4):
            blue[i][j] = blue[i][j-1]


def green_remove(idx):
    global green
    for i in range(idx, -1, -1):
        if i == 0:
            for j in range(4):
                green[i][j] = 0
            return
        for j in range(4):
            green[i][j] = green[i-1][j]

def check_light():
    # blue
    for j in range(2):
        for i in range(4):
            if blue[i][j] == 1:
                blue_remove(5)
                break
    # green
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                green_remove(5)
                break

for t, x, y in txy:
    go_green(t, x, y)
    go_blue(t, x, y)
    check()
    check_light()

cnt = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j]:
            cnt += 1
for i in range(4):
    for j in range(2, 6):
        if blue[i][j]:
            cnt += 1
print(answer)
print(cnt)