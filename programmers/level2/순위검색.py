from itertools import combinations


def solution(info, query):
    info_dict = {}
    for i in info:
        i_list = i.split(' ')
        i_key = i_list[:-1]
        i_value = int(i_list[-1])
        for ii in range(5):
            for c in combinations(i_key, ii):
                tmp = ''.join(c)
                # 효율성 탈락
                # info_dict[tmp] = info_dict.get(tmp, []) + [i_value]
                if tmp in info_dict:
                    info_dict[tmp].append(i_value)
                else:
                    info_dict[tmp] = [i_value]
    for key in info_dict:
        info_dict[key].sort()

    answer = []
    for q in query:
        q_list = q.split(" ")
        q_key = q_list[:-1]
        q_value = int(q_list[-1])
        while "and" in q_key:
            q_key.remove("and")
        while "-" in q_key:
            q_key.remove("-")
        q_key = ''.join(q_key)
        if q_key in info_dict:
            scores = info_dict[q_key]
            lt, rt = 0, len(scores)-1
            while lt <= rt:
                mid = (lt+rt) // 2
                if scores[mid] >= q_value:
                    rt = mid -1
                else:
                    lt = mid + 1
            answer.append(len(scores)-lt)
        else:
            answer.append(0)
    return answer




