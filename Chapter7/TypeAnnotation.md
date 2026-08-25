# 파이썬 타입 어노테이션(type annotation)

> 예제 코드: [Source/type_annotation.py](Source/type_annotation.py)

- [동적 언어와 정적 언어](#동적-언어와-정적-언어)
- [타입 어노테이션](#타입-어노테이션)
- [변수와 함수에 타입 지정하기](#변수와-함수에-타입-지정하기)
- [컨테이너 요소 타입 지정하기](#컨테이너-요소-타입-지정하기)
- [typing 모듈과 내장 타입](#typing-모듈과-내장-타입)
- [Optional, Union, Callable, Any](#optional-union-callable-any)
- [mypy로 타입 검사하기](#mypy로-타입-검사하기)

## 동적 언어와 정적 언어

파이썬은 실행 중 변수에 다른 타입의 값을 다시 대입할 수 있는 동적 타입 언어이다. 반면 자바 같은 정적 타입 언어는 선언한 타입과 다른 값을 대입하면 컴파일 오류가 발생한다.

```python
a = 1
print(type(a))   # <class 'int'>

a = "1"
print(type(a))   # <class 'str'>
```

동적 언어는 빠르고 유연하게 코드를 작성할 수 있지만, 프로젝트가 커질수록 타입을 잘못 사용한 버그가 생길 가능성도 커진다.

## 타입 어노테이션

타입 어노테이션(type annotation)은 변수, 매개변수, 반환값에 기대하는 타입을 적는 문법이다. 파이썬 3.5부터 지원하며, 파이썬이 타입을 강제하는 것이 아니라 코드를 읽는 사람과 도구에 힌트를 제공한다.

```python
변수_이름: 타입 = 값

def 함수_이름(매개변수: 타입) -> 반환_타입:
    return 값
```

> 어노테이션과 다른 타입의 값을 넘겨도 파이썬 프로그램은 실행된다. 실제 타입 검사는 IDE나 `mypy` 같은 별도 도구가 수행한다.

## 변수와 함수에 타입 지정하기

변수 이름 뒤에 `: 타입`을 적고, 함수에서는 매개변수 뒤와 `->` 뒤에 각각 타입을 적는다. 이를 통해 함수가 받을 인수와 반환할 값을 쉽게 파악할 수 있다.

```python
num: int = 1
name: str = "홍길동"
numbers: list = [1, 2, 3]

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"안녕하세요 {name}님!"

def get_user_info(user_id: int) -> dict:
    return {"id": user_id, "name": "홍길동"}
```

기본 어노테이션에는 `int`, `str`, `list`, `tuple`, `dict`, `set`, `bool` 등을 사용한다.

## 컨테이너 요소 타입 지정하기

리스트, 딕셔너리, 튜플에는 대괄호 안에 요소 타입까지 지정할 수 있다. `list[int]` 문법은 파이썬 3.9 이상에서 사용할 수 있다.

```python
numbers: list[int] = [1, 2, 3]
user_info: dict[str, int] = {"age": 30}
coordinates: tuple[float, float] = (3.5, 7.2)
```

`dict[str, int]`는 키가 문자열이고 값이 정수인 딕셔너리이며, `tuple[float, float]`는 실수 두 개를 순서대로 담는 튜플이다.

## typing 모듈과 내장 타입

파이썬 3.5~3.8에서는 컨테이너의 요소 타입을 표시하려면 `typing` 모듈의 `List`, `Dict`, `Tuple`을 사용한다. 파이썬 3.9 이상에서는 소문자 내장 타입을 쓰는 방식을 권장한다.

- **파이썬 3.5~3.8** — `typing` 모듈의 대문자 타입을 사용한다.

  ```python
  from typing import List, Dict, Tuple

  numbers: List[int] = [1, 2, 3]
  user_info: Dict[str, int] = {"age": 30}
  ```

- **파이썬 3.9 이상** — 내장 타입에 대괄호를 붙여 사용한다.

  ```python
  numbers: list[int] = [1, 2, 3]
  user_info: dict[str, int] = {"age": 30}
  ```

> 구버전 파이썬도 지원해야 한다면 해당 버전에서 동작하는 `typing` 문법을 선택해야 한다.

## Optional, Union, Callable, Any

`typing` 모듈은 기본 타입만으로 표현하기 어려운 경우에 사용한다. 파이썬 3.9 이상에서도 `Optional`, `Union`, `Callable`, `Any` 같은 타입은 가져와 사용한다.

```python
from typing import Optional, Union, Callable, Any

# str 또는 None
user_name: Optional[str] = None

# int 또는 str
user_id: Union[int, str] = "jenny"

# int를 받아 str을 반환하는 함수
def process_data(callback: Callable[[int], str]) -> str:
    return callback(42)

# 어떤 타입이든 허용
unknown_data: Any = {"key": "value"}
```

실무에서는 기본 타입에 내장 타입을 쓰고, `None` 가능 여부나 여러 타입 허용처럼 특별한 경우에만 필요한 항목을 `typing`에서 가져온다.

```python
from typing import Optional, Union

sources: list[int] = [95, 87, 92]
user_data: dict[str, str] = {"name": "홍길동"}

def find_user(user_id: int) -> Optional[dict[str, str]]:
    if user_id > 0:
        return {"name": "홍길동", "email": "hong@example.com"}
    else:
        return None
```

## mypy로 타입 검사하기

`mypy`는 타입 어노테이션을 바탕으로 코드를 실행하기 전에 타입 문제를 찾아주는 정적 타입 검사기이다. 어노테이션과 맞지 않는 인수를 넘겨도 파이썬은 실행하지만, `mypy`와 IDE는 경고를 표시할 수 있다.

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 3.4)
print(result)   # 6.4
```

```bash
pip install mypy
mypy Chapter7/Source/type_annotation.py
```

```text
Chapter7/Source/type_annotation.py:78: error: Argument 2 to "add" has incompatible type "float"; expected "int"  [arg-type]
Found 8 errors in 1 file (checked 1 source file)
```

위 예제 파일에는 학습 과정에서 같은 이름을 다시 정의한 부분도 있으므로 `mypy`는 그 부분까지 함께 알려 준다. 타입 오류를 고치면 `mypy`를 다시 실행해 문제가 없는지 확인할 수 있다.
