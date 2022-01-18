# 0118_workshop

## 1. 간단한 N의 약수

```python
number = int(input())

#반복, 나누어 떨어지면 작성,

for i in range(1,number+1):
    if number % i == 0:
        print(i, end =' ')
```



## 2. 중간값 찾기

```python
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

#오름차순 정렬
numbers.sort()
#17번째 숫자 출력
print(numbers[16])
```



## 3. 계단 만들기

```python
number = int(input())

# for문으로 number 까지 반복
for i in range(1, number+1):
    for pyramid in range(1, i+1):
        print(pyramid, end = ' ')
    print()