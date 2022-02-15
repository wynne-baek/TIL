import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    result = [0]* 10
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(5):
        result[i * 2] = sorted(nums)[-i-1]
        result[(i* 2)+1] = sorted(nums)[i]

    print(f'#{_+1}', *result)