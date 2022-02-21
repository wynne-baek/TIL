import sys
sys.stdin = open('input.txt')

N = int(input())
answer = 0
for i in range(1, N+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == N:
        answer = i
        # 가장 작은 i를 원하니까 찾으면 break
        break
print(answer)