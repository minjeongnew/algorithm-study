from collections import Counter
from itertools import combinations
from pprint import pprint


def solution(orders, course):
    answer = []
    for c in course:
        order_combinations = []
        for order in orders:
            combi = combinations(sorted(order), c)
            order_combinations += combi
        o_dict = Counter(order_combinations)
        # pprint(o_dict)
        if o_dict:
            max_ = max(list(o_dict.values()))
            # print(max_)
            if max_ >= 2:
                for key, value in o_dict.items():
                    if o_dict[key] >= max_:
                        answer.append(''.join(key))
    return sorted(answer)


if __name__ == '__main__':
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]
    print(solution(orders, course))