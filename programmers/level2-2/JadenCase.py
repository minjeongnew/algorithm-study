def solution(s):
    answer = s[0].upper()
    flag = False
    for i in range(1, len(s)):
        if s[i] == ' ':
            flag = True
            answer += s[i]
        else:
            if flag:
                answer += s[i].upper()
                flag = False
            else:
                answer += s[i].lower()
    return answer