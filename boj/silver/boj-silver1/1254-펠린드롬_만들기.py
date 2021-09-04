s = input()
for i in range(len(s)):
    t = s[i:]
    if t == t[::-1]:
        print(len(s)+i)
        break
# 부분 문자열이 펠린드롬이 되기까지의 왼쪽 문자열 개수만큼 더해주면됨