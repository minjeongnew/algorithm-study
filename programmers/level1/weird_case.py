def solution(s):
    answer = ''
    s_list = s.split(' ')
    for word in s_list:
        tmp = ''
        for i in range(len(word)):
            if i%2 ==0:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        tmp += ' '
        answer += tmp
    return answer[:-1]


def solution2(s):
    return ' '.join(map(lambda x: ''.join([a.lower() if i%2 else a.upper() for i, a in enumerate(x)]), s.split(' ')))