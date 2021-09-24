def solution(s):
    answer = []
    s = sorted(s[2:-2].split("},{"), key=len)
    for x in s:
        x = x.split(",")
        if not answer:
            answer.append(int(x[0]))
        for i in x:
            if int(i) not in answer:
                answer.append(int(i))
    return answer


if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))