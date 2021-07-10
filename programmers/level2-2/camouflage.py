def solution(clothes):
    c = {}
    for cl in clothes:
        if cl[1] in c.keys():
            c[cl[1]] += 1
        else:
            c[cl[1]] = 1

    answer = 1
    for v in c.values():
        answer *= (v+1)

    return answer - 1



if __name__ == '__main__':
    c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(c))
    c = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(c))