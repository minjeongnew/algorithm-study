def solution(genres, plays):
    genres_dict = dict()
    genres_list = []
    idx = 0
    for g, p in zip(genres, plays):
        genres_dict[g] = genres_dict.get(g, []) + [idx, p]
        idx += 1
    for g in genres_dict:
        genres_dict.sort(key=lambda x:-x[1])
        genres_list.append([g, sum(p for idx, p in genres_dict[g])])
    genres_list.sort(key=lambda x:-x[1])
    answer = []
    for g, s in genres_list:
        if len(genres_dict[g]) >= 2:
            answer.append(genres_dict[g][0][0])
            answer.append(genres_dict[g][1][0])
        else:
            answer.append(genres_dict[g][0][0])
    return answer