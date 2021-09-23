def solution(record):
    answer = []
    ids = {}
    for x in record:
        x = x.split(' ')
        if x[0] == 'Change':
            ids[x[1]] = x[2]
        elif x[0] == 'Enter':
            ids[x[1]] = x[2]

    for x in record:
        x = x.split(' ')
        if x[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(ids[x[1]]))
        elif x[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(ids[x[1]]))
    return answer


# 과거 제출
def solution2(record):
    answer = []
    # uid : [[states], nickname]
    users = {}

    order_stack = []  # uid 넣을 거임
    for r in record:
        u = r.split(" ")
        order_stack.append(u[1])
        if u[1] in users.keys():
            if u[0] == 'Leave':
                tmp = users[u[1]][1]
                stack = [users[u[1]][0] + [u[0]], tmp]
                users[u[1]] = stack
            else:
                stack = [users[u[1]][0] + [u[0]], u[2]]
                users[u[1]] = stack
        else:
            users[u[1]] = [[u[0]], u[2]]

    for o in order_stack:
        if users[o][0][0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(users[o][1]))
        elif users[o][0][0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(users[o][1]))
        s_tmp = users[o][0][1:]
        n_tmp = users[o][1]
        users[o] = [s_tmp, n_tmp]
    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))