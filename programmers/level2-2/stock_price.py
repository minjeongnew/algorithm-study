def solution(prices):
    s = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                s[i] += 1
                break
            else:
                s[i] += 1

    return s


if __name__ == '__main__':
    p = [1, 2, 3, 2, 3]
    print(solution(p))