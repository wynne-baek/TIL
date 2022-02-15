import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    TC = int(input())
    grid = [[0] * 10 for _ in range(10)]
    for t_list in range(TC):
        ax, ay, bx, by, color = map(int, input().split())
        for i in range(ax, bx+1):
            for j in range(ay, by+1):
                if color == 1:
                    grid[i][j] += 1
                if color == 2:
                    grid[i][j] += 2
    cnt = 0
    for list in grid:
        cnt += list.count(3)

    print(f'#{_+1} {cnt}')
