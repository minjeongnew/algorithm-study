def solution(arr):
    l = len(arr)
    answer = [arr[0]]
    for i in range(1, l):
        if arr[i-1] == arr[i]: continue
        else:
            answer.append(arr[i])
    return answer