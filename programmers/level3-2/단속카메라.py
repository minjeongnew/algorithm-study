def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    camera = -30001
    print(routes)
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
    return answer


if __name__ == '__main__':
    r = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(r))