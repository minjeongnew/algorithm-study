# 수학
# 점화식 찾기
# n = x + x+1 + x+2 + x+3 + .. + x+l-i
# n = (x*l) + ((l-1)*(l-2))/2
# t = ((l-1)*(l-2))/2 로 치환
# n = (x*l) + t/
# x = (n-t)/l -> x 를 구하장

n, l = map(int, input().split())

x = -1
t = 0
iter = 0
for i in range(l, 101):
    t = (i*(i-1)) / 2
    if (n - t) % i == 0 and (n - t) // i >= 0:
        x = (n - t) // i
        iter = i
        break
if x == -1:
    print(x)
else:
    for i in range(iter):
        print(int(x) + i, end=" ")
    print()
