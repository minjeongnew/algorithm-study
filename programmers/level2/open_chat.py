# 내 풀이는 자료 구조에 너무 많은 접근을 하는듯
#
# 다른 사람 풀이로 생각하기
def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        # 동사가 Change가 아니라면
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]]+printer[r.split(' ')[0]])

    return answer