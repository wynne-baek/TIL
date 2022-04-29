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

   