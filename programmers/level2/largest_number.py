def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    # [0,0,0,0]인 경우 '0'을 리턴함
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)