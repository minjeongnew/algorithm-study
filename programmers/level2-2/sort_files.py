def solution(files):
    file_list = []
    for file in files:
        head = ''
        for f in file:
            if f.isdecimal():
                break
            else:
                head += f
        num = ''
        for f in file[len(head):len(head)+5]:
            if f.isalpha():
                break
            else:
                num += f
        tmp = [head.islower(), int(num), file]
        file_list.append(tmp)
    file_list = sorted(file_list, key=lambda x: [x[0], x[1]])
    return [x[2] for x in file_list]