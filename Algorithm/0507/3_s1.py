def solution(alp, cop, problems):
    answer = 0
    """
    알고력, 코딩력, 문제들이 담긴 배열이 주어짐
    문제 : [필요알고력, 필요코딩력, 보상알고력, 보상코딩력, 걸리는 시간] 의 형태로 저장되어 있음
    높이는 방법
    1)공부(1 올리는데 1시간)
    2)문제풀이(정해진 시간,보상 알고력, 보상 코딩력)

    모든 문제를 통틀어서 최대필요알고력 최대필요코딩력을 달성하면 됨
    풀 수 있는 문제 중, 차이를 메꿀 수 있으면서 최소 시간을 요구하는 문제를 풀면 되는데... 
    """
    max_coR = 0
    min_coR = 10000
    max_alR = 0
    min_alR = 10000
    grow_co = []
    grow_al = []
    time = []
    for p in problems:
        if p[0] > max_alR:
            max_alR = p[0]
        if p[0] > min_alR:
            min_alR = p[0]
        if p[1] > max_coR:
            max_coR = p[1]
        if p[1] < min_coR:
            min_coR = p[1]
        grow_al.append(p[2])
        grow_co.append(p[3])
        time.append(p[4])
    if alp < min_alR and cop < min_coR:
        time = min_alR - alp + min_coR - alp
        answer += time

    return answer