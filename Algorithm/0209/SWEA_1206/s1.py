import sys
sys.stdin = open('input.txt')


for tc in range(1, 11): #반복해서 input 넣어주기
    tc_num = int(input())
    my_list = list(map(int, input().split())) #각 줄 list로 저
    # print(my_list) #input 확인해본 결과, 홀수 줄은 테스트케이스 갯수, 짝수줄은 테스트 케이
    result = 0 #매번 리스트 초기
    for i in range(2, tc_num-1): #3부터 시작해서 num-2까지 반
        # my_list[i]가 앞 2개, 뒤 2개보다 클때,(슬라이싱과 max 활용)
        if max(my_list[i-2:i+3]) == my_list[i]:
            # my_list[i] 주 4개 중 가장 큰 수를 찾자! 원본에 변화를 주지 않는 sorted 사
            sorted_nums = sorted(my_list[i-2:i+3], reverse=True)
            #sorted, reverse된 리스트에서 두번째 요소를 뽑아 빼줌
            light = my_list[i] - sorted_nums[1]
            #result값에 더해줌
            result += light
        else:
            continue
    print(f'#{tc}',result)





