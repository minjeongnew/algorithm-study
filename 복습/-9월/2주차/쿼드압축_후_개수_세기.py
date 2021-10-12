answer = [0, 0]


def calc(arr, x, y, n):
    init = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != init:
                nn = n // 2
                calc(arr, x, y, nn)
                calc(arr, x, y+nn, nn)
                calc(arr, x+nn, y, nn)
                calc(arr, x+nn, y+nn, nn)
                return
    answer[init] += 1


def solution(arr):
    calc(arr, 0, 0, len(arr))
    return answer


if __name__ == "__main__":
    a = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(solution(a))