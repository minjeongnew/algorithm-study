def solution(num):
    answer = 0
    n = 500
    while n > 500:
        if num == 1:
            return answer
        if num%2 == 0:
            num//=2
            answer+=1
        else:
            num = num+3 +1
            answer+=1
        n-=1
    return -1