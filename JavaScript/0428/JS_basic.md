# JS_function

## 선언식 vs 표현식

- 함수의 타입 : 선언식 함수와 표현식 함수 모두 `function` 타입

- 호이스팅
  - 함수 선언식 : 호이스팅 발생, 함수 호출 이후에 선언해도 동작
  - 함수 표현식 : 함수 정의 전 호출 시 에러 발생, 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의  scope 규칙을 따름
    - 함수 표현식을 var 키워드로 작성할 경우, 변수가 선언 전 undefined로 초기화 되어 다른 에러 발생

## Arrow function

- 화살표 함수
  - 함수를 비교적 간결하게 정의
  - function 키워드 생략 가능
  - 함수의 매개변수가 단 하나 뿐이라면 `()`도 생략 가능
  - 함수의 몸통이 표현식 하나라면 `{}`, `return`도 생략 가능

```javascript
const arrow1 = function (name) {
    return `hello, ${name}`
}
// 1. function 키워드 생략
const arrow = (name) => {return `Hello ${name}`}
// 2. 매개변수가 1개일 경우 () 생략
const arrow = name => {return `Hello ${name}`}
// 함수 바디가 return 을 포함한 표현식 1개일 경우 {}, return 생략
const arrow4 = name => `Hello ${name}`
```



# 문자열

- 문자열 관련 주요 메서드 목록
  1. includes : 특정 문자열의 존재여부를 참/거짓으로 반환
     - 문자열에 value가 존재하는지 판별 후 t/f 반환
  2. split : 문자열을 토큰 기준으로 나눈 배열 반환
     - value가 없을 경우, 기존 문자열을 배열에 담아 반환
     - value가 빈 문자열일 경우, 각 문자로 나눈 배열을 반환(공백 포함)
     - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환
  3. replace : 해당 문자열을 대상 문자열로 교체해 반환
     - str.replace(from, to) : 문자열에 from값이 존재할 경우, 1개만 to 값으로 교체해 반환
     - str.replaceAll(from, to) : 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체해 반환
  4. trim : 문자열의 좌우 공백 제거해 반환(`trimStart`, `trimEnd`)
     - str.trim() : 문자열 시작과 끝의 모든 공백문자를 제거한 문자열 반환
     - str.trimStart() : 문자열 시작의 공백문자를 제거한 문자열 반환
     - str.trimEnd() : 문자열 끝의 공백문자를 제거한 문자열 반환

```javascript
// 1. includes
const str = 'a santa at nasa'

str.includes('santa')		// true
str.includes('asan')		// false

// 2. split
const str2 = 'a cup'

str2.split()					//['a cup']
str2.split('')				//['a', ' ', 'c', 'u', 'p']
str2.split(' ')				//['a', 'cup']

// 3. replace
const str3 = 'a b c d'

str3.replace(' ', '-')			//'a-b c d'
str3.replaceAll(' ', '-')		//'a-b-c-d'

// 4. trim
const str4 = '    hello    '

str4.trim()							// 'hello'
str4.trimStart()				// 'hello    '
str4.trimEnd()					// '    hello'
```



# 배열(Arrays)

- 배열의 정의

  : 키와 속성들을 담고 있는 참조 타입의 객체

- 특징

  1. 순서를 보장하는 특징이 있음
  2. 주로 대괄호를 이용해 생성, 0을 포함한 양의 정수 인덱스로 특정 값 접근 가능
  3. 배열의 길이는 `array.length` 형태로 접근 가능

- 배열 관련 주요 메서드(기본)
  1. reverse : 원본 배열의 요소들의 순서를 반대로 정렬
  2. push & pop : 배열의 가장 **뒤**에 요소 추가 or 제거
  3. unshift & shift : 배열의 가장 **앞**에 요소 추가 or 제거
  4. includes : 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환
  5. indexOf : 배열에 특정 값이 존재하는지 판별 후 인덱스 반환(없을 경우 -1 반환)
  6. join : 배열의 모든 요소를 구분자를 이용해 연결(구분자 생략 시 쉼표 기준)

```javascript
// 1. reverse

const numbers = [1, 2, 3, 4, 5]
numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]

// 2. push & pop
numbers.push(100)
console.log(numbers) // [5, 4, 3, 2, 1, 100]
numbers.pop()
console.log(numbers) // [5, 4, 3, 2, 1]

// 3. unshift & shift
numbers.unshift(100)
console.log(numbers) // [100, 5, 4, 3, 2, 1]
numbers.shift()
console.log(numbers) // [5, 4, 3, 2, 1]

// 4. includes
console.log(numbers.includes(1))		// true
console.log(numbers.includes(100))	// false

// 5. indexOf
let result

result = numbers.indexOf(3)
console.log(result)							// 2
result = numbers.indexOf(100)
console.log(result)							// -1

// 6. join

let answer

answer = numbers.join()
console.log(answer)					// 5,4,3,2,1
answer = numbers.join('')	
console.log(answer)					// 54321
answer = numbers.join(' ')
console.log(answer)					// 5 4 3 2 1
answer = numbers.join('-')
console.log(answer)					// 5-4-3-2-1
```

- Spread opeator
  - `...array` 사용 시 배열 내부에서 배열 전개 가능
  - 얕은 복사 방지에 활용 가능

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray)		// [0, 1, 2, 3, 4]
```

- 배열 관련 주요 메서드(심화)

  : 배열을 순회하며 특정 로직을 수행, 메서드 호출 시 인자로 callback 함수(어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수)를 받는 것이 특징

  1. forEach : 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
     - 콜백 함수는 3개의 매개변수로 구성(element: 배열의 요소, index : 배열 요소의 인덱스, array:배열 자체)
     - **반환 값이 없는 메서드**
  2. map : **콜백 함수의 반환 값**을 요소로 하는 **새로운 배열 반환**
     - 기존 배열 전체를 다른 형태로 바꿀 때 유용
  3. filter : **콜백 함수의 반환 값이 참인 요소**들만 모아 **새로운 배열 반환**
     - 기존 배열의 요소들을 필터링할 때 유용
  4. reduce : **콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환**
     - acc : 이전 콜백 함수의 반환 값이 누적되는 변수
     - initialValue(선택) : 최초 콜백 함수 호출 시 acc에 할당되는 값, default는 배열의 첫 번쨰 값
     - 빈 배열의 경우 initialValue 제공하지 않으면 에러 발생
  5. find : 콜백 함수의 **반환 값이 참이면 해당 요소를 반환**
     - 조건을 만족하는 첫 번째 요소를 반환
     - 찾는 값이 배열에 없으면 undefined 반환
  6. some : 배열의 **요소 중 하나라도 판별 함수를 통과**하면 참을 반환
     - 모든 요소가 통과하지 못하면 거짓 반환
     - 빈 배열은 항상 거짓 반환
  7. every : 배열의 **모든 요소가 판별 함수를 통과**하면 참을 반환

```javascript
// 1. forEach
const fruits = ['딸기', '수박', '참외', '메론', '사과']

fruits.forEach((fruit, index) => {
  console.log(fruit, index)
})
// 딸기 0
// 수박 1
// 참외 2
// 메론 3
// 사과 4

// 2. map
const number = [1, 2, 3, 4, 5]
const doubleNum = number.map((num) => {
  return num * 2
})

console.log(doubleNum)		// [2, 4, 6, 8, 10]

// 3. filter
const oddNums = number.filter((num, index) => {
  return num % 2
})
// ^ 콜백 함수의 반환 값이 참 = 나머지가 있음 = 홀수 => 홀수만 모아 새로운 배열 반환
console.log(oddNums)			// [1, 3, 5]

// 4. reduce
const result = numbers.reduce((acc, num) => {
  return acc + num
}, 0)
// ^ initialValue

console.log(result)		// 15

// 5. find
const avengers = [
  { name : 'Tony', age : 45},
  { name : 'Steve', age : 32},
  { name : 'Thor', age : 400},
  		// ^ 객체이기 때문에 속성에 값을 할당할 때는 : 사용, = 사용하지 않음!!
]

const ans = avengers.find((avenger) => {
  return avenger.name === 'Tony'
})

console.log(ans) 		// {name: 'Tony', age: 45}

// 6. some
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
  return num % 2 === 0
})
console.log(hasEvenNumber)		// false

const hasOddNumber = numbers.some((num) => {
  return num % 2
})
console.log(hasOddNumber)			// true

// 7. every
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
  return num % 2 === 0
})
console.log(isEveryNumberEven)		// true

const isEveryNumberOdd = numbers.every((num) => {
  return num % 2
})
console.log(isEveryNumberOdd)			// false
```

- 배열 순회 방법 비교
  1. for loop
     - 모든 브라우저 환경에서 지원 
     - 인덱스 활용해 배열의 요소에 접근
     - break, continue 사용 가능
  2. for ... of
     - 일부 오래된 브라우저 환경에서 지원 X
     - 인덱스 없이 배열의 요소에 바로 접근 가능
     - break, continue 사용 가능
  3. forEach
     - 대부분의 브라우저 환경에서 지원
     - **break, continue 사용 불가능**

```javascript
const chars = ['A', 'B', 'C', 'D']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}
// 0 A
// 1 B
// 2 C
// 3 D

// for ... of
for (const char of chars) {
  console.log(char)
}
// A
// B
// C
// D

// forEach
chars.forEach((char, idx) => {
  console.log(idx, char)
})
// 0 A
// 1 B
// 2 C
// 3 D

chars.forEach(char => {
  console.log(char)
})
// A
// B
// C
// D
```