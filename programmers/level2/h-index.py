def solution(citations):
    citations.sort(reverse=True)
    for idx, v in enumerate(citations):
        if idx >= v:
            return idx
    return len(citations)