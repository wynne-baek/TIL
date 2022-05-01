# 객체(Objects)

- 객체의 정의와 특징
  - 객체는 속성의 집합, 중괄호 내부에 key와 value의 쌍으로 표현
  - key : 문자열 타입만 가능 * key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
  - value : 모든 타입 가능(함수 포함)
  - 객체 요소 접근은 점 or 대괄호로 가능 * key 이름에 띄어쓰기 같은 구분자 있으면 대괄호 접근만 가능

```javascript
const me = {
  name : 'jack', 
  phoneNumber : '01098765432', 
  'samsung products' : {
  buds : 'Galaxy', 
	phone : 'S20',
},
}

console.log(me.name)		// jack
console.log(me['samsung products'])		// {buds: 'Galaxy', phone: 'S20'}
console.log(me['samsung products'].buds) // Galaxy
```

## 객체 관련 ES6 문법

1. 속성명 축약 : 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능

   ```javascript
   const books = ['JS', 'Python']
   const magazine = ['Vogue', 'Science']
   
   const bookShop = {
     books,
     magazine,
   }
   
   console.log(bookShop)
   ```

2. 메서드명 축약 : 메서드 선언 시 function 키워드 생략 가능

   ```javascript
   const obj = {
     greeting() {
       console.log('Hi')
     }
   }
   
   obj.greeting()
   ```

3. 계산된 속성 : 객체를 정의할 때 key의 이름을 표현식으로 이용해 동적으로 생성 가능

   ```javascript
   const key = 'regions'
   const value = ['광주', '대전', '구미', '서울']
   
   const ssafy = {
     [key] : value,
   }
   
   console.log(ssafy)
   console.log(ssafy.regions)
   ```

4. 구조 분해 할당 : 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

   ```javascript
   const userInformation = {
     name : 'ssafy kim',
     userId : 'ssafyStudent1234',
     phoneNumber : '010-9923-2234',
     email : 'ssafy@ssafy.com'
   }
   
   const { name } = userInformation
   // const name = user.name
   // 위 두 코드가 같은 코드라는 것이 구조분해 할당의 핵심
   const { userId } = userInformation
   const { phoneNumber } = userInformation
   const { email } = userInformation
   
   const { name, userId } = userInformation
   ```

5. Spread operator : spread operator(...)를 사용하면 객체 내부에서 객체 전개 가능

   - 얕은 복사 방지에 활용 가능

   ```javascript
   const obj = {b : 2, c : 3, d : 4}
   const newObj = {a : 1, ...obj, e : 5}
   
   console.log(newObj)			// {a: 1, b: 2, c: 3, d: 4, e: 5}
   ```

## JSON(JavaScript Object Notation)

- key - value 쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입 => JS의 객체로 조작하기 위해 구문 분석 필수
- JSON 조작을 위한 두 가지 내장 메서드 제공
  1. JSON.parse() : JSON => 자바스크립트 객체
  2. JSON.stringify() : 자바스크립트 객체  => JSON

## 배열은 객체다

- 키와 속성들을 담고 있는 참조 타입의 객체!
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체