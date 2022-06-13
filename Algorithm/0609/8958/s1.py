import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    score = 0
    tmp = 0
    quiz = input()
    for char in quiz:
        if char == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0

    print(score)

