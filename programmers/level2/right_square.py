# 최대공약수
def gcd(x, y):
    k = min(x, y)
    for i in range(k, 0, -1):
        if x%i == 0 and y%i ==0:
            return i


def solution(w, h):
    g = gcd(w, h)
    all = w*h
    g_w = w/g
    g_h = h/g
    # 기울기가 1이 아닌 경우
    if g_h/g_w != 0:
        return all - (g_w+g_h-1)*g
    # 기울기가 1일 때
    return all - w