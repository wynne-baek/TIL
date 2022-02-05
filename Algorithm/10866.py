import sys
from collections import deque
n = int(sys.stdin.readline())
my_q = deque([])

for i in range(n):
    command = sys.stdin.readline().split()
    # push_front
    if command[0] == 'push_front':
        my_q.appendleft(command[1])
    # push_back
    if command[0] == 'push_back':
        my_q.append(command[1])
    # pop_front
    if command[0] == 'pop_front':
        if len(my_q) > 0:
            print(my_q.popleft())
        else:
            print(-1)
    # pop_back
    if command[0] == 'pop_back':
        if len(my_q) > 0:
            print(my_q.pop())
        else:
            print(-1)
    # size
    if command[0] == 'size':
        print(len(my_q))
    # empty
    if command[0] == 'empty':
        if len(my_q) == 0:
            print(1)
        else:
            print(0)
    # front
    if command[0] == 'front':
        if len(my_q) == 0:
            print(-1)
        else:
            print(my_q[0])
    # back
    if command[0] == 'back':
        if len(my_q) == 0:
            print(-1)
        else:
            print(my_q[-1])
    