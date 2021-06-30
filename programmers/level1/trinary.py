def reverse_trinary(n):
    ans = ''
    while n>0:
        ans += str(n%3)
        n//=3
    return ans


def trinary_to_decimal(n):
    ans = 0
    i = len(n) -1
    j = 0
    while j < len(n):
        ans += (3**i)*(int(n[j]))
        j+=1
        i-=1
    return ans

def solution(n):
    answer = trinary_to_decimal(reverse_trinary(n))

    return answer