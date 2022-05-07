from collections import deque


def solution(rc, operations):
    # 방향델타 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    len_r = len(rc[0])
    len_c = len(rc)
    answer = [[]]
    for op in operations:
        if op == 'Rotate':
            nums = deque([rc[0][0]])
            x, y = 0, 0
            flag = 1
            i = 0
            while flag:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len_c and 0 <= ny < len_r and nx == 0 and ny == 0:
                    rc[nx][ny] = nums.popleft()
                    flag = 0
                elif 0 <= nx < len_c and 0 <= ny < len_r:
                    nums.append(rc[nx][ny])
                    rc[nx][ny] = nums.popleft()
                    x, y = nx, ny
                else:
                    i += 1
        else:
            temp = deque([rc[0]])
            i = 1
            while i < len(rc):
                temp.append(rc[i])
                rc[i] = temp.popleft()
                i += 1
            rc[0] = temp.popleft()

    answer = rc
    return answer