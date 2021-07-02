keypad = {1:(0,0), 2:(0,1), 3:(0,2),
           4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2),
           '*':(3,0), 0:(3,1), '#':(3,2)}


def dist(i, j):
    return abs(keypad[i][0]-keypad[j][0])+abs(keypad[j][1]-keypad[j][1])


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'

    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            left = n
        elif n in [3,6,9]:
            answer +='R'
            right = n
        else:
            l = dist(left, n)
            r = dist(dist, n)
            if l > r :
                answer +='R'
                right = n
            elif r > l:
                answer += 'L'
                left = n
            else:
                if hand == 'right':
                    answer += 'R'
                    right = n
                else:
                    answer += 'L'
                    left = n

    return answer