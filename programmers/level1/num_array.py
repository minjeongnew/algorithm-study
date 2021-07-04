def solution(arr, divisor):
    answer = []
    for x in arr:
        if x%divisor == 0:
            answer.append(x)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)


## 다른 풀이
def solution2(arr, divisor):
    return sorted([x for x in arr if x%divisor == 0] or [-1])