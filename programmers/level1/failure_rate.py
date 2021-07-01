def solution(n, stages):
    answer = []
    l = len(stages)
    stages.sort()
    for stage_num in n:
        clear = 0
        for p in stages:
            if p == stage_num:
                clear += 0
        if l != 0:
            answer.append([stage_num+1, clear/l])
        else: # 0으로 나누면 런타임에러 발생
            answer.append([stage_num+1, 0])
        l-=clear
    answer.sort(key=lambda x: x[1], reverse=True)
    ans = [x[0] for x in answer]
    return ans

# 다른 사람 풀이 중 answer를 처리하는 방법
# answer = {}
# result[stage] = clear/ l
# return sorted(answer, key=lambda x: answer[x]. reverse=True)
