import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1,11):
    # N = 파리판 사이즈, M = 파리채 사이
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for i in range(N)]
    #print(fly_arr)
    result = []

    for cnt1 in range(N-M+1):
        for cnt2 in range(N-M+1):
            fly_sum = 0
            for j in range(cnt1, cnt1+M):
                for k in range(cnt2, cnt2+M):
                    fly_sum += fly_arr[j][k]
            result.append(fly_sum)
    print(f'#{_} {max(result)}')