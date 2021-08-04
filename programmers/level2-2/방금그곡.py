def change_music(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    elif 'C#' in music:
        music = music.replace('C#', 'c')
    elif 'D#' in music:
        music = music.replace('D#', 'd')
    elif 'F#' in music:
        music = music.replace('F#', 'f')
    elif 'G#' in music:
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
        # 재생 시간:
        t = (int(end[0])*60 + int(end[1])) - (int(start[0])*60 + int(start[1]))
        # 악보 정보 변환
        changed = change_music(music[3])
        # 악보 길이
        pl = len(changed)
        # 방송된 곡 전체
        pm = changed * (t//pl) + changed[:t%pl]
        m = change_music(m)
        if m in pm: # 해당되면 [순서(idx), 재생시간, 제목]
            answer.append([idx, t, music[2]])
    if len(answer) == 0:
        return '(None)'
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x:(-x[1], x[0]))
        return answer[0][2]


if __name__ == '__main__':
    m = "CC#BCC#BCC#BCC#B"
    m_infos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    print(solution(m, m_infos))