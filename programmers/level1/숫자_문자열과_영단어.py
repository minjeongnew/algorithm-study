def solution(s):
    answer = ''
    n_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n_dic = dict()
    for i in range(10):
        n_dic[n_list[i]] = str(i)
    word = ''
    for i in range(len(s)):
        if s[i].isdecimal():
            answer += s[i]
        else:
            word += s[i]
            if word in n_dic:
                answer += n_dic[word]
                word = ''
    return int(answer)


def solution2(s):
    n_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = s
    for i in range(10):
        answer = answer.replace(n_list[i], str(i))
    return answer


if __name__ == '__main__':
    s = "2three45sixseven"
    print(solution2(s))