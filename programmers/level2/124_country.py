def solution(n):
    answer = ''
    while n>0:
        remain = n%3
        if remain == 0:
            answer += '4'
            n-=1
        else:
            answer += '124'[n%3-1]
        n//=3
    return answer