def solution(enroll, referral, seller, amount):
    trees = {"-": "root"}
    sells = {"-": 0}
    for e, r in zip(enroll, referral):
        trees[e] = r
        sells[e] = 0
    for s, a in zip(seller, amount):
        c = a * 100
        sells[s] += (c - c//10)
        while trees[s] != "root":
            s = trees[s]
            c //= 10
            # 이 조건이 없었을 때 테스트케이스 11, 12, 13 실패
            # 0을 더할 필요는 없으니까
            if c - c//10 == 0:
                break
            sells[s] += (c-c//10)
    answer = []
    for e in enroll:
        answer.append(sells[e])
    return answer


if __name__ == "__main__":
    e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    s = ["young", "john", "tod", "emily", "mary"]
    a = [12, 4, 2, 5, 10]
    print(solution(e, r, s, a))
