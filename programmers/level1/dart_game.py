def solution(dartResult):
    score ={'S':1, 'D':2, 'T':3}
    darts = list(dartResult)
    tmp = [0]
    flag = True # '10'을 처리하기 위해
    l = len(darts)
    for i in range(l):
        # 10 처리
        if i != l-1 and darts[i].isdigit() and darts[i+1].isdigit():
            tmp.append(10**score[darts[i+2]])
            flag = False
        if darts[i] == '*':
            tmp[-1] *=2
            tmp[-2] *=2
        if darts[i] == '#':
            tmp[-1] *=-1
        if flag and darts[i] in score.keys():
            tmp.append(int(darts[i-1])**score[darts[i]])

    return sum(tmp)