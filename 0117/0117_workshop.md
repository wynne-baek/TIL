# 0117_workshop

## 1. 세로로 출력하기

자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```python
number = int(input())

i = 1
# i가 a보다 작거나 같으면 프린트 후 줄바꿈 후 +1

#while
while i <= number:
    print(i)
    i = i+1
    
#for
for i in range(1,number+1):
    print(i)
```



## 2. 거꾸로 세로로 출력하기

자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

```python
number = int(input())

i = number
# i가 a보다 작거나 같고, 0보다 크거나 같으면 프린트 후 -1

#while
while 0 <= i <= number:
    print(i)
    i = i-1
    
#for
for i in range(number, -1, -1):
		print(i)
```



## 3. n줄 덧셈

```python
a = int(input())
print(int(a*(a+1)/2))
```



