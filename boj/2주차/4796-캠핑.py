import sys


idx = 0
while True:
    idx += 1
    # 캠핑장을 연속하는 p일 중 l일 동안만 사용할 수 있다
    # 강산이는 v일 짜리 휴가를 시작헀다
    # 강산이는 캠핑장을 최대 며칠동안 사용 가능할까?
    # 1 < l < p < v
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0:
        break
    div = v // p
    mod = v % p
    answer = div*l + min(mod, l) # l일 동안만 사용할 수 있다는 조건 조심
    print('Case {}: {}'.format(idx, answer))