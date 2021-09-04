import sys

n = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solve(idx, first, second):
    if idx == n:
        if len(first) == n // 2 and len(second) == n // 2:
            s1, s2 = 0, 0
            for i in range(n//2):
                for j in range(n//2):
                    if i != j:
                        s1 += table[first[i]][first[j]]
                        s2 += table[second[i]][second[j]]
            return abs(s1-s2)
        else:
            return -1
    if len(first) > n // 2:
        return -1
    if len(second) > n // 2:
        return -1
    ans = -1
    t1 = solve(idx+1, first+[idx], second)
    if ans == -1 or (t1 != -1 and t1 < ans):
        ans = t1
    t2 = solve(idx+1, first, second+[idx])
    if ans == -1 or (t2 != -1 and t2 < ans):
        ans = t2
    return ans

print(solve(0, [], []))
