def process(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    return music


def solution(m, musicinfos):
    answer = []
    idx = 0
    for info in musicinfos:
        idx += 1
        music = info.split(',')
        start = music[0].split(':')
        end = music[1].split(':')
        # 재생 시간 계산
        t = (int(start[0])*60 + int(start[1])) - (int(end[0])*60 + int(end[1]))

        changed = process(music[3])
        # 재생된 음의 길이
        ml = len(changed)
        # 재생 시간에 재생된 음
        pm = changed * (t//ml) + changed[:t%ml]
        # 기억한 멜로디
        mm = process(m)
        # 기억한 멜로디가 재생된 음에 있다면 [시간, idx, 제목] 추가
        if mm in pm:
            answer.append([t, idx, music[2]])

    if not answer:
        return 'None'
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]