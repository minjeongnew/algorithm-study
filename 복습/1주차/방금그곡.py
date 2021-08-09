def music_change(music):
    if "A#" in music:
        music = music.replace("A#", "a")
    if "C#" in music:
        music = music.replace("C#", "c")
    if "D#" in music:
        music = music.replace("D#", "d")
    if "F#" in music:
        music = music.replace("F#", "f")
    if "G#" in music:
        music = music.replace("G#", "g")
    return music


def solution(m, musicinfos):
    answer = []
    m = music_change(m) # 들은 멜로디 변환
    idx = 0
    for info in musicinfos:
        idx += 1
        info = info.split(",")
        # ["12:00","12:14","HELLO", "CDEFGAB"]
        start = info[0].split(":")
        end = info[1].split(":")
        # 음악 시간
        time = (int(end[0])*60 + int(end[1])) - (int(start[0])*60 + int(start[1]))
        # 악보 정보 변환하기
        music = music_change(info[3])
        # 악보 길이
        lm = len(music)
        # 재생 음악
        play = music * (time//lm) + music[:(time%lm)]
        if m in play:
            answer.append([time, idx, info[2]]) # 재생 시간, 입력된 순서, 제목
    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x:(-x[0], x[1]))
        return answer[0][2]


if __name__ == '__main__':
    m = "CC#BCC#BCC#BCC#B"
    m_infos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    print(solution(m, m_infos))
    m = "ABCDEFG"
    m_infos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    print(solution(m, m_infos))