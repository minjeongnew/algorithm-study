def solution(enroll, referral, seller, amount):
    pdict = {"-": "root"}
    sells = {"-": 0}
    for e, r in zip(enroll, referral):
        pdict[e] = r # pdidct[자식] = 부모
        sells[e] = 0
    for s, a in zip(seller, amount):
        c = a * 100
        while pdict[s] != "root":
            if c == 0:
                break
            sells[s] += c - c // 10
            c = c - (c - c // 10)
            s = pdict[s]

    answer = []
    for e in enroll:
        answer.append(sells[e])
    return answer


if __name__ == "__main__":
    if __name__ == "__main__":
        e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
        r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
        s = ["young", "john", "tod", "emily", "mary"]
        a = [12, 4, 2, 5, 10]
        print(solution(e, r, s, a))
