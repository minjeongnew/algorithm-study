def solution(gems):
    answer = [0, 100001]
    start, end = 0, 0
    gem_num = len(set(gems))
    gem_dict = {gems[0]:1}

    while start < len(gems) and end < len(gems):
        if len(gem_dict) < gem_num:
            if end == len(gems) - 1:
                break
            end += 1
            if gems[end] in gem_dict:
                gem_dict[gems[end]] += 1
            else:
                gem_dict[gems[end]] = 1
        else:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            print(start, end)
            print(gem_dict)
            start += 1
    return answer


def solution2(gems):
    answer = []
    # '현재' 최단 구간 거리
    shortest = len(gems) + 1
    start, end = 0, 0
    gem_num = len(set(gems))
    gem_dict = {}
    while end < len(gems):
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1
        end += 1
        if len(gem_dict) == gem_num:
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
    return answer


if __name__ == '__main__':
    g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution2(g))