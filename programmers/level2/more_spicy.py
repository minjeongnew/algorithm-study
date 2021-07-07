import heapq


def mix(min1, min2):
    return min1 + min2*2

def check(arr, k):
    if arr[0] > k:
        return True
    return False

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    l = len(scoville)

    if scoville[0] >= k:
        return answer
    for i in range(l-1):
        if check(scoville, k):
            return answer
        else:
            m1 = heapq.heappop(scoville)
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, mix(m1, m2))
            answer+=1

    if check(scoville, k): # [1,1,100],k=7
        return answer
    if len(scoville) > 0:
        return -1


# 다른사람풀이
def solution2(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= k:
            break
        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, mix(first, second))
        answer += 1

    return answer