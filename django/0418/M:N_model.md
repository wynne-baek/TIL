# M:N model

## 01 1: N의 한계

- 새로운 예약 생성이 불가능
  - 새로운 객체를 생성해야 함
- 하나의 외래 키에 2개의 데이터 삽입 불가능
  - 외래 키에 '1, 2'형식의 데이터 사용 불가능

- 해결 방법
  1. 중개 모델 : 중개 테이블, Associative Table
  2. ManyToManyField

## 02 ManyToManyField

- 다대다(M:N) 관계 설정 시 사용하는 모델 필드

- 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요

- 모델 필드의 RelatedManager를 사용해 관련 개체를 추가, 제거, 생성 가능

  - 1:N, M:N 관련 컨텍스트에서 사용되는 매니저
  - 같은 이름이라도 각 관계에 따라 다르게 사용 및 동작
    - 1:N - target 모델 인스턴스만 사용 가능
    - M:N - 관련된 두 객체에서 모두 사용 가능
  - Add()
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    - 모델 인스턴스, 필드값(PK)를 인자로 허용
  - remove()
    - 관련 객체 집합에서 지정된 모델 객체를 제거
    - 내부적으로 `QuerySet.delete()`를 사용해 관계가 삭제됨
    - 모델 인스턴스, 필드 값(PK)를 인자로 허용

  ```python
  # add()
  
  doctor1 = Doctor.objects.create(name='Justin')
  patient1 = Patient.objects.create(name='Tony')
  
  doctor1.patient_set.add(patient1)
  # or
  patient1.doctor.add(doctor1)
  
  # remove()
  doctor1 = Doctor.objects.get(pk=1)
  patient1 = Patient.objects.get(pk=1)
  
  doctor1.patient_set.remove(patient1)
  # or
  patient1.doctor.remove(doctor1)
  ```

  

- 연결하려는 두 모델 중 하나를 선택해 작성 가능

```python
# hospitals/models.py

class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor)
  # ^ 요런 식으로!
  name = models.TextField()
  
 # or

class Doctor(models.Model):
  patients = models.ManyToManyField(Patient)
  # ^ 요런 식으로!

```

- 참조 / 역참조를 활용해 행을 생성 및 삭제할 수 있음

- Related_name

  : target model(관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 사용할 manager의 이름을 설정

  => 역참조 시 사용하는 manager의 이름을 설정

  => ForeignKey의 related_name과 같은 역할

  ```python
  class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    # ^ 요런 식으로!
    name = models.TextField()
  ```

- 중개모델 in Django

  - django는 ManyToManyField를 통해 중개 테이블 자동 생성

  - 직접 작성하는 경우는?

    : 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용해 중개 테이블을 나타내는 Django 모델을 지정할 수 있음

    => 가장 일반적인 용도 : 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려는 경우에 사용

=> 실제 Doctor와 Patient 테이블이 변화하지는 않음, but, 완전 종속이었던 1:N 관계와 달리 M -> N / N -> M 두 가지 형태로 모두 표현이 가능해짐!

- symmetrical

  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

  - symmetrical=True(기본값)일 경우, Django는 person_set 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함
    - 너는 내 친구 = 나는 네 친구
    - 대칭을 원하지 않을 경우 False로 설정
    - Follow 기능 구현에서 다시 보기!

  ```python
  class Person(models.Model):
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetricla=False)
    
  ```

- 데이터베이스에서의 표현
  - 다대다 관계를 나타내는 중개테이블을 만듦
  - 테이블 이름은 다대다 필드의 이름과 이를 포함하는 모델의 테이블 이름을 조합해 생성됨
- 중개 테이블 필드 생성 규칙
  1. Source model 및 target model 이 다른 경우
     - `id`
     - `<containing_model>_id`
     - `<other_model>_id`
  2. ManyToManyField가 동일한 모델을 가리키는 경우
     - `id`
     - `from_<model>_id`
     - `to_<model>_id`

## 03 Like 구현

- QuerySet API - `exist()`
  - QuerySet에 결과가 포함되어 있으면 True, 그렇지 않으면 False 반환
  - 특히 규모가 큰 QuerySet의 컨텍스트에서 특정 개체 존재 여부와 관련된 검색에 유용
  - 고유한 필드가 있는 모델이 QuerySet의 구성원인지 여부를 찾는 가장 효율적인 방법