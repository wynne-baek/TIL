from collections import deque

def rotate(rc, num):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    len_r = len(rc[0])
    len_c = len(rc)
    how_many = (len_r + len_c)*2 - 4
    num = num % (how_many)
    x, y = 0, 0
    i = 0
    cnt = 1
    if num:
        nums = deque([rc[0][0]])
        while cnt != num:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len_c and 0 <= ny < len_r:
                nums.append(rc[nx][ny])
                cnt += 1
                x, y = nx, ny
            else:
                i = (i + 1) % 4
        while cnt < how_many:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len_c and 0 <= ny < len_r:
                nums.append(rc[nx][ny])
                rc[nx][ny] = nums.popleft()
                x, y = nx, ny
                cnt += 1
            else:
                i = (i + 1) % 4
        for _ in range(num):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len_c and 0 <= ny < len_r:
                rc[nx][ny] = nums.popleft()
                x, y = nx, ny
            else:
                i = (i + 1) % 4
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

print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))