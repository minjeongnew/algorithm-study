s = input()
for i in range(len(s)):
    t = s[i:]
    if t == t[::-1]:
        print(len(s)+i)
        break

