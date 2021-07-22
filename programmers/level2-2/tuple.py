def solution(s):
    tmp = s[2:-2].split('},{')
    s_list = []
    for x in tmp:
        s_list.append(x.split(','))
    s_list.sort(key=len)
    return [int(n) for n in s_list[-1]]


if __name__ == '__main__':
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))