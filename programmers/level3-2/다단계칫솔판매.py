def solution(enroll, referral, seller, amount):
    tree = {"-": "root"}
    money = {"-": 0}
    for e, r, in zip(enroll, referral):
        tree[e] = r
        money[e] = 0
    for s, a in zip(seller, amount):
        c = a * 100
        while tree[s] != "root":
            if c == 0:
                break
            money[s] += (c - c//10)
            s = tree[s]
            c = c // 10
    answer = []
    for e in enroll:
        answer.append(money[e])
    return answer


if __name__ == "__main__":
    e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    s = ["young", "john", "tod", "emily", "mary"]
    a = [12, 4, 2, 5, 10]
    print(solution(e, r, s, a))