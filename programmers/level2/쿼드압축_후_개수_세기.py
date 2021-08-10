answer = [0, 0]


def count(arr, x, y, n):
    init = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != init:
                nn = n // 2
                count(arr, x, y, nn)
                count(arr, x, y+nn, nn)
                count(arr, x+nn, y, nn)
                count(arr, x+nn, y+nn, nn)
                return
    answer[init] += 1


def solution(arr):
    n = len(arr)
    count(arr, 0, 0, n)
    return answer


if __name__ == '__main__':
    a = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(a))