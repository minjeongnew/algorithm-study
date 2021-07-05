def solution(arr):
    return [x for x in arr if x > min(arr)] or [-1]