# 일일이 모든 수에 대하여 prime 구하는 경우의 수
# 50C3 = 약 2만?

# 두 번째 방법 채택
# 에라토스테네체 사용해서 prime 배열 만들고 계속 사용하기
# prime 배열 크기 -> 1000*3

p = [False, False] + [True]*3000

# 에라토스테네 체
def prime(n):
    for i in range(2, n+1):
        if p[i]:
            for j in range(2*i, n+1, i):
                p[j]=False


def solution(nums):
    answer = 0
    len_n = len(nums)

    prime(max(nums)*3)

    for i in range(len_n):
        for j in range(i+1, len_n):
            for k in range(j+1, len_n):
                if p[nums[i]+nums[j]+nums[k]]:
                    answer +=1

    return answer
