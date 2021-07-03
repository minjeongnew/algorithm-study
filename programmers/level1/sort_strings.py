def solution(strings, n):
    return sorted(strings, key=lambda x:[x[n], x])
    # 정렬 기준 key-> 단어의 n번째 인덱스 기준 정렬 후 사전식 정렬