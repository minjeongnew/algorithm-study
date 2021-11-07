import sys

n = int(sys.stdin.readline())
words = set([str(sys.stdin.readline().strip()) for _ in range(n)])
words = sorted(words, key=lambda x:(len(x), x))
for x in words:
    print(x)