import sys
sys.stdin = open('input.txt')

T = int(input()) #테스트케이스 입력 받기

for tc in range(1, T+1): #입력받은 테스트케이스 반복
    my_list = list(map(int, input().split())) #my_list라는 이름으로 저장
    #print(my_list) #input 잘 되었는지 확인!
    total = 0 #변수 total 생성 및 초기화
    for number in my_list: # my_list 안의 숫자들 반복해서
        total +=number # total 값에 더해주기
    mean = total / len(my_list) # total 을 my_list 의 길이로 나눠줌
    print(f'#{tc}',round(mean))
    # 출력 : 각 줄은 #t 공백 한칸, 정답 출력(정답은 소수점 첫째 자리에서 반올림한 정수)
    # f string으로 tc번호 입력
    # 소수점 첫 자리에서 반올림한 정수 만들기 위해 round함수 사용(처음에 round(mean)을 문자열로 변환해 출력하려고 했는데 그럴 필요는 없는듯?
