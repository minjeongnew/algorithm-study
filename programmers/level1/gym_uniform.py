def solution(n, lost, reserve):
    # lost 이면서 reserve인 경우 제외하기
    reserve2 = [i for i in reserve if i not in lost]
    lost2 = [j for j in lost if j not in reserve]

    answer = n - len(lost2)
    # 앞에서 빌려준 학생
    b = []
    for i in lost2:
        for j in reserve2:
            if j not in b and i in [j-1, j+1]:
                answer +=1
                b.append(i)
                break

    return answer