# 골드5

import sys
from pprint import pprint
import heapq


n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    if not answer:
        for num in nums:
            heapq.heappush(answer, num)
    else:
        for num in nums:
            if answer[0] < num:
                heapq.heappush(answer, num)
                heapq.heappop(answer)
print(answer[0])

# print(pivot)





