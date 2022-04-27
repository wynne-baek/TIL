# JS_function

## 함수

- 참조 타입 중 하나로 `function` 타입에 속함
- 함수 정의 방법 2가지
  1. 함수 선언식
  2. 함수 표현식
- JS의 함수는 일급 객체에 해당
  - 일급 객체의 조건
    1. 변수에 할당 가능
    2. 함수의 매개변수로 전달 가능
    3. 함수의 반환 값으로 사용 가능

### 함수 선언식(function statement, declaration)

- 함수의 이름과 함께 정의하는 방식
- 구성 요소
  1. 함수의 이름
  2. 매개변수
  3. 몸통(중괄호 내부)

```javascript
function add(num1, num2){
  return num1 + num2
}

add(1, 2)		// 3
```

### 함수 표현식(function expression)

- 함수를 표현식(어떤 하나의 값으로 결정되는 코드) 내에서 정의하는 방식
- 함수의 이름 생략하고 **익명 함수**로 정의 가능
  - 익명 함수 : 이름이 없는 함수 - 함수 표현식에서만 가능
- 구성 요소
  1. 함수의 이름(생략 가능)
  2. 매개 변수
  3. 몸통(중괄호 내부)

```JavaScript
const add = function (num1, num2) {
  return num1 + num2
}

add(1, 2)		// 3
```

### 기본 인자

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

```javascript
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting()		// Hi Anonymous
```

### 매개변수와 인자의 개수 불일치 허용

```javascript
// 1. 매개변수보다 인자의 개수가 많을 경우
const noArgs = function () {
    return 0 
}

noArgs(1, 2, 3)			 // 0

const twoArgs = function(arg1, arg2){
    return [arg1, arg2]
}

twoArgs(1, 2, 3)		 // [1, 2]

// 2. 매개변수보다 인자의 개수가 적을 경우
const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

threeArgs()				//[undefined, undefined, undefined]
threeArgs(1)			//[1, undefined, undefined]
threeArgs(1, 2)		//[1, 2, undefined]
```

### Rest parameter

- 함수가 정해지지 않은 수의 매개변수를 배열로 받음(python의 *args(언패킹연산자)와 유사)

```javascript
const rest = function (arg1, arg2, ...restArgs){
  																// ^ 요 점 3개 필수, 없으면 그냥 변수명으로 처리됨
    return [arg1, arg2, restArgs]
}

rest(1, 2, 3, 4, 5)		//[1, 2, [3, 4, 5]]
rest(1, 2)						//[1, 2, []]
			// ^ rest parameter로 처리한 매개변수에 인자 넘어오지 않으면, 빈 배열로 처리
```

### spread operator

- 배열 인자를 전개해 전달할 수 있음

```javascript
const spread = function (arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
}

const nums = [1, 2, 3]
spread(...nums)			// 6
		 // ^ 점 세개를 활용해 nums라는 배열의 인자를 전개해서 전달한 것!
```