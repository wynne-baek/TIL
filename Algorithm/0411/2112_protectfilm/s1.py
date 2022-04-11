import sys
sys.stdin = open('input.txt')

def check(arr):
    for i in range(W):
        film_cnt = 1
        for j in range(D - 1):
            if arr[j][i] == arr[j + 1][i]:
                film_cnt += 1
            else:
                film_cnt = 1
            if film_cnt >= K:
                break
        if film_cnt < K:
            return False
    return True

def dfs(arr, cnt, n):
    global min_cnt
    num0 = [0] * W
    num1 = [1] * W
    # 종료조건
    new_arr = []
    for line in arr:
        new_arr.append(line)
    if min_cnt <= cnt:
        return
    if check(new_arr):
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if cnt == K:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    else:
        for idx in range(n, D):
            if not visited[idx]:
                temp = new_arr[idx][:]
                visited[idx] = 1
                new_arr[idx] = num0
                dfs(new_arr, cnt+1, idx)
                new_arr[idx] = num1
                dfs(new_arr, cnt+1, idx)
                new_arr[idx] = temp
                visited[idx] = 0
    return

T = int(input())
for _ in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(D)]
    min_cnt = K
    if K == 1:
        answer = 0
    else:
        visited = [0] * D
        dfs(arr, 0, 0)
        answer = min_cnt
    print(f'#{_}', answer)