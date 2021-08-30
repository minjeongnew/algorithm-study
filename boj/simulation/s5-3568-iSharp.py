import sys

a = list(map(str, sys.stdin.readline().split()))
b = []
while a:
    x = a.pop(0)
    x = x.replace(",", "")
    x = x.replace(";", "")
    b.append(x)


def solve(v, s):
    tmp = v
    reversed_s = s[::-1]
    idx = -1
    for i in range(len(reversed_s)):
        x = reversed_s[i]
        if x in ["*", "[", "]", "&"]:
            if x == "]":
                tmp += "["
            elif x == "[":
                tmp += "]"
            else:
                tmp += x
        else:
            idx = i
            break
    tmp += " "
    tmp += reversed_s[idx:][::-1]
    tmp += ";"
    print(tmp)


for x in b[1:]:
    solve(b[0], x)