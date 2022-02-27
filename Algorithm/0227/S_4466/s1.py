import sys
sys.stdin = open('input.txt')
# 테스트 케이스
T = int(input())
# 시험친 과목 N, 출력할 과목 수 K
for _ in range(1, T+1):
    N, K = map(int, input().split())
    # N개의 점수
    score = list(map(int, input().split()))
    result = 0
    for i in range(-1, -K - 1, -1):
        result += sorted(score)[i]
    print(f'#{_} {result}')
