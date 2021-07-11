def solution(s):
    answer = ''
    answer += s[0].upper()
    l = len(s)
    flag = False
    for i in range(1, l):
        if s[i] == ' ':
            flag = True  # 공백 뒤에는 대문자
            answer += s[i]
        else:
            # 대문자
            if flag:
                answer += s[i].upper()
                flag = False
            else:
                answer += s[i].lower()

    return answer