import sys
sys.stdin = open('input.txt')

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
                new_temp = []
                for num in sorted(temp, reverse=True):
                    if sum(new_temp) < C:
                        new_temp.append(num)
                    if sum(new_temp) == C:
                        for nums in new_temp:
                            bee_sum[idx][i] += nums ** 2
                        break
                    if sum(new_temp) > C:
                        new_temp.pop()
                else:
                    for nums in new_temp:
                        bee_sum[idx][i] += nums ** 2
    print(bee_sum)
    answer = []
    for sums in bee_sum:
        answer.append(max(sums))
    answer = sorted(answer, reverse=True)
    result = answer[0] + answer[1]
    print(result)
