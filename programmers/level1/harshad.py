def solution(x):
    return True if x%sum(map(int, list(str(x)))) ==0 else False