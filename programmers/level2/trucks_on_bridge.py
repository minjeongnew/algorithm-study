from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    t_on_b = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    cur = 0 # 현재 다리 위 트럭 무게 총합
    while t_on_b:
        answer += 1
        tmp = t_on_b.popleft()
        cur -= tmp
        if cur + truck_weights[0] <= weight:
            tmp2 = truck_weights.popleft()
            cur += tmp2
            t_on_b.append(tmp2)
        else:
            t_on_b.append(0)
    return answer


if __name__ == '__main__':
    b1, w1, t1 = 2, 10, [7,4,5,6]
    print(solution(b1, w1, t1))
    b2, w2, t2 = 100, 100, [10,10,10,10,10,10,10,10,10,10]
    print(solution(b2,w2,t2))