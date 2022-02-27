# 1. 단조증가하는 수 판별하는 함수
def danzo(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if str_num[i] > str_num[i+1]:
            return False
    return True

import sys
sys.stdin = open('input.txt')
# 테스트 케이스 갯수
T = int(input())
for _ in range(1, T+1):
    # 숫자 갯수
    N = int(input())
    # 숫자
    nums = list(map(int, input().split()))
# 숫자의 곱 중 가장 큰 단조증가하는 수
    max_danzo = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = nums[i] * nums[j]
        # 2. 판별해서 맞으면 max로 저장
            if danzo(num) is True:
            # 3. max값과 비교하며 갱신해서 출력!
                if num > max_danzo:
                    max_danzo = num
    print(f'#{_} {max_danzo}')