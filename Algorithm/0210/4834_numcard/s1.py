import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    tc_len = int(input())
    cards = list(map(int, input()))
    #카운팅 정렬 사용하기
    arr = [0] * 10
    for idx in range(tc_len):
        arr[cards[idx]] += 1
    #print(arr)
    result = [] # 빈 리스트 준비
    #max(arr)가 1개 이상일 경우, 빈리스트에 인덱스를 추가
    if arr.count(max(arr)) != 1:
        for idx in range(10):
            if arr[idx] == max(arr):
                result.append(idx)
        #print(result)
        # 리스트에서 제일 큰 값과 max(arr)을 출력해준다
        print(f'#{_ + 1}', max(result), max(arr))
    # 만약 1개라면, max(arr)과 그 값을 가져다 주는 인덱스를 출력한다.
    if arr.count(max(arr)) == 1:
        print(f'#{_ + 1}', arr.index(max(arr)) , max(arr))

