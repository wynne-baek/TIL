# 0413 Django_auth

### 두 데코레이터 사용 시 발생하는 구조적 문제 / 해결

```python
# articles/views.py

@login_required
@require_POST
def delete(request, pk):
  article = get_object_or_404(Article, pk=pk)
  article.delete()
  return redirect('articles:index')
```

- 위와 같이 `@require_POST` 작성된 함수에 `@login_required`를 함께 사용하는 경우 에러 발생
  - why? 로그인 이후 next 매개변수를 따라 해당 함수로 다시 redirect, 이 때 `@require_POST` 때문에 405 에러 발생
- 두 가지 문제 발생
  1. redirect 과정에서 POST 데이터의 손실
  2. redirect 요청은 POST 방식이 불가능하기 때문에 GET 방식으로 요청됨

- 해결

  -  `@login_required`는 GET method request를 처리할 수 있는 view 함수에서만 사용해야 함

  ```python
  # articles/views.py
  
  @require_POST
  def delete(request, pk):
    if request.user.is_authenticated:
    	article = get_object_or_404(Article, pk=pk)
    	article.delete()
    return redirect('articles:index')
  ```

## Accounts CRUD

### 01 회원가입(C)

- [UserCreationForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)

  : username과 password로 권한이 없는 새 user를 생성하는 ModelForm

  - 3개의 필드 (1)username (2)password1 (3)password2

    => `validate_password()`로 password가 일치하는지 확인

    =>`set_password()`로 사용자의 비밀번호 설정

```python
#accounts/views.py

from django.contrib.auth.forms import UserCreationFrom

@require_http_method(['GET', 'POST'])
def signup(request):
  # POST 요청일 경우
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    # 유효한지 확인
    if form.is_valid():
      # 회원가입 후 자동으로 로그인
      user = form.save()
      # ^ UserCreationForm의 save 메서드
      auth_login(request, user)
      return redirect('articles:index')
  # POST 이외의 요청일 경우, form을 보여주기
  else:
    form = UserCreationForm()
   context = {
     'form': form,
   }
  return render(request, 'accounts/signup.html', context)
```

### 02 회원 탈퇴(D)

: DB에서 사용자를 삭제하는 것과 같음

```python
# accounts/views.py

from django.views.decorators.http import require_POST

@require_POST
def delete(request):
  if request.user.is_authenticated:
    request.user.delete()
    #탈퇴하면서 해당 유저의 세션 데이터 함께 삭제 / 주의: 반드시 탈퇴 후 로그아웃 순으로 처리해야 함!!
    auth_logout(request)
  return redirect('articles:index')
```

### 03 회원정보 수정(U)

- [UserChangeForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserChangeForm)

  : 사용자의 정보 및 권한 변경을 위해 **admin 인터페이스에서 사용**되는 ModelForm

  - 단순하게 UserChangeForm 사용할 경우, admin 인터페이스에서 사용되는 ModelForm이기 때문에 일반 사용자가 접근해서는 안될 정보들까지 모두 수정 가능

  => UserChangeForm을 상속받아 CustomUserChangeForm이라는 서브 클래스 작성해 접근 가능한 필드를 조정해야 함

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
  
  class Meta:
    model = get_user_model()
    # 수정 시 필요한 필드만 선택해 작성
    fields = ('email', 'first_name', 'last_name')
```

- get_user_model()
  - 현재 프로젝트에서 활성화된 사용자 모델을 반환
  - ~~User 클래스 직접 참조~~ , **`django.contrib.auth.get_user_model()`을 사용해 참조해야 함!!!**

```python
# accounts/views.py

from .forms import CustomChangeForm

@login_required
@require_http_method(['GET', 'POST'])
def update(request):
  if request.method == 'POST':
    form = CustomChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return reirect('articles:index')
  else:
    form = CustomChangeForm(instance=request.user)
  context = {
    'form':form,
  }
  return render(request, 'accounts/update.html', context)
```

### 04 비밀번호 변경

- [PasswordChangeForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.PasswordChangeForm)

  : 사용자가 비밀번호를 변경할 수 있도록 하는 Form

  - 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
  - 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

```python
#accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      # 암호 변경 시 세션 무효화 방지
      update_session_auth_hash(request, form.user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/change_password.html', context)
```

- [PasswordChangeForm의 첫번째 인자가 user인 이유](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L374)

- 암호 변경 시 세션 무효화 방지

  - [`update_session_auth_hash(request, user)`](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.update_session_auth_hash)

    : 현재 요청과 새 session hash가 파생될 업데이트된 사용자 객체를 가져오고, session hash를 적절하게 업데이트

    - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태 유지 불가능

    => 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트 함