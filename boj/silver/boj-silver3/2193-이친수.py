n = int(input())

# 1 - 1
# 2 - 1
# 3 - 2
# 4 - 3
# 5 - 5
a, b = 1, 1
for i in range(1, n):
    a, b = b, a+b
print(a)

# 시간 초과 코드
# cnt = 0
# def solve(idx, ans):
#     global cnt
#     if idx == n-1:
#         cnt += 1
#         return
#     if ans[-1] != "1":
#         solve(idx + 1, ans + "1")
#     solve(idx+1, ans+"0")
#
#
# solve(0, "1")
# print(cnt)