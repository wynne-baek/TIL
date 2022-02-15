import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    t = int(input())
    ladder = [list(map(int, input().split()))for _ in range(100)]
    #print(ladder)
    #도착지점 2에서 위 왼 오 활용해서 직진
    #도착지점의 y좌표를 찾아서 y에 저장
    x = 99
    y = ladder[99].index(2)
    #print(y)
    while x != 0:
        #제일 윗줄에 도착하면 반복문 종료
        # out of range 주의 / 지금 칸 좌측이 1이면 좌로 이동
        if (y-1 >= 0) and ladder[x][y-1] == 1:
            ladder[x][y] = 0
            y -= 1
        # 우측이 1이면 우로 이동
        elif (y+1 < 100) and ladder[x][y+1] == 1:
            ladder[x][y] = 0
            y += 1
        # 아니면 위로!
        else:
            x -= 1
    print(f'#{tc}', y)



