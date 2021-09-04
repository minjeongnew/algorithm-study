n = int(input())
# 1 -> 1, 2, 3, 4, 5, 6, 7, 8, 9
# 2 -> 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98

nums = [[0]*10 for _ in range(n+1)]
nums[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    # 끝자리가 0인 경우
    nums[i][0] = nums[i-1][1]
    # 끝자리가 9인 경우
    nums[i][9] = nums[i-1][8]
    for j in range(1, 9):
        nums[i][j] = nums[i-1][j-1] + nums[i-1][j+1]

print(sum(nums[n]))