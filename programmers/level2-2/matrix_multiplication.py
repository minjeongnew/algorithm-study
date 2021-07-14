def solution(arr1, arr2):
    answer = []
    l1 = len(arr1)
    l2 = len(arr1[0])
    l3 = len(arr2[0])
    for i in range(l1):
        tmp = []
        for j in range(l3):
            ans = 0
            for k in range(l2):
                ans += arr1[i][k] * arr2[k][j]
            tmp.append(ans)
        answer.append(tmp)
    return answer


if __name__ == '__main__':
    a1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    a2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(solution(a1, a2))