def solution(nums):
    l = len(set(nums)) # 중복 제거 후 종류의 개수
    if l < len(nums)//2: # 중복 제거 후 종류가 n/2보다 작은 경우
        return l
    return len(nums)//2 # 그 이외에는 n/2개를 리턴


# 위의 식을 간결하게 표현한 것
def solution2(nums):
    return min(len(set(nums)), len(nums)//2)