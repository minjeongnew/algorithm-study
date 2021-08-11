def solution(s):
    length = []
    result = ""
    for cut in range(1, len(s)//2+1):
        count = 1
        tmp = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tmp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tmp
                tmp = s[i:i+cut]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tmp
        length.append(len(result))
        result = ""
    return min(length)


import re


def solution2(s):
    if len(s) <= 2:
        return len(s)
    answer = []
    for i in range(1, len(s)//2 + 1):
        re_list = re.sub('(\w{%i})'%i, '\g<1> ', s).split()
        # print(relist)
        result = []
        count = 1
        for j in range(len(re_list)):
            if j < len(re_list)-1 and re_list[j] == re_list[j+1]:
                count += 1
            else:
                if count == 1:
                    result.append(re_list[j])
                else:
                    result.append(str(count) + re_list[j])
                    count = 1
        answer.append(len(''.join(result)))
    return min(answer)


if __name__ == "__main__":
    s = "abcabcabcabcdededededede"
    print(solution2(s))