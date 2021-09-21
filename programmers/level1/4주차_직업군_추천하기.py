def solution(table, languages, preference):
    scores = {}
    for x in table:
        for lang, pre in zip(languages, preference):
            tmp = x.split(' ')
            job = tmp[0]
            if lang in tmp:
                scores[job] = scores.get(job, 0) + (6 - tmp.index(lang))
    answers = sorted(scores.items(), key=lambda x:[-x[1], x[0]])
    return answers[0][0]