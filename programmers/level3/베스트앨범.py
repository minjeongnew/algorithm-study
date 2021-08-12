def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    idx = 0
    for g, p in zip(genres, plays):
        genres_dict[g] = genres_dict.get(g, []) + [[idx, p]]
        idx += 1
    for g in genres_dict:
        genres_dict[g].sort(key=lambda x:-x[1])
        genres_list.append([g, sum([play for idx, play in genres_dict[g]])])

    genres_list.sort(key=lambda x:-x[1])
    answer = []
    for g, _ in genres_list:
        answer.extend(x[0] for x in genres_dict[g][:2])
    return answer


if __name__ == "__main__":
    g, p = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    print(solution(g, p))