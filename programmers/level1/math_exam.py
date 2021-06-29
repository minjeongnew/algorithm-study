def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    r = [0,0,0]

    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    for idx in range(len(answers)):
        # 순환 주기를 체크
        if s1[idx%l1] == answers[idx]:
            r[0] += 1
        if s2[idx % l2] == answers[idx]:
            r[1] += 1
        if s3[idx % l3] == answers[idx]:
            r[2] += 1

    ans = []
    for idx, v in enumerate(r):
        ans.append([idx+1,v])

    ans.sort(key=lambda x:x[1]) # value값에 대해서 정렬함
    # 가장 큰 value
    max_v = ans[-1][1]
    res = [x[0]+1 for x in ans if x[1] == max_v]

    return res