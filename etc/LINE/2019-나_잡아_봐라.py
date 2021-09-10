# 코드 스니펫
from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    q = deque()
    q.append([brown_loc, 0])
    v = [set() for _ in range(200001)]
    while cony_loc <= 200000:
        cony_loc += time
        # print(v[cony_loc])
        if time in v[cony_loc]:
            return time

        for _ in range(len(q)):
            current_brown_position, current_time = q.popleft()
            # print(current_brown_position)
            new_time = current_time + 1
            new_brown_position = current_brown_position - 1
            if 0 <= new_brown_position <= 200000:
                v[new_brown_position].add(new_time)
                q.append([new_brown_position, new_time])
            new_brown_position = current_brown_position + 1
            if 0 <= new_brown_position <= 200000:
                v[new_brown_position].add(new_time)
                q.append([new_brown_position, new_time])
            new_brown_position = current_brown_position * 2
            if 0 <= new_brown_position <= 200000:
                v[new_brown_position].add(new_time)
                q.append([new_brown_position, new_time])
            # print("-", _, time)
        # print(-9)
        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!