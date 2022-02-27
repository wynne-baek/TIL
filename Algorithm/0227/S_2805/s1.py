import sys
sys.stdin = open('input.txt')
# 테스트 케이스
T = int(input())
# 크기 N
for _ in range(1, T+1):
    N = int(input())
    # N개씩 N줄
    paddy = [list(map(int, input())) for __ in range(N)]
    #print(paddy)
    total = 0
    for i in range(N//2):
        for j in range(N // 2 - i, N // 2 + i + 1):
            total += paddy[i][j]
            total += paddy[N-1-i][j]
    total += sum(paddy[N//2])
    print(f'#{_} {total}')
