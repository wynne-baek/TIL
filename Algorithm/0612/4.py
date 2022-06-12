def solution(grid, k):
    answer = -1
    """
    n, m 격자
    평지, 숲, 강 = 0, 1, -1
    """

    def dfs(x, y, temp):
        # 종료조건
        if x == n - 1 and y == m - 1:
            this_answer = temp[:]
            answers.append(this_answer)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and ground[nx][ny] >= 0 and not visited[nx][ny]:
                temp.append(ground[nx][ny])
                visited[nx][ny] = 1
                dfs(nx, ny, temp)
                temp.pop()
                visited[nx][ny] = 0

    # 입력 이차원 배열로 변경
    n = len(grid)
    m = len(grid[0])
    ground = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'F':
                ground[i][j] = 1
            elif grid[i][j] == '#':
                ground[i][j] = -1
    # print(ground)

    # dfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    stack = [(0, 0)]
    temp = [0]
    answers = []
    dfs(0, 0, temp)
    # print(answers)
    min_cnt = 10000
    for answer in answers:
        cnt = current = 0
        while current + k < len(answer):
            for step in range(k, 0, -1):
                if answer[current + step] == 0:
                    current += step
                    cnt += 1
                    break
        if cnt < min_cnt:
            min_cnt = cnt
    answer = cnt -1
    return answer