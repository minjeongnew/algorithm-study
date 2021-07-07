def solution(record):
    result = []
    state = {'Enter': '님이 들어왔습니다.',
             'Leave':'님이 나갔습니다.'}

    user = {}
    for r in record:
        u = r.split()
        if u[0] == 'Enter' or u[0] == 'Change':
            user[u[1]] = u[2]

    for r in record:
        u = r.split()
        if u[0] in state.keys():
            result.append(user[u[1]]+state[u[0]])
    return result


if __name__ == '__main__':
    record = ["Enter uid1234 Muzi",
              "Enter uid4567 Prodo",
              "Leave uid1234",
              "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))