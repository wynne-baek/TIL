import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, 11):
    S = int(input())
    arr = [list(map(int, input().split())) for _ in range(S)]
    arr2 = list(zip(*arr))
    # print(arr)
    # print(arr2)
    result = 0
    for i in range(S):
        before = 0
        for j in range(S):
            if arr2[i][j] == 2:
                if before == 1:
                    result += 1
                    before = 2
            elif arr2[i][j] == 1:
                before = 1
    print(f'#{_} {result}')
