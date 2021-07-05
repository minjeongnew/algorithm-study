def solution(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divs.append(i)
            divs.append(n//i)
    return sum(set(divs))