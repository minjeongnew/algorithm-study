from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    t_on_b = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    cur = 0 # 다리 위 현재 트럭 무게 총합
    while t_on_b:
        answer += 1
        old_truck = t_on_b.popleft() # 다리에서 나갈 트럭 또는 그냥 0
        cur -= old_truck
        if cur + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            cur += new_truck
            t_on_b.append(new_truck)
        else:
            t_on_b.append(0)
    return answer


if __name__ == '__main__':
    b1, w1, t1 = 2, 10, [7,4,5,6]
    print(solution(b1, w1, t1))
    b2, w2, t2 = 100, 100, [10,10,10,10,10,10,10,10,10,10]
    print(solution(b2,w2,t2))