def solution(gems):
    answer = []
    gems_num = len(set(gems))
    gems_dict = dict()
    start, end = 0, 0
    shortest = len(gems) + 1
    while end < len(gems):
        gems_dict[gems[end]] = gems_dict.get(gems[end], 0) + 1
        end += 1
        if len(gems_dict) == gems_num:
            while start < end:
                if gems_dict[gems[start]] > 1:
                    gems_dict[gems[start]] -= 1
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
    print(solution(g))