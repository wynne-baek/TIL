# 입력
import sys
from itertools import combinations, permutations
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    synergys = [list(map(int, input().split())) for __ in range(N)]
    #print(synergy)
    ingredient = list(range(N))
    # 정답 초기값 설정(최댓값이 20000)
    ans = 20000 * N * (N-1)
    # 조합으로 절반 구하기
    for combi in combinations(ingredient, N//2):
        # 시너지 합 담을 변수 초기화
        sum1, sum2 = 0, 0
        # 나머지 절반
        remain = [i for i in ingredient if i not in combi]
        # 반씩 시너지 합 구해주기
        # 1.1. 조합 사용
        # for synergy in combinations(combi, 2):
        #     sum1 += synergys[synergy[0]][synergy[1]]
        #     sum1 += synergys[synergy[1]][synergy[0]]
        # for synergy in combinations(remain, 2):
        #     sum2 += synergys[synergy[0]][synergy[1]]
        #     sum2 += synergys[synergy[1]][synergy[0]]
        # 1.2. 순열 사용
        for synergy in permutations(combi, 2):
            sum1 += synergys[synergy[0]][synergy[1]]
        for synergy in permutations(remain, 2):
            sum2 += synergys[synergy[0]][synergy[1]]
        # 절댓값으로 두 값 차 구해주기
        cal = abs(sum1 - sum2)
        # 결과값과 비교해 더 작은 값 저장!
        if cal < ans:
            ans = cal
    print(f'#{_} {ans}')
