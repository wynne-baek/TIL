import sys
sys.stdin = open('input.txt')

'''가로(일반), 세로(전치행렬)로 1이 연속해서 k개 등장하는 것의 개수를 세주자!'''

T = int(input())
# N: 퍼즐 가로세로 길이, K : 단어 길이
for _ in range(10):
    N, K = map(int, input().split())
    #흰색 부분 : 1, 검은 부분 : 0, 흰 부분에 작성 가능
    arr = [list(map(int, input().split())) for i in range(N)]
    #print(arr)
    #전치행렬
    arr2 = [list(x) for x in zip(*arr)]
    #print(arr2)
    cnt = 0
    for lst in arr:
        for j in range(N-K+1):
            if lst[j:j+K].count(1) == K:
                if ((j-1 < 0) or lst[j-1] == 0) and ((j+K == N) or lst[j+K] == 0):
                    cnt += 1
    for lst in arr2:
        for j in range(N-K+1):
            if lst[j:j+K].count(1) == K:
                if ((j-1 < 0) or lst[j-1] == 0) and ((j+K == N) or lst[j+K] == 0):
                    cnt += 1
    print(f'#{_+1} {cnt}')