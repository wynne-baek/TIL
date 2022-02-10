import sys
sys.stdin = open('input.txt')

for _ in range(10):
    # 덤프 가능 횟수
    count = int(input())
    box = list(map(int, input().split()))
    #print(box)
    #젤 큰거 -1, 젤 작은거 + 1, cnt -1
    while count != 0:
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        count -= 1
    result = max(box) - min(box)
    print(f'#{_ + 1}', result)
