# Javascript Base

## Intro

- JavaScript의 필요성
  1. 브라우저 화면을 동적으로 만들기 위함
  2. 브라우저를 조작할 수 있는 유일한 언어

## Browser

- 브라우저에서 할 수 있는 일

  - DOM 조작

    : 문서(HTML 조작)

  - BOM 조작

    : navigator, screen, location, frames, history, XHR

  - JavaScript Core(ECMAScript)

    : Data Structure(Object, Array), Conditional Expression, Iteration

- DOM(Document Object Model)

  - HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
  - 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급해 다루는 논리적 트리 모델
  - 문서가 객체(Object)로 구조화, key로 접근 가능
  - 단순한 속성 접근, 메서드 활용을 넘어 프로그래밍 언어적 특성을 활용한 조작 가능
  - 주요객체
    - Window(브라우저 탭, 최상위 객체)
    - document(페이지 컨텐츠의 Entry Point, `<head>`, `<body>`등과 같은 수많은 다른 요소 포함)
    - navigator, location, history, screen
  - 파싱(Parsing) : 구문 분석, 해석 => 브라우저가 문자열을 해석해 DOM Tree로 만드는 과정

- BOM(Browser Object Model)
  - 자바스크립트가 브라우저와 소통하기 위한 모델
  - 브라우저의 창이나 프레임을 추상화해 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

## 기본 문법

### 변수와 식별자

- 변수 선언 키워드(let, const)
  - let
    - **재할당 할 예정인** 변수 선언 시 사용
    - 변수 **재선언 불가능**
    - 블록 스코프
  - const
    - **재할당 할 예정이 없는** 변수 선언 시 사용
    - 변수 **재선언 불가능**
    - 블록 스코프

- 선언, 할당, 초기화

  - 선언 : 변수를 생성하는 행위 또는 시점
  - 할당 : 선언된 변수에 값을 저장하는 행위 또는 시점
  - 초기화 : 선언된 변수에 **처음으로** 값을 저장하는 행위 또는 시점

  ```javascript
  let foo
  console.log(foo)		//선언
  
  foo = 11
  console.log(foo)		//할당
  
  let bar = 0
  console.log(bar)		//선언 + 할당
  ```

- 블록 스코프(block scope)

  - if, for, 함수 등의 중괄호 내부
  - 블록 스코프에서 가지는 변수는 **블록 바깥에서 접근 불가능**

- var
  - var로 선언한 변수는 재선언, 재할당 모두 가능
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
  - 호이스팅 되는 특성으로 인해 문제 발생 가능성 있어 const와 let 사용을 권장함
    - 호이스팅 : 변수를 선언 이전에 참조할 수 있는 현상
    - 변수 선언 이전의 위치에서 접근 시 undefined 반환
  - 함수 스코프 : 함수의 중괄호 내부를 가리키며, 함수 스코프를 가지는 변수는 **함수 바깥에서 접근 불가능**

### 데이터 타입

- 종류
  - 원시 타입(Primitive type)
    - 객체가 아닌 기본 타입
    - 변수에 해당 타입의 값이 담김
    - 다른 변수에 복사 시 실제 값이 복사됨
  - 참조 타입(Reference type)
    - 객체 타입의 자료형
    - 변수에 해당 객체의 참조 값이 담김
    - 다른 변수에 복사할 때 참조 값이 복사됨

#### Primitive type

1. 숫자 타입(Number)
   - 정수, 실수 구분 없는 하나의 숫자 타입
   - 부동소수점 형식을 따름
   - NaN(Not-A-Number) : 계산 불가능할 경우 반환되는 값(산술 연산 불가)

2. 문자열 타입(String)
   - 텍스트 데이터를 나타내는 타입
   - 16비트 유니코드 문자의 집합
   - 작은따옴표, 큰따옴표 모두 가능
   - 템플릿 리터럴(Template Literal)
     - ES6부터 지원, ``(backtick)으로 표현, ${expression} 형태로 표현식 삽입 가능
     - 파이썬의 f스트링과 비슷한듯!

3. undefined
   - 변수의 값이 없음을 나타내는 데이터 타입
   - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined 할당

4. null

   - **변수의 값이 없음을 의도적으로 표현**할 때 사용하는 데이터 타입
   - 원시 타입이지만 typeof 연산자의 결과는 object 로 표현됨

   ```javascript
   // undefined 타입과 null 타입 비교
   
   typeof undefined	// undefined
   
   typeof null				// object
   ```

5. Boolean 타입

   - 논리적 참 또는 거짓을 나타내는 타입
   - true, false로 표현
   - 조건문 또는 반복문에서 유용하게 사용
     - boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true/false로 변환됨 

#### Reference Type(참조 타입)

- 함수, 배열, 객체 ...

### 연산자

#### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원

```javascript
let x = 0

x += 10		// 10
x -= 3		// 7
x *= 10		// 70
x /= 10		// 7
x++				// 8
x--				// 7
```

#### 비교 연산자

- 피연산자들을 비교하고 결과값을 Boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용해 표준 사전 순서를 기반으로 비교

#### 동등 비교 연산자(==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- but, 예상치못한 결과가 발생 가능, **특별한 경우 제외하고 사용 X**

#### 일치 비교 연산자(===)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean값을 반환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
  - 엄격한 비교 : 두 비교 대상의 타입과 값이 모두 같은지 비교하는 방식
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

#### 논리 연산자

- and : `&&`
- or : `||`
- not : `!`
- 단축 평가 지원
  - false && true => false
  - true || false => true

#### 삼항 연산자

- 세 개의 피연산자를 사용해 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론 앞의 값, 거짓이면 콜론 뒤의 값 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- 한 줄 표기 권장

```javascript
console.log(true ? 1 : 2)		// 1
console.log(false ? 1 : 2)	// 2

const result = Math.PI > 4 ? 'YES' : 'NO'
console.log(result) 				// NO
```

### 조건문

- 종류
  - 'if' statement
    - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
  - 'switch' statement
    - 조건 표현식의 결과값이 어느 값에 해당하는지 판별
    - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용(조건이 많아질 경우, if문보다 가독성이 나을 수 있음)

#### if statement

- `if`, `else if`, `else`

  - 조건은 소괄호 안에 작성
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성

  ```javascript
  const nation = 'Korea'
  
  if (nation === 'Korea'){
    console.log('안녕하세요')
  }
  else if (nation === 'France'){
    console.log('Bonjour')
  }
  else {
    console.log('Hello')
  }
  ```

#### switch statement

- `switch`

  - 표현식의 결과값을 이용한 조건문
  - 표현식의 결과값과 case 문의 오른쪽 값을 비교
  - break / default 문은 선택적으로 사용 가능
  - break 문이 없는 경우, break 문을 만나거나 default 문을 실행할때까지 다음 조건문 실행
  - 블록 스코프 생성

  ```javascript
  // break 있는 경우
  const nation = 'Korea'
  
  switch(nation){
    case 'Korea':{
      console.log('안녕하세요')
      break
    }
    case 'France':{
      console.log('Bonjour')
      break
    }
    default:{
      console.log('Hello')
  	}
  }
  
  // break 없는 경우
  const nation = 'Korea'
  
  switch(nation){
    case 'Korea':{
      console.log('안녕하세요')
    }
    case 'France':{
      console.log('Bonjour')
    }
    default:{
      console.log('Hello')
  	}
  }
  // 없는 경우, Fall-through되어 모두 출력됨
  ```

### 반복문

#### 종류와 특징

- while
- for
- for... in
  - 객체의 속성들을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장 X
- for... of
  - 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용
    - 반복 가능한 객체 종류 : Array, Map, Set, String

#### while

- 조건문이 참(true)인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
let i = 0

while (i < 6) {
  console.log(i)
  i += 1
}
```

#### for

- 세미콜론으로 구분되는 세 부분으로 구성
- initialization
  - 최초 반복문 진입 시 1회만 실행되는 부분

- condition
  - 매 반복 시행 전 평가되는 부분
- expression
  - 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성

```javascript
for (let i = 0; i < 6; i++){
  console.log(i)
}
// 0, 1, 2, 3, 4, 5
```

#### for ... in

- 객체의 속성들을 순회할 때 사용
- 배열도 순회 가능하지만 **권장하지 않음**
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
const capitals = {
  korea : 'Seoul',
  france : 'Paris',
  USA : 'Washington D.C.'
}

for (let capital in capitals) {
  console.log(capital)
}
// korea, france, USA
```

#### for... of

- 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits){
  fruit = fruit + '!'
  console.log(fruit)
}

for (const fruit of fruits){
  console.log(fruit)
}
```

