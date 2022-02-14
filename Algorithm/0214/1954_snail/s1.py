import sys
sys.stdin = open('input.txt')

TC = int(input())

#상 우 하 좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(TC):
    size = int(input())
    #print(size)
    # TC * TC 인 이차원 리스트 생성
    # 0,0 부터 ~0, _까지 _
    arr = [[0]* size for _ in range(size)]

    r, c = 0, 0
    d = 0

    for n in range(1, size*size + 1):
        arr[r][c] = n
        r += dr[d]
        c += dc[d]

        if r < 0 or c < 0 or r >= size or c >= size or arr[r][c] != 0:
            #다시 바로 전 단계로 돌아가서
            r -= dr[d]
            c -= dc[d]
            #d를 다음으로
            d = (d + 1) % 4
            # 다시 출발
            r += dr[d]
            c += dc[d]

    print(f'#{_+1}')
    for row in arr:
        for num in row:
            print(num, end=' ')
        print()


