import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for _ in range(1, T+1):
    N, M, C = map(int, input().split())
    bees = [list(map(int, input().split())) for __ in range(N)]
    #print(bees)
    bee_sum = [[0]*N for __ in range(N)]
    for idx in range(N):
        for i in range(N-M+1):
            temp = []
            for j in range(M):
                temp.append(bees[idx][i+j])
            if sum(temp) <= C:
                for nums in temp:
                    bee_sum[idx][i] += nums ** 2
            elif sum(temp) > C:
                combis = []
                for i in range(M):
                    combis.append(combinations(temp, i))
                print(tuple(combis))
                max_combi = 0
                temp_combi = 0
                for combi in combis:
                    if sum(list(combi)) <= C:
                        for combi_num in combi:
                            temp_combi += combi_num ** 2
                        if temp_combi > max_combi:
                            max_combi = temp_combi
                bee_sum[idx][i] = max_combi

    print(bee_sum)
    answer = []
    for sums in bee_sum:
        answer.append(max(sums))
    answer = sorted(answer, reverse=True)
    result = answer[0] + answer[1]
    print(result)