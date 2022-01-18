# 0118 homework

## 1. Mutable & Immutable

Mutable : List, Set, Dictionary

Immutable : Tuple, Range



## 2. 홀수만 담기

```python
odd_num = []

#range는 ()
for x in range(1,51,1):
	if x % 2 == 1 :
    odd_num.append(x)
  else:
    continue
  x = x + 1

print(odd_num)
```



## 3. Dictionary 만들기

```python
class_mate = {'김현영':30, '김영훈':29, '김남훈':28, '고은민':27, '권민주':26, '구홍지':25}
```



## 4. 반복문으로 네모 출력

``` python
n = 5
m = 9

#반복 임시 변수 i
i = 0
#while문으로 9번 반복
while i <= m:
    print('*'*n)
    i = i + 1
```



## 5. 조건표현식

```python
temp = 36.5
a = '입실 불가' if temp >= 37.5 else '입실 가능'
print(a)
```



## 6. 평균 구하기

```python
scores = [80, 89, 99, 83]

sum = 0

#for로 모든 요소 더해서 sum 만들기
for score in scores:
  sum = sum + score

#sum을 score의 갯수로 나누기
print(sum/len(scores))
```