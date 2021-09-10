import sys, math

n = int(sys.stdin.readline())

prime_idx = [False, False] + [True]*(n-1)

def get_primes(x):
    for i in range(2, int(math.sqrt(x+1)+1)):
        for j in range(2*i, x+1, i):
            if prime_idx[i]:
                prime_idx[j] = False
    primes = []
    for idx, v in enumerate(prime_idx):
        if v:
            primes.append(idx)
    return primes
primes = get_primes(n)
# print(primes)
end = 0
cnt = 0
interval_sum = 0
len_p = len(primes)
for start in range(len_p):
    while interval_sum < n and end < len_p:
        interval_sum += primes[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= primes[start]
print(cnt)


