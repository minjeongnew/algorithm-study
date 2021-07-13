def solution(arr1, arr2): # nxc * cxm
    l1 = len(arr1)  # n
    l2 = len(arr1[0]) # m
    l3 = len(arr2[0]) # c
    answer = []
    for i in range(l1):
        tmp = []
        for j in range(l2):
            ans = 0
            for k in range(l3):
                ans += (arr1[i][k]* arr2[k][j])
            tmp.append(ans)
        answer.append(tmp)
    return answer


import numpy as np


def solution2(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)

    return a.dot(b).tolist()


if __name__ == '__main__':
    a = [[2, 3, 2],
         [4, 2, 4],
         [3, 1,4]]
    b = [[5, 4, 3],
         [2, 4, 1],
         [3, 1, 1]]
    print(solution(a, b))
    print(solution2(a, b))