# 0412 django_auth

## 01. Django authentication system

- Django.contrib.auth에 django contrib module로 제공

- 필수 구성은 setting.py에 이미 포함되어 있으며, INSTALLED_APPS 설정의 두 항목으로 구성

  1. django.contrib.auth

     : 인증 프레임워크의 핵심과 기본 모델 포함

  2. django.contrib.contenttypes

     : 사용자가 생성한 모델과 권한을 연결할 수 있음

- Django는 인증과 권한 부여를 함께 제공(처리)

## 02. account CRUD

### 0. 기본 로직

(1) urls.py 작성

(2) views.py 작성

(3) 템플릿 생성 or 수정

### 1. app 생성

```
$ python manage.py startapp accounts
```

- app 이름이 반드시 accounts일 필요는 없음
- but, auth 관련해 django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 **accounts로 지정하는 것을 권장**

### 2. 로그인

세션을 create하는 로직

- django 자체적으로 built-in forms 제공
- AuthenticationForm
  - 사용자 로그인을 위한 form
  - request를 첫번째 인자로 취함

- [login 함수](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in-1) : login(request, user, backend=None)
  - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 login() 함수가 필요
  - 세션에 user의 id 저장(==로그인)

```python
# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
#views에 있는 login과 이름이 같기 때문에 auth_login으로 별명을 설정해서 import

def login(request):
  # POST 요청이면, 채워진 form을 확인하자
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    # 유효성 검사, 유효하다면 login 함수 실행
    if form.is_vaild():
      auth_login(request, form.get_user())
      return redirect('articles:index')
  # POST가 아닌 요청이면, form을 보여주자!
  else:
    form = AuthenticationForm()
  context = {
    'form' : form
  }
  return render(request, 'accoounts/login.html', context)
```

- get_user()
  - AuthenticationForm의 인스턴스 메서드
  - user_cache는 생성 시 None, 유효성 검사 통과 시 로그인한 사용자 객체로 할당
  - 인스턴스 유효성 먼저 확인, 유효할 때만 user 제공
- Authentication data in templates
  - Context processors : 템플릿이 렌더링 될 때, 자동으로 호출 가능한 컨텍스트 데이터 목록
    - 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함됨
  - Users
    - 템플릿 RequestContext를 렌더링할 때, 현재 로그인한 사용자를 나타내는 auth.User 인스턴스(로그인하지 않은 경우, AnonymousUser 인스턴스)
    - 템플릿 변수 `{{ user }}`에 저장됨

### 3. 로그아웃

세션을 Delete하는 로직

- [logout(request) 함수](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out) : logout(request)
  - HttpRequest 객체를 인자로 받고 반환값 없음
  - 사용자가 로그인하지 않은 경우 오류 발생 X
  - 현재 요청에 대한 session data를 DB에서 완전히 삭제, 클라이언트의 쿠키에서도 sessionid 삭제
  - 다른 사람이 동일한 웹 브라우저를 사용해 로그인할 경우, **이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함**

```python
# views.py

from django.contrib.auth import logout as auth_logout
#views에 있는 login과 이름이 같기 때문에 auth_login으로 별명을 설정해서 import

def logout(request):
  auth_logout(request)
  return redirect('articles:index')
```

### * 로그인 사용자에 대한 접근 제한

#### (1) is_authenticated attribute

- User model의 속성 중 하나

- 모든 User 인스턴스에 대해 항상 True, AnonymousUser에 대해 항상 False

- 사용자가 인증되었는지 여부를 알 수 있는 방법

- 일반적으로 request.user에서 이 속성 사용, 미들웨어 통과했는지 확인

- 단, 권한과는 관련 X, 사용자의 활성화 상태, 유효한 세션 보유 여부도 확인 X

- 적용

  (1) 로그인, 비로그인 상태에서 출력되는 링크 다르게 설정

  (2) 인증된 사용자(로그인 상태) 라면 로그인 로직 수행할 수 없도록 처리

  (3) 인증된 사용자(로그인 상태) 만 로그아웃 로직을 수행할 수 있도록 처리

  (4) 인증된 사용자(로그인 상태) 만 게시글 작성 링크를 볼 수 있도록 처리

#### (2) Login_required decorator

- 사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect
- 사용자가 로그인되어 있으면, 정상적으로 view 함수를 실행
- 인증 성공 시 redirect되어야 하는 경로는 'next'라는 쿼리 문자열 매개변수에 저장됨
  - next : 기존에 요청했던 주소록 redirect하기 위해 주소를 keep, but 별도 처리 없으면 view에 설정한 redirect 경로로 이동