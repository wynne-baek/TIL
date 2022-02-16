import sys
sys.stdin = open('input.txt')

NUMS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(1, T+1):
    TC = list(map(str, input().split()))
    size = int(TC[1])
    sorted_num = []
    #print(size)
    nums = list(map(str, input().split()))
    #계수 정렬 쓰면?!
    count_list = [0] * 10
    for i in range (10):
        count_list[i] = nums.count(NUMS[i])
    #print(count_list)
    for j in range(1,10):
        count_list[i] += count_list[i-1]
    #print(count_list)
    for k in range(10):
        sorted_num.append((NUMS[k]+' ')* count_list[k])
    print(f'#{_}')
    print(*sorted_num)
