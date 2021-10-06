def solution(files):
    answer = []
    for idx, file in enumerate(files):
        origin = file
        head, number, tail = '', '', ''
        stop_head = 0
        for i, x in enumerate(file):
            if x.isdecimal():
                stop_head = i
                break
            else:
                head += x.lower()
        file = file[stop_head:]
        stop_number = 0
        for i, x in enumerate(file):
            if x.isdecimal():
                number += x
            else:
                stop_number = i
                break
        file = file[stop_number:]
        tail = file
        answer.append([head, number, tail, origin, idx])
    answer.sort(key=lambda x: (x[0], int(x[1]), x[4]))
    return [x[3] for x in answer]


if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))