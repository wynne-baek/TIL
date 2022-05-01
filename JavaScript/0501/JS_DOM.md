# JS_DOM 조작

## DOM 조작 순서

1. 선택
2. 변경

## DOM 관련 객체의 상속 구조

- EventTarget : Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node : 여러 가지 DOM 타입들이 상속하는 인터페이스
- Element 
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 Node와 그 부모인 EventTarget의 속성을 상속 
- Document
  - 브라우저가 불러온 웹 페이지
  - DOM 트리의 진입점 역할을 수행
- HTMLElement
  - 모든 종류의 HTML 요소
  - 부모 element의 속성 상속

## DOM 선택

### 선택 관련 메서드

1. `document.querySelector(selector)` - 단일 element
   - 제공한 선택자와 일치하는 element 하나 선택
   - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)

2. `document.querySelectorAll(selector)` - NodeList
   - 제공한 선택자와 일치하는 여러 element를 선택
   - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
   - 지정된 셀렉터에 일치하는 노드리스트를 반환

- querySelector(), querySelectorAll()을 사용하는 이유
  - id, class, tag 선택자 등을 모두 사용 가능해 더 구체적이고 유연하게 선택 가능
  - 예시) `document.querySelector('#id')`, `document.querySelectorAll('.class')`

### HTMLCollection & NodeList

- 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공(유사 배열)
- HTML Collection
  - Name, id, index 속성으로 각 항목에 접근 가능
- NodeList
  - index로만 각 항목에 접근 가능
  - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
- 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, **querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음**

### Collection

- Live Collection
  - 문서가 바뀔 때 실시간으로 업데이트 됨
  - DOM의 변경사항을 실시간으로 collection에 반영
- Static Collection (non-live)
  - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
  - querySelectorAll()의 반환 NodeList만 static collection

### 변경 관련 메서드(Creation)

- `document.createElement()` : 작성한 태그 명의 HTML 요소를 생성해 반환

### 변경 관련 메서드(append DOM)

- `element.append()`
  - 특정 부모 Node의 자식 Nodelist 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - 여러 개의 Node 객체, DOMString을 추가할 수 있음
  - 반환 값이 없음
- `Node.appendChild()`
  - 한 노드를 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 삽입(노드만 추가 가능)
  - 한 번에 오직 하나의 노드만 추가 가능
  - 만약 주어진 노드가 이미 문서에 존재하는 다른 노드를 참조한다면 새로운 위치로 이동

- 차이점(서술형)
  - append 사용시 DOMString 객체를 추가 가능, appendChild()는 노드 객체만 허용
  - append는 반환값 없음, appendChild()는 추가된 노드 객체를 반환
  - append는 여러 노드 객체와 문자열 추가 가능, appendChild는 하나의 노드 객체만 추가 가능

### 변경 관련 속성(property)

- `Node.innerText`
  - 노드 객체와 그 자손의 텍스트 컨텐츠를 표현(해당 요소 내부의 raw data)
  - 즉, 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
- `Element.innerHTML`
  - 요소 내에 포함된 HTML 마크업을 반환
  - XSS 공격에 취약하므로 사용 시 주의

### 삭제 관련 메서드

- `ChildNode.remove()` : 노드가 속한 트리에서 해당 노드를 제거
- `Node.removeChild()`
  - DOM에서 자식 노드를 제거하고 제거된 노드를 반환
  - 노드는 인자로 들어가는 자식 노드의 부모노드

### 속성 관련 메서드

- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값을 반환
  - 인자는 값을 얻고자 하는 속성의 이름

## Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스 클릭, 키보드 클릭 등 사용자 행동으로 발생할 수 있고
  - 특정 메서드를 호출해 프로그래밍적으로도 만들 수 있음

### Event handler - `addEventListener()`

- `EventTarget.addEventListener()`
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능

- `target.addEventListener(type, listener[])`
  - Type : 반응할 이벤트 유형(대소문자 구분 문자열)
  - Listener : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체, EventListener의 인터페이스 or JS function 객체(콜백함수)여야 함

### Event 취소

- `event.preventDefault()`
- 현재 이벤트의 기본 동작 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
- 취소할 수 없는 이벤트도 존재