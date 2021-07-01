def solution(d, budget):
    answer = 0
    d.sort() # 부서 별 예산을 정렬 -> 최대한 많은 부서에게 예산을 나눠주는 것을 목표로 함
    for idx in range(len(d)):
        if d[idx] <= budget:
            answer+=1
            budget-=d[idx]
        else:
            break
    return answer