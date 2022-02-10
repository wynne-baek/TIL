import sys
sys.stdin = open('input.txt')

#testcase 갯수
T = int(input())
#
for _ in range(T):
    tc_len, size = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(tc_len, size)
    #print(arr)
    result = []
    for i in range(tc_len -size + 1):
        my_sum = 0
        for j in range(size):
            my_sum += arr[i + j]
        result.append(my_sum)
    answer = max(result) - min(result)
    print(f'#{_+1}', answer)












