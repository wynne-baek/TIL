import sys
sys.stdin = open('input.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

TC = int(input())
for _ in range(TC):
    size, my_sum = map(int, input().split())
    #print(size, sum)
    #size의 부분집합을 모두 모아서, 그 중에 sum이 my_sum인 갯수를 출력하자
    set = []
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(A[j])
        set.append(subset)
    #print(set) #부분집합 출력
    len_set = []
    for list in set:
        if len(list) == size:
            len_set.append(list)
    #print(len_set) #길이가 size와 같은 리스트 출력
    result = 0
    for j in len_set:
        if sum(j) == my_sum:
            result += 1

    print(f'#{_+1}', result)