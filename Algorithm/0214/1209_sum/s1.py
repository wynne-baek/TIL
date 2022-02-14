import sys
sys.stdin = open('input.txt')

for _ in range(10):
    TC = int(input()) # 테스트 케이스 번
    arr = [list(map(int, input().split())) for __ in range(100)] # 각 테스트케이스를 이차원 리스트로 저장
    #print(TC, arr)
    #결과들을 저장할 result 리스트 생성
    result = []
    #1. 가로
    for i in range(100):
        h_sum = 0 # 수평 합 초기화
        for j in range(100):
            h_sum += arr[i][j]
        result.append(h_sum)
    #print(result)
    #2. 세로
    for j in range(100):
        p_sum = 0 # 수직 합 초기화
        for i in range(100):
            p_sum += arr[i][j]
        result.append(p_sum)
    # 3. 대각선(좌 -> 우)
    d_sum1 = 0 # 대각선 합 1 초기화
    for i in range(100):
        d_sum1 += arr[i][i]
    result.append(d_sum1)
    #print(d_sum1)
    # 4. 대각선 (우 -> 좌)
    d_sum2 = 0 # 대각선 합 2 초기화
    for i in range(100):
        d_sum2 += arr[i][99-j]
    result.append(d_sum2)
    #print(d_sum2)
    #결과 출력
    print(f'#{TC}',max(result))
