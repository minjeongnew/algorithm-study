# 최대 공약수
def gcd(x, y):
    min_ = min(x, y)
    for i in range(min_, 0, -1):
        if x%i==0 and y%i==0:
            return i


def solution(w, h):
    answer = 0
    g = gcd(w, h)
    x = w / g
    y = h / g
    # 기울기가 1이 아닌 경우
    if y / x != 1:
        # 작은 사각형에서 잘라진 사각형 수
        cutt = x + y - 1
        answer = w*h - g*(cutt)
    # 기울기가 1인 경우
    else:
        answer = w*h - w
    return answer
