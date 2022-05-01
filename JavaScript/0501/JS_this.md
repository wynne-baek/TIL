# JS_this

## `Window` ? or `object` ?

- JS의 this는 실행 문맥에 따라 다른 대상을 가리킴
  1. class 내부의 생성사 함수 => this는 생성되는 객체
  2. 메서드(`객체.메서드명()`으로 호출 가능한 함수) => this는 해당 메서드가 소속된 객체를 가리킴
  3. 이외의 모든 경우는 최상위 객체(`window`)를 가리킴

- function 키워드와 화살표 함수 차이

  ```javascript
  const obj = {
    PI : 3.14,
    radiuses : [1, 2, 3, 4, 5],
    printArea : function () {
      this.radiuses.forEach( ---- function (r) {
        console.log(this.PI * r * r)
      } ----.bind(this))
      // ^ bind 까지 묶여있어야 같은 동작을 한다.
    },
  }
  ```

  ```javascript
  const obj = {
    PI : 3.14,
    radiuses : [1, 2, 3, 4, 5],
    printArea : function () {
      this.radiuses.forEach(---- (r) => {
        console.log(this.PI * r * r)
      } ----)
    }, 
  }
  ```

  - `this.radiuses`는 메서드 소속이기 때문에 정상적으로 접근 가능
  - forEach의 콜백함수의 경우 메서드가 아님
  - 때문에 콜백함수 내부의 this는 window가 되어 this.PI는 정상적으로 접근 불가능
  - 이 콜백함수 내부에서 this.PI에 접근하기 위해 함수객채 `.bind(this)` 메서드를 사용
  - 번거로운 bind 과정을 없앤 것이 화살표 함수

## 결론

- 함수 내부에 this 키워드가 존재할 경우 => 화살표 함수와 function키워드로 선언한 함수가 다르게 동작
- 함수 내부에 this 키워드가 존재하지 않을 경우 => 완전히 동일하게 동작



# lodash

- 모듈성, 성능 및 추가 기능을 제공하는 JS 유틸리티 라이브러리
- 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수 제공
- 예시 : reverse, sortBy, range, random, cloneDeep ...