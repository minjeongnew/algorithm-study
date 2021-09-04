# n개의 퀸을 배치 -> 무조건 모든 행에 퀸이 위치해야 함
# 0열 ~ n-1열까지
# 유망한지(promising)한지, 즉 이전의 열로 인해 영향을 받는지 검사하는 함수를 추가한다
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x+1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)