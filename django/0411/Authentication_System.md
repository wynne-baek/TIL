# Authentication_System

## 00. 기본 개념

- Authentication & Authorization

  - Authentication : 인증

    : 신원 확인, 사용자가 누구인지 확인하는 것

  - Authorization : 권한, 허가

    : 권한 부여, 인증된 사용자가 수행할 수 있는 작업을 결정

- 쿠키와 세션

  - HTTP : Hyper Text Tansfer Protocol
    - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
    - 웹에서 이루어지는 모든 데이터 교환의 기초
    - 클라이언트 - 서버 프로토콜이기도 함
  - 특징
    - 비연결지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
    - 무상태 : 연결을 끊는 순간 클라이언트, 서버 간 통신 끝, 상태 정보 유지 X
    - 클라이언트와 서버가 주고 받는 메시지는 서로 완전히 독립적

  **=> 클라이언트와 서버의 지속적인 관계 유지를 위해 쿠키와 세션이 존재**

  - 쿠키 : 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

    - 사용자가 웹사이트에 방문할 경우, 해당 웹사이트 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
      - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
      - 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키 함께 전송
    - HTTP 쿠키는 상태가 있는 세션을 만들어 줌
    - 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지 판단할 때 주로 사용
      - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
      - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

    **=> 웹페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함께 전송**

    - 쿠키의 사용 목적
      1. 세션 관리 :  로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
      2. 개인화 : 사용자 선호, 테마 등의 설정
      3. 트래킹 : 사용자 행동을 기록 및 분석

  - 세션 : 사이트와 특정 브라우저 사이의 상태를 유지시키는 것

    - 클라이언트가 서버에 접속 시 서버가 특정 session id를 발급하고, 클라이언트는 받은 session id를 쿠키에 저장
      - 클라이언트가 다시 서버 접속 시, 요청과 함께 쿠키를 서버에 전달
      - 쿠키는 요청때마다 서버에 함께 전송, 서버에서 session id 를 확인해 알맞은 로직을 처리
    - ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장

  - 쿠키 수명

    1. Session Cookies
       - 현재 세션 종료 시 삭제
       - 브라우저가 현재 세션이 종료되는 시기를 정의
    2. Persistent Cookies or Permanent cookies
       - Expires 속성에 지정된 날짜 혹은 Max-age 속성에 지정된 기간이 지나면 삭제