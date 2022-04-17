# DB 01

## Database

### DB

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료의 모음으로 그 내용을 고도로 구조화해 검색과 갱신의 효율화를 꾀한 것
- **몇 개의 자료 파일을 조직적으로 통합해 자료 항목의 중복을 없애고 자료를 구조화해 기억시켜둔 자료의 집합체**

### 데이터베이스로 얻는 장점

: 데이터 중복 최소화, 데이터 무결성, 데이터 일관성, 데이터 독립성, 데이터 표준화, 데이터 보안 유지

## RDB

###  관계형 데이터베이스(RDB)

: Relational Database

- 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스

- 관계형 모델에 기반

  - 스키마 : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

  - 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

    ![스크린샷 2022-04-17 오후 7.18.26](DB.assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-04-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.18.26.png)

  - 열 : 고유한 데이터 형식 지정 (컬럼, 필드라고도 불림)
  - 행 : 실제 데이터가 저장되는 형태(로우, 레코드라고도 불림)

## RDBMS

### 관계형 데이터베이스 관리 시스템(RDBMS)

: Relational Database Management System

- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
- 예) MySQL, SQLite, PostgreSQL, ORACLE, MS SQL

### Sqlite Data type

1. NULL
2. INTEGER : 부호 있는 정수
3. REAL : 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB : 입력된 그대로 정확히 저장된 데이터(타입 없이 그대로 저장)

## SQL

### SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
- 데이터 베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

### SQL 분류

![스크린샷 2022-04-17 오후 7.26.17](DB.assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-04-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.26.17.png)

### SQL 키워드 - DML

- INSERT : 새로운 데이터 삽입(추가)

- SELECT : 저장되어있는 데이터 조회

- UPDATE : 저장되어있는 데이터 갱신
- DELETE : 저장되어있는 데이터 삭제

#### SELECT

`SELECT * FROM table;` : SELECT문은 특정 테이블의 레코드(행) 정보를 반환

### CREATE

`CREATE TABLE classmates (id INTEGER PRIMARY KEY, name TEXT);`

```sqlite
.tables # 테이블 조회
.schema classmates # 해당 테이블의 스키마 조회
```

### DROP

`DROP TABLE classmates` :  테이블을 삭제

## CRUD

### CREATE

- INSERT : 테이블에 단일 행 삽입

`INSERT INTO 테이블 이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...)` : INSERT는 특정 테이블에 레코드를 삽입(생성)

- 모든 열에 데이터가 있는 경우, column을 명시하지 않아도 됨

- 주의) 꼭 필요한 정보라면 공백으로 비워두면 안됨 => NOT NULL 설정 필요

### READ

- SELECT
  - query data from a table
  - 테이블에서 데이터를 조회
  - 다양한 절과 함께 사용 : ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...

- 절(Clause)

  - LIMIT : 쿼리에서 **반환되는 행 수를 제한** -  특정 행부터 시작해 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함

  - WHERE : 쿼리에서 반환된 행에 대한 **특정 검색 조건을 지정**

  - SELECT DISTINCT : 조회 결과에서 **중복 행을 제거** - DISTINC 절은 SELECT 키워드 바로 뒤에 작성해야 함
  - 참고) OFFSET :  동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지의 위치변화량(변위차)을 나타내는 정수형

```sql
-- SELECT
SELECT 컬럼1, 컬럼2, ... FROM 테이블 이름;
-- 모든 컬럼 값이 아닌 특정 컬럼만 조회하기
SELECT rowid, name FROM classmates;
-- classmates 테이블에서 id, name 컬럼 값만 조회

-- LIMIT
SELECT rowid, name FROM classmates LIMIT 1;
-- classmates 테이블에서 id, name 컬럼 값을 하나만 조회

-- OFFSET
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- 3번째 행부터 1개 행을 조회, 0부터 시작함

-- WHERE
SELECT rowid, name FROM classmates WHERE address='서울';
-- classmates 테이블에서 id, name 컬럼 값 중 주소가 서울인 경우의 데이터 조회

-- DISTINCT
SELECT DISTINCT age FROM classmates;
-- classmates 테이블에서 age값 전체를 중복 없이 조회
```

### DELETE

: 테이블에서 행을 제거

```sql
DELETE FROM classmates WHERE rowid=5;
-- classmates 테이블에서 id가 5인 레코드 삭제
```

- AUTOINCREMENT

  : column attribute

  - SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

  - 테이블을 생성하는 단계에서 AUTOINCREMENT를 통해 설정 가능

    ```sql
    CREATE TABLE 테이블이름 (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      ...
    );
    ```

### UPDATE

: 기존 행의 데이터를 수정

- SET clause에서 테이블의 각 열에 대해 새로운 값 설정

```sql
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
-- classmates 테이블에 id가 5인 레코드를 이름은 홍길동으로, 주소를 제주도로 수정
```

## WHERE

```sql
-- 특정 조건으로 데이터 조회하기
SELECT * FROM 테이블이름 WHERE 조건;

-- users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보를 조회
SELECT * FROM users WHERE age >= 30;

-- users 테이블에서 age가 30 이상인 유저의 이름만 조회
SELECT first_name FROM users WHERE age >= 30;

-- users 테이블에서 age가 30 이상이고 성이 김인 사람의 나이와 성 조회
SELECT age, last_name FROM users WHERE age >=30 AND last_name='김';
```

## SQLite Aggregate Functions

### Aggregate Function

- 집계함수 : 각 집합에 대한 계산을 수행하고 단일 값을 반환, 여러 행으로부터 하나의 결과값을 반환하는 함수
- SELECT 구문에서만 사용
- 예) COUNT(테이블 전체 행 수), AVG(age) : age컬럼 전체 평균 값, MAX : 그룹에 있는 모든 값의 최대값을 가져옴, MIN : 그룹에 있는 모든 값의 최소값을 가져옴, SUM : 모든 값의 합을 계산

```sql
-- COUNT
SELECT COUNT(컬럼) FROM 테이블 이름;
-- 레코드의 개수 조회하기

-- users 테이블 레코드 총 개수 조회
SELECT COUNT(*) FROM users;

-- AVG, SUM, MIN, MAX
SELECT AVG(컬럼) FROM 테이블 이름;
SELECT SUM(컬럼) FROM 테이블 이름;
SELECT MIN(컬럼) FROM 테이블 이름;
SELECT MAX(컬럼) FROM 테이블 이름;
```

## LIKE

### LIKE operator

: 패턴 일치를 기반으로 데이터를 조회하는 방법

- % : 0개 이상의 문자 -  문자열이 있을 수도, 없을 수도 있음
- _ : 임의의 단일 문자 - 반드시 이 자리에 한 개의 문자가 존재해야 함

### wildcard character

: 파일을 지정할 때, 구체적인 이름 대신 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호

- 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나 긴 이름을 생략할 때 쓰임
- 텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자
- 지정된 패턴 일치를 기반으로 데이터 수집에도 도움이 됨

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
-- 패턴을 확인해 해당하는 값을 조회
```

## ORDER BY

### ORDER BY clause

: 조회 결과 집합을 정렬

- SELECT 문에 추가해 사용
- 정렬 순서를 위한 2개의 키워드 제공
  - ASC - 오름차순(기본)
  - DESC - 내림차순

## GROUP BY

### GROUP BY

- 행 집합에서 요양 행 집합을 만듦
- SELECT 문의 옵션 절
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 문장에 WHERE 절이 포함된 경우, 반드시 WHERE 절 뒤에 작성해야 함

```sql
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- users에서 각 성씨가 몇 명씩 있는지 조회

SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
-- AS를 활용해 COUNT에 해당하는 컬럼 명을 바꿔서 조회 가능
```

## ALTER TABLE

- 기능
  1. table 이름 변경
  2. 테이블에 새로운 컬럼 추가
  3. 컬럼 이름 수정

```sql
ALTER TABLE 기존테이블이름 RENAME TO 새로운 테이블 이름;
ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입설정;
```

- 테이블에 있는 기존 레코드들에 새로 추가할 필드에 대한 정보가 없음, 그렇기 때문에 NOT NULL 형태의 컬럼 추가 불가능
  - 해결방법
    1. NOT NULL 설정 없이 추가
    2. 기본 값 설정

# ORM

### ORM

- Object-Relation-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용함

![IMG_3EB441E896C9-1](../../../../Downloads/IMG_3EB441E896C9-1.jpeg)

### ORM의 장점과 단점(서술형 각)

- 장점
  - SQL 잘 몰라도 DB조작 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(**생산성**)

-> 왜 ORM을 사용할까? **"우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용한다"**

### models.py 작성

```python
# appname/models.py

class Appname(models.Model):
  title = models.CharField(max_length=10)
  content= models.TextField()
```

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  - Django.db.models 모듈의 Model 클래스를 상속받음
- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의
  - title, content는 모델의 필드를 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

### 사용 모델 필드

- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - CharField의 max_length는 필수 인자
  - 필드의 최대 길이(문자), 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용
- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성 시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음
    - Max_length 사용은 CharField에서 사용해야 함



## Migrations

### Migrations

- "Django가 model에 생긴 변화를 반영하는 방법"
- 마이그레이션 실행 및 DB 스키마를 다루기 위한 몇 가지 명령어
  - makemigration
  - migrate
  - sqlmigrate
  - showmigrations

### Migrations commands

1. makemigrations
   - 모델을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
   - `python manage.py makemigrations`
   - 'migrations/0001_initial.py' 생성 확인
2. migrate
   - 마이그레이션을 DB에 반영하기 위해 사용
   - 설계도를 실제 DB에 반영하는 과정
   - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
   - `python manage.py migrate`
3. sqlmigrate
   - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
   - 마이그레이션이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음
   - `python manage.py sqlmigrate app_name 0001`
4. showmigrations
   - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
   - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음
   - `python manage.py showmogrations`

### model 수정

1. 추가 모델 필드 작성 후 makemigrations 진행
2. 디폴트값 설정, 함수 값 자동 설정 등등
3. migrate를 통해 models.py 수정사항 반영

### DateField의 옵션

- auto_now_add
  - 최초 생성 일자
  - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)
- auto_now
  - 최종 수정 일자
  - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

### DateTimeField가 아닌 DateField의 options를 확인한 이유

- DateTimeField는 Datefield와 동일한 추가 인자를 사용함
- DateTimeField는 Datefield의 서브 클래스

### migration 3단계(서술형 각)

1. models.py :  model 변경사항 발생 시
2. `python manage.py makemigrations` : migrations 파일 생성
3. `python manage.py migrate` : DB 반영(모델과 DB의 동기화)



## Database API

### DB API

- "DB를 조작하기 위한 도구"
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- Database-abstract API 혹은 database-access API 라고도 함

### DB API의 구문 - Making queries

**Article.objects.all()** [classname.manager.queryset API]

- Manager
  - Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects 라는 Manager를 추가
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음

### Django Shell

- 일반 Python Shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
- 그래서 장고 프로젝트 설정이 로드 된 Python shell을 활용해 DB API 구문 테스트 진행
- 기본 Django shell 보다 더 많은 기능을 제공하는 shell_plus를 사용해 진행
  - Shell_plus를 원활히 사용하기 위한 2가지 라이브러리 설치(ipython, django-extensions)
  - 앱 등록 후 Shell_plus 실행 `python manage.py shell_plus`



## CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create, Read, Update, Delete를 묶어서 일컫는 말

### Read

`Article.objects.all()` : 전체  article 객체 조회

### Create

1. 인스턴스 생성 후 인스턴스 변수 설정

   ```python
   article = Article()
   article.title = 'first'
   article.content = 'first content'
   article.save()
   ```

2. 초기값과 함께 인스턴스 생성

   ```python
   article = Article(title='second', content='second content')
   article.save()
   ```

3. QuerySet API - create() 사용

   ```python
   Article.objects.create(title='third', content='third content')
   ```

   -> save()가 이미 포함되어 있어서 바로 생성됨

### create 관련 메서드

- save() method
  - saving objects
  - 객체를 데이터베이스에 저장
  - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
    - ID 값은 Django가 아니라 DB에서 계산되기 때문
  - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요

### str method

표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음 -> 작성 후 반드시 shell_plus를 재시작해야 반영됨

### READ

- QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
- 두가지로 분류
  1. Methods that return new querysets
  2. Methods that do not return querysets

- all()
  - 현재 QuerySet의 복사본을 반환
- get()
  - 주어진 lookup 매개변수와 일치하는 객체를 반환
  - 객체를 찾을 수 없으면 DoesNotExist 예외 발생 / 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
  - 위와 같은 특징때문에 primary key와 같이 고유성을 보장하는 조회에서 사용해야 함
- filter()
  - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

### UPDATE

```python
article = Article.objects.get(pk=1)
article.title
#'first'
article.title = 'byebye'
article.save()

article.title
# 'byebye'
```

### DELETE

delete()

- QuerySet 의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환

  ```python
  article = Article.objects.get(pk=1)
  
  article.delete()
  (1, {'articles.Article':1})
  
  Article.objects.get(pk=1)
  DoesNotExist: Article matching query does not exist.
  ```

### Field lookups

- 조회 시 특정 검색 조건을 지정

- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨

  ```python
  Article.objects.filter(pk__gt=2)
  Article.objects.filter(content__contains='ja')
  ```



# DB 02

## Foreign Key

: 외래 키

- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 속성(필드)에 해당하고, 이는 참조되는 테이블의 기본키를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응됨
  - 이 떄문에 참조하는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조할 수 없음
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음

### 특징

- 키를 사용해 부모 테이블의 유일한 값을 참조(참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없음, 다만 유일한 값이어야 함

- 참조 무결성 : 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성 / 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

### ForeignKey field

- A many-to-one relationship
- 2개의 위치 인자가 반드시 필요
  1. 참조하는 model class
  2. On_delete 옵션
- migrate 작업 시 필드 이름에 _id를 추가해 데이터베이스 열 이름을 만듦

- 참고) 재귀 관계(자신과 1:N)

### on_delete

- 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 지를 정의
- 데이터 무결성을 위해 매우 중요한 설정
- 옵션 : CASCADE :  부모 객체가 삭제됐을 때 이를 참조하는 객체도 삭제

### 1:N 관계 related manager

- 역참조(comment set)
  - Article - Comment : 1:N
  - article.comment 형태로는 사용 X, article.comment_set manager 생성됨
  - 게시글에 몇 개의 댓글이 작성되었는지 보장할 수 없기 때문
    - 댓글이 있을 수도, 없을 수도 있음
    - 실제로 Article 클래스에는 comment와의 어떠한 관계도 작성되어 있지 않음
- 참조('article')
  - Comment - Article : N:1
  - 댓글은 어떠한 댓글이든 참조하고 있는 게시글 있으므로 comment.article로 접근 가능
  - ForeignKeyField 또한 Comment클래스에서 작성됨

### related_name

- 역참조 시 사용할 이름을 변경할 수 있는 옵션
- 대체 시, 기존의 `_set` 사용 불가, 설정한 이름으로 대체됨