def solution(s):
    answer = []
    for idx in range(1, len(s)//2+1):
        result = ''
        count = 1
        tmp = s[:idx]
        for idx2 in range(idx, len(s), idx):
            if tmp == s[idx2:idx2+idx]:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tmp
                tmp = s[idx2:idx2+idx]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tmp
        answer.append(len(result))
        
    return answer


if __name__ == "__main__":
    s = "ababcdcdababcdcd"
    print(solution(s))