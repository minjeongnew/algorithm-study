def solution(s):
    s = sorted(s[2:-2].split('},{'), key=len)
    answer = []
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))

    return answer


if __name__ == '__main__':
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution(s))
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))