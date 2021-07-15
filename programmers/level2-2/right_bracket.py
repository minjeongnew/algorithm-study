def solution(s):
    ans = 0
    for x in s:
        if ans < 0:
            return False
        if x == '(':
            ans += 1
        elif x == ')':
            ans -= 1
    return ans == 0