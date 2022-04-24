# DRF

## Serialization

- 직렬화 : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- Serializers in Django : 쿼리셋, Model Instance와 같은 복잡한 데이터를 JSON, XML등의 유형으로 쉽게 변환할 수 있는 파이썬 데이터 타입으로 만들어줌

## DRF(Django REST Framework)

### DRF

- Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
- DRF의 Serializer는 Django의 Form, ModelForm 클래스와 매우 유사하게 구성 및 작동

#### 설치과정

1. ```bash
   $ pip install djangorestframework
   ```

2. ```python
   #settings.py
   
   INSTALLED_APPS = [
     ...
     'rest_framework'
   ]
   ```

#### 사용 방법

- Article 모델에 맞춰 자동으로 필드를 생성해 serialize해주는 ModelSerializer 사용

  ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  from .models import Article
  
  class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Article
      fields = '__all__'
  ```

- DRF Response()를 활용해 serialize된 JSON 객체 응답

  ```python
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.reponse import Response
  from .serializers import ArticleSerializer
  
  @api_view(['GET'])
  def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Responser(serializer.data)
  ```

### Single Model

#### 'many' argument

- many=True : Serializing multiple objects
- 단일 인스턴스 대신 쿼리셋 등을 직렬화하기 위해서는 serializer를 인스턴스화 할 때 many=True를 키워드 인자로 전달해야함

#### api_view

- 기본적으로  GET 메서드만 허용, 다른 메서드 요청에 대해서는 405 Method Not Allowed 응답
- View 함수가 응답해야하는 HTTP 메서드의 목록을 리스트의 인자로 받음

- DRF에서는 선택이 아닌 **필수적으로 작성**해야 해당 함수가 정상적으로 동작

#### Status Codes in DRF

- Status 코드를 명확하고 읽기 쉽게 만드는데 사용할 수 있는 정의된 상수 집합을 제공
- Status 모듈에 HTTP status code 집합이 모두 포함되어 있음
- 단순히 status=201 같은 표현도 사용은 가능하나 권장 X

```python
from rest_framework import status

def example_list(request):
  return Response(serializer.data, status=status.HTTP_201_CREATED)
																									# ^ 이거
```

#### 'raise_exception' argument

- raising an exception on invalid data 
- is_valid() 는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP status code 400을 응답으로 반환함