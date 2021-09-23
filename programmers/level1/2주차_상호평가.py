def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    n = len(scores)
    for i in range(n):
        pivot = scores[i][i]
        tmp = [scores[x][i] for x in range(n)]
        avg = 0
        if min(tmp) == pivot and tmp.count(pivot) == 1:
            avg = (sum(tmp)-pivot) / (n-1)
        elif max(tmp) == pivot and tmp.count(pivot) == 1:
            avg = (sum(tmp) - pivot) / (n - 1)
        else:
            avg = sum(tmp) / n
        answer += grade(avg)
    return answer
