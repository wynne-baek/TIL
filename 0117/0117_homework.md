# 0117 Homework

## 1. Python 예약어

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```



## 2. 실수 비교

```python
import **math**, **sys**
num1 = 0.1 * 3
num2 = 0.3
math.fabs(num1 - num2) <= sys.float_info.epsilonimport math, sys
```



## 3. 이스케이프 시퀀스

1. 줄바꿈 : \n
2. 탭 : \t
3. 백슬래시 : \\\



## 4. String Interpolation 

```python
name = '철수'
print(f'안녕, {name}야')
```



## 5. 형 변환

(5)



## 6. 네모출력

```python
n = 5
m = 9
print(('*' * n + '\n') * m)
```



## 7. 이스케이프 시퀀스 응용

```python
print("\"파일은 c:\Windows\\Users\내문서\Python에 저장이 되었습니다.\" \n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'")
```



## 8. 근의 공식

```python
a = int(input("이차항의 계수를 입력하세요: "))
b = int(input("일차항의 계수를 입력하세요: "))
c = int(input("상수항의 계수를 입력하세요: "))

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
 
print('해는 {} 또는 {}'.format(r1, r2))
```

