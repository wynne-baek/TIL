import sys
sys.stdin = open('input.txt')

# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

T = int(input())
#K(한번 충전으로 최대한 이동할 수 있는 정류장 수), N(정류장 갯수), M(충전기가 설치된 정류장의 갯수)
#충전기가 설치되어 있는 정류장 번호
for _ in range(T):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    # print(K, N, M)
    # print(M_list)
    # 충전기가 있으면 1, 충전기가 없으면 0인 리스트 생성
    stop = [0] * (N+1)
    for num in M_list:
        stop[num] = 1

    bus = 0
    result = 0
    while bus < N:
        bus += K
        if bus >= N:
            break
        else:
            if stop[bus] == 1:
                result += 1
            elif stop[bus] == 0:
                for i in range(bus, bus-K, -1):
                    if stop[i] == 1:
                        bus = i
                        result += 1
                        break
                else:
                    result = 0
                    break

        # if stop[bus+1:bus+K-1].count(0) == K:
        #     result = 0
        #     break
        # else:
    print(f'#{_+1}', result)

