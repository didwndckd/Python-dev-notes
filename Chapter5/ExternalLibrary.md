# 외부 라이브러리(external library)

> 예제 코드: [Source/advanced/external_library.py](Source/advanced/external_library.py)

- [외부 라이브러리란](#외부-라이브러리란)
- [pip](#pip)
- [Faker](#faker)
- [fractions.Fraction](#fractionsfraction)
- [sympy](#sympy)

## 외부 라이브러리란

파이썬을 설치할 때 함께 설치되는 [표준 라이브러리](StandardLibrary.md)와 달리, 외부 라이브러리는 별도로 설치해야 사용할 수 있다. 파이썬 패키지는 **PyPI**(Python Package Index)라는 저장소에 모여 있고, 이를 내려받아 설치해 주는 도구가 **pip**(핍)이다.

> 외부 라이브러리는 프로젝트마다 필요한 버전이 다르므로 [가상 환경(venv)](../Appendix/VirtualEnvironment.md)을 활성화한 상태에서 설치하는 것이 좋다. 아래 예제도 가상 환경이 활성화되어 있다고 가정한다.

## pip

pip의 가장 큰 장점은 **의존성 있는 패키지를 자동으로 함께 설치**해 준다는 것이다. B 패키지가 A 패키지를 필요로 한다면, B를 설치할 때 A도 함께 설치된다.

```bash
# 맥: python3 ~
# 윈도우: python ~

# 파이썬 패키지 설치(버전을 생략하면 최신 버전)
python3 -m pip install SomePackage

# 특정 버전으로 설치
python3 -m pip install SomePackage==1.0.4

# 최신 버전으로 업그레이드
python3 -m pip install --upgrade SomePackage

# 설치된 패키지 확인
python3 -m pip list

# 파이썬 패키지 삭제
python3 -m pip uninstall SomePackage
```

`pip list`를 실행하면 설치된 패키지와 버전이 함께 출력된다.

```
Package                  Version
------------------------ --------
amqp                     2.1.4
anyjson                  0.3.3
billiard                 3.3.0.23
celery                   3.1.0
(... 생략 ...)
```

> `pip`을 그냥 실행하지 않고 `python3 -m pip`으로 실행하면, 지금 사용 중인 파이썬 인터프리터에 확실하게 설치된다.

## Faker

`Faker`는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리다. 이름, 주소 같은 데이터를 직접 만들지 않아도 되므로 테스트 데이터가 많이 필요할 때 편리하다.

```bash
python3 -m pip install Faker
```

```python
from faker import Faker

fake = Faker()
print(fake.name())      # Rebecca Powell: 매번 바뀜

fake = Faker('ko-KR')   # 한글로
print(fake.name())      # 강정남: 매번 바뀜

print(fake.address())   # 부산광역시 종로구 역삼04길 375
```

`Faker()`에 `ko-KR`처럼 지역 코드를 전달하면 그 지역에 맞는 데이터를 만들어 준다.

- **테스트 데이터 만들기** — [리스트 컴프리헨션](../Chapter3/For.md)과 함께 쓰면 원하는 건수만큼 한 번에 만들 수 있다.

  ```python
  # 이름과 주소를 쌍으로 하는 30건의 데이터
  test_data = [(fake.name(), fake.address()) for i in range(30)]
  print(test_data)
  # [('장혜진', '울산광역시 서구 백제고분가 지하138 (미숙김황읍)'), ('송상훈', '경기도 춘천시 역삼61가 855-50'), ...]
  ```

- **자주 쓰는 항목** — `name`, `address` 외에도 다양한 항목을 제공한다.

  | 항목 | 설명 |
  | --- | --- |
  | `fake.name()` | 이름 |
  | `fake.address()` | 주소 |
  | `fake.postcode()` | 우편 번호 |
  | `fake.country()` | 국가명 |
  | `fake.company()` | 회사명 |
  | `fake.job()` | 직업명 |
  | `fake.phone_number()` | 전화 번호 |
  | `fake.email()` | 이메일 주소 |
  | `fake.user_name()` | 사용자명 |
  | `fake.pyint(min_value=0, max_value=100)` | 0부터 100 사이의 임의의 숫자 |
  | `fake.ipv4_private()` | IP 주소 |
  | `fake.text()` | 임의의 문장(한글 문장은 `fake.catch_phrase()`) |
  | `fake.color_name()` | 색상명 |

## fractions.Fraction

`fractions.Fraction`은 유리수를 정확하게 연산하기 위한 표준 라이브러리다. `0.1 + 0.2`처럼 실수 연산에서 생기는 오차 없이 분수를 그대로 다룰 수 있다.

```python
from fractions import Fraction

# Fraction(분자, 분모)
print(Fraction(1, 5))     # 1/5
print(Fraction('1/5'))    # 1/5
```

`Fraction(분자, 분모)` 형태로도, `Fraction('분자/분모')`처럼 문자열로도 만들 수 있다.

## sympy

`sympy`는 방정식 기호(symbol)를 사용하게 해 주는 라이브러리다. 미지수를 기호로 선언하고 방정식을 세우면 해를 구해 준다.

```bash
python3 -m pip install sympy
```

- **미지수 만들기** — `sympy.symbols()`로 방정식에 사용할 기호를 생성한다.

  ```python
  import sympy

  # x를 미지수로 생성
  x = sympy.symbols("x")

  # x, y를 미지수로 생성
  x, y = sympy.symbols('x y')
  ```

  > **왜 미지수를 따로 만들어야 할까?** 파이썬은 정의되지 않은 이름을 쓰면 `NameError`가 나고, 그렇다고 `x = 100`처럼 값을 넣으면 `x * Fraction('2/5')`가 곧바로 `40`으로 계산돼 풀어야 할 식이 남지 않는다. `symbols()`가 반환하는 `Symbol` 객체는 값이 없으므로 연산이 계산되지 않고 식 그대로 보존되고, `solve()`는 그 식을 보고 해를 구한다.
  >
  > ```python
  > print(type(x))               # <class 'sympy.core.symbol.Symbol'>
  > print(x * Fraction('2/5'))   # 2*x/5: 계산되지 않고 식으로 남는다
  > ```
  >
  > 왼쪽의 `x`(파이썬 변수명)와 `symbols("x")`에 넘긴 `"x"`(기호 이름)는 별개다. `a = sympy.symbols("x")`로 써도 동작하지만 헷갈리므로 보통 같게 맞춘다.

- **일차방정식 풀기** — `sympy.Eq(a, b)`는 `a`와 `b`가 같다는 방정식이고, `sympy.solve()`가 해를 구한다.

  ```python
  # 예제: 가진 돈의 2/5로 학용품을 샀다. 학용품을 사는 데 쓴 돈이 1,760원이라면 남은 돈은?
  # 위 예제의 일차방정식 x * (2/5) = 1760을 코드로 표현
  f = sympy.Eq(x*Fraction('2/5'), 1760)

  result = sympy.solve(f)   # 원래 가진 돈 x를 구함
  print(result)             # [4400]

  remains = result[0] - 1760
  print(remains)            # 2640
  ```

  > `2/5`를 그대로 쓰면 부동소수점 실수가 되므로, 정확한 계산을 위해 `Fraction('2/5')`을 사용했다.

- **이차방정식 풀기** — 해가 여러 개이면 리스트에 모두 담겨 반환된다.

  ```python
  # x^2 = 1과 같은 2차 방정식의 해 구하기
  x = sympy.symbols('x')
  f = sympy.Eq(x**2, 1)
  result = sympy.solve(f)
  print(result)   # [-1, 1]
  ```

- **연립방정식 풀기** — 방정식을 리스트로 묶어 `solve()`에 전달한다.

  ```python
  # x + y = 10
  # x - y = 4
  x, y = sympy.symbols('x y')
  f1 = sympy.Eq(x+y, 10)
  f2 = sympy.Eq(x-y, 4)
  result = sympy.solve([f1, f2])
  print(result)   # {x: 7, y: 3}
  ```

> 미지수가 1개면 결괏값이 **리스트**, 2개 이상이면 **딕셔너리**라는 점에 주의하자.
