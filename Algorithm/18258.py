import sys
from collections import deque
n = int(sys.stdin.readline())
my_q = deque([])

for i in range(n):
    command = sys.stdin.readline().split()
    # push
    if command[0] == 'push':
        my_q.append(command[1])
    # pop
    if command[0] == 'pop':
        if len(my_q) == 0:
            print(-1)
        else:
            print(my_q.popleft())
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