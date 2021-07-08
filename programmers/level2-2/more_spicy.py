import heapq as hq


def mix(m1, m2):
    return m1 + m2*2


def solution(scoville, k):
    answer = 0
    hq.heapify(scoville)
    while True:
        m1 = hq.heappop(scoville)
        if m1 >= k:
            return answer
        if len(scoville) == 0:
            return -1

        m2 = hq.heappop(scoville)
        hq.heappush(scoville, mix(m1, m2))
        answer += 1
    return answer