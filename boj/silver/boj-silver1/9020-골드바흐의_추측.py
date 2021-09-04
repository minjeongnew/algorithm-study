import math

n = int(input())
nums = [int(input()) for _ in range(n)]
max_num = max(nums)
primes = [False, False] + [True] * max_num

for i in range(2, int(math.sqrt(max_num))+1):
    for j in range(i+i, max_num, i):
        primes[j] = False
for num in nums:
    g = num
    mid = g // 2
    for i in range(2, mid+1):
        if primes[mid] and primes[g-mid]:
            print(mid, g-mid)
            break
        mid -= 1