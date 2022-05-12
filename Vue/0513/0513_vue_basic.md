# 0513_TIL

## vue basic syntax

### Template Syntax

- Interpolation(보간법)

  1. Text

     Ex) `<span>메시지: {{ msg }}</span>`

  2. Raw HTML

     Ex) `<span v-html="rawHtml"></span>`

  3. attributes

     Ex) `<div v-bind:id="dynamicId"></div>`

  4. JS 표현식

     Ex) `{{ number +  }}`, `{{ message.split('').reverse().join('') }}`

- Directive(디렉티브)

  - v-접두사가 있는 특수 속성
  - 속성 값은 단일 JS표현식(v-for 예외)
  - 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할

  - 전달인자(Argument)
    - `:` 콜론을 통해 전달인자를 받을 수 있음
  - 수식어(Modifiers)
    - `.` 점으로 표시되는 특수 접미사
    - directive를 특별한 방법으로 바인딩 해야함을 나타냄

### v-text

```vue
<body>
  <div id="app">
    <p, v-text="message"></p>
    <!-- 위 아래는 같은 것 -->
    <p>{{ message }}</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  // ^ CDN
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello',
      }
    })
  </script>
</body>
```

- 엘리먼트의 textContent를 업데이트
- 내부적으로 interpolation 문법이 v-text로 컴파일 됨

### v-html

```vue
<body>
  <div id="app">
    <div>Hello</div>
    <div v-html="myHtml"></div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el : '#app',
      data: {
        myHtml : '<b>Hello<b/>',
      }
    })
  </script>
</body>
```

- 엘리먼트의 innerHTML을 업데이트
  - XSS 공격에 취약할 수 있음
- 임의로 사용자로부터 입력받은 내용은 v-html **절대 사용 금지**

### v-show

```vue
<body>
  <div id="app">
    <p v-show="isTrue">true</p>
    <p v-show="isFalse">false</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        isTrue: true,
        isFalse: false,
      }
    })
  </script>
</body>
```

- 조건부 렌더링
- 요소는 항상 렌더링되고 DOM에 남아있음
- 단순히 엘리먼트에 display CSS 속성을 토글하는 것

### v-if, v-else-if, v-else

```vue
<body>
  <div id="app">
    <!-- 1 -->
    <div v-if="seen">seen이 True일 때만 렌더링</div>
    
    <!-- 2 -->
    <div v-if="myType === 'A'">A</div>
    <div v-else-if="myType === 'B'">B</div>
    <div v-else-if="myType === 'C'">C</div>
    <div v-else>Not A/B/C</div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        seen: true,
        myType: 'D'
      }
    })
  </script>
</body>
```

- 조건부 렌더링
- 조건에 따라 요소를 렌더링
- directive의 표현식이 true일 때만 렌더링
- 엘리멘트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨

### v-for

```vue
<body>
  <div id="app">
    <div v-for="fruit in fruits">
      {{ fruit }}
    </div>

    <div v-for="(fruit, index) in fruits" :key="`fruit-${index}`">
      {{ fruit }}
    </div>

    <div v-for="todo in todos" :key="todo.id">
      {{ todo.title }} : {{ todo.completed }}
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data : {
        fruits : ['apple', 'banana', 'coconut'],
        todos : [
          { id:1, title:'todo1', completed: true},
          { id:2, title:'todo2', completed: false},
          { id:3, title:'todo3', completed: true},
        ],
      }
    })
  </script>
</body>
```

- 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러번 렌더링
- Item in items 구문 사용
- Item 위치의 변수를 각 요소에서 사용할 수 있음
  - 객체의 경우 key
- v-for 사용 시 반드시 key 속성을 각 요소에 작성
- v-if와 함께 사용 시 v-for 우선순위가 더 높음
  - **단, 가능하면 v-if와 v-for를 동시에 사용하지 말 것**

### v-on

- 엘리먼트에 이벤트 리스너 연결
- 이벤트 유형은 전달인자로 표시
- 특정 이벤트 발생 시 주어진 코드가 실행
- `v-on:click` -> `@click` shorthand 사용 가능

### v-bind

- HTML 요소의 속성에 Vue 상태 데이터를 값으로 할당
- Object 형태로 사용하면 value가 true인 key가 class qkdlseld rkqtdmfh gkfekd
  - `v-bind:href` -> `:href` shorthand 사용 가능

### v-model

- HTML form 요소의 값과 data를 양방향 바인딩
- 수식어
  - .lazy : input 대신 change 이벤트 이후에 동기화
  - .number : 문자열을 숫자로 변경
  - .trim : 입력에 대한 trim을 진행