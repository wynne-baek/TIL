## 2번으로 제출 시, 정확 통과/효율 2,4,7 불통

from collections import deque

def rotate(rc, num):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    len_r = len(rc[0])
    len_c = len(rc)
    nums = deque([rc[0][0]])
    x, y = 0, 0
    flag = 1
    i = 0
    while flag:
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len_c and 0 <= ny < len_r and nx == 0 and ny == 0:
            flag = 0
        elif 0 <= nx < len_c and 0 <= ny < len_r:
            nums.append(rc[nx][ny])
            x, y = nx, ny
        else:
            i += 1
    x, y = 0, 0
    cnt = 0
    idx = 0
    while cnt != num - 1:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < len_c and 0 <= ny < len_r:
            x, y = nx, ny
            cnt += 1
        else:
            idx = (idx + 1) % 4
    while nums:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < len_c and 0 <= ny < len_r:
            rc[nx][ny] = nums.popleft()
            x, y = nx, ny
        else:
            idx = (idx + 1) % 4
    return rc

def shiftRow(rc, num):
    num %= len(rc)
    if num:
        temp = deque()
        for cnt in range(num):
            temp.append(rc[cnt])
        i = num
        while i < len(rc):
            temp.append(rc[i])
            rc[i] = temp.popleft()
            i += 1
        for idx in range(num):
            rc[idx] = temp.popleft()
    return rc


def solution(rc, operations):
    temp_op = []
    for op in operations:
        if not temp_op:
            temp_op.append(op)
        elif temp_op and temp_op[-1] == op:
            temp_op.append(op)
        elif temp_op and temp_op[-1] != op:
            if temp_op[-1] == 'Rotate':
                rotate(rc, len(temp_op))
            elif temp_op[-1] == 'ShiftRow':
                shiftRow(rc, len(temp_op))
            temp_op = [op]
    if temp_op and temp_op[0] == 'Rotate':
        rotate(rc, len(temp_op))
    elif temp_op and temp_op[0] == 'ShiftRow':
        shiftRow(rc, len(temp_op))
    answer = rc
    return answer

print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))