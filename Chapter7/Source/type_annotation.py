# 타입 어노테이션: 정적 언어처럼 강제로 타입을 체크하지는 않고 타입에 대한 힌트 정도만 제공

a = 1
print(type(a)) # <class 'int'>

a = "1"
print(type(a)) # <class 'str'>

# 변수에 타입 지정하기
num: int = 1
name: str = "홍길동"
numbers: list = [1, 2, 3]

# 함수에 타입 지정하기: 함수의 매개변수, 반환값 명시 가능
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"안녕하세요 {name}님!"

def get_user_info(user_id: int) -> dict:
    return {"id": user_id, "name": "홍길동"}

# 리스트나 딕셔너리같은 타입은 그 안에 어떤 타입의 요소가 들어가는지까지 명시 가능
numbers: list[int] = [1, 2, 3]
user_info: dict[str, int] = {"age": 30}
coordinates: tuple[float, float] = (3.5, 7.2)


# typing 모듈: 더 구체적인 타입 정보가 필요한 경우
# 파이썬 3.9이상은 typing 모듈 없이 소문자 내장타입(list, dict, tuple) 그대로 사용 가능, 구버전은 대문자 타입을 사용하는 경우가 많음(List, Dict, Tuple)

# 파이썬 3.5~3.8: typing 모듈 필수
from typing import List, Dict, Tuple
numbers: List[int] = [1, 2, 3]
user_info: Dict[str, int] = {"age": 30}

# 파이썬 3.9 이상: 내장 타입으로 사용 가능(권장)
numbers: list[int] = [1, 2, 3]
user_info: dict[str, int] = {"age": 30}

# 파이썬 3.9 이상에서도 typing 모듈이 필요한 경우
from typing import Optional, Union, Callable, Any
# 1. Optional - None이 가능한 경우
user_name: Optional[str] = None # str 또는 None

# 2. Union - 여러 타입이 가능한 경우
user_id: Union[int, str] = "jenny" # 정수 또는 문자열

# 3. Callable - 함수 타입 지정: 아래는 int를 받아서 str을 반환한다는 예시
def process_data(callback: Callable[[int], str]) -> str:
    return callback(42)

# 4. Any - 어떤 타입이든 허용한다는 의미
unknown_data: Any = {"key": "value"}

# 실무에서의 권장 예시
from typing import Optional, Union # 필요한 것만 가져오기

# 기본 타입은 내장 타입 사용
sources: list[int] = [95, 87, 92]
user_data: dict[str, str] = {"name": "홍길동"}

# 특별한 경우에만 typing 모듈 사용
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # 사용자를 찾으면 딕셔너리 반환, 없으면 None 반환
    if user_id > 0:
        return {"name": "홍길동", "email": "hong@example.com"}
    else:
        return None

# mypy
# 파이썬은 타입 어노테이션으로 매개변수의 타입을 명시 하더라도 다음과 같이 다른 타입의 인수를 입력할 수 있음
def add(a: int, b: int) -> int:
    return a + b

# 파이참과 같은 파이썬 전용 IDE를 사용하면 타입이 맞지 않는다고 경고 메시지를 표시함.
result = add(3, 3.4)
print(result) # 6.4

# mypy 설치
# pip install mypy

# 아래 명령어 실행
# mypy Chapter7/Source/type_annotation.py                                                                                                                                                                                                               ─╯

# 실행 결과
# Chapter7/Source/type_annotation.py:6: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# Chapter7/Source/type_annotation.py:25: error: Name "numbers" already defined on line 12  [no-redef]
# Chapter7/Source/type_annotation.py:35: error: Name "numbers" already defined on line 12  [no-redef]
# Chapter7/Source/type_annotation.py:36: error: Name "user_info" already defined on line 26  [no-redef]
# Chapter7/Source/type_annotation.py:39: error: Name "numbers" already defined on line 12  [no-redef]
# Chapter7/Source/type_annotation.py:40: error: Name "user_info" already defined on line 26  [no-redef]
# Chapter7/Source/type_annotation.py:74: error: Name "add" already defined on line 15  [no-redef]
# Chapter7/Source/type_annotation.py:78: error: Argument 2 to "add" has incompatible type "float"; expected "int"  [arg-type] <- 여기 add 함수에 대한 경고
# Found 8 errors in 1 file (checked 1 source file)


