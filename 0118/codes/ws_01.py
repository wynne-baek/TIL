#입력 : 1 이상 1000 이하의 정수

#출력 : 정수 n 의 모든 약수, 오름차순

number = int(input())

#반복, 나누어 떨어지면 작성,

for i in range(1,number+1):
    if number % i == 0:
        print(i, end =' ')