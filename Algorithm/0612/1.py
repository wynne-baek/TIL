def solution(p):
    size = len(p)
    answer = [0] * size
    for i in range(size):
        j = p.index(min(p[i:]))
        if i != j:
            p[i], p[j]= p[j], p[i]
            answer[i] += 1
            answer[j] += 1
    return answer