# 모듈(module)

> 예제 코드: [Source/modules/](Source/modules) — [mod1.py](Source/modules/mod1.py), [mod2.py](Source/modules/mod2.py), [sub_modules/mod3.py](Source/modules/sub_modules/mod3.py), [use_mod.py](Source/modules/use_mod.py)

- [모듈 만들기](#모듈-만들기)
- [모듈 불러오기](#모듈-불러오기)
- [직접 실행과 import 구분(\_\_name\_\_)](#직접-실행과-import-구분__name__)
- [클래스나 변수를 포함한 모듈](#클래스나-변수를-포함한-모듈)
- [다른 디렉터리에 있는 모듈 불러오기](#다른-디렉터리에-있는-모듈-불러오기)

## 모듈 만들기

모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다. 다른 파이썬 프로그램에서 불러와 쓸 수 있게 만든 파일이라고도 할 수 있다. 확장자 `.py`로 만든 파이썬 파일은 **모두 모듈**이므로, 따로 특별한 문법이 필요하지는 않다.

```python
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

## 모듈 불러오기

`import`로 모듈을 통째로 불러온다. 이때 모듈 이름은 파일명에서 확장자 `.py`를 뗀 부분이다.

```python
import 모듈_이름
```

```python
import mod1
# print(add(1, 2))    # 에러 발생: 모듈 이름 없이는 못 쓴다
print(mod1.add(1, 2))   # 3
print(mod1.sub(2, 1))   # 1
```

> `import mod1.py`처럼 확장자를 붙이지 않도록 주의한다. `mod1`만 쓴다.

- **함수만 골라 불러오기** — `from ... import ...`를 쓰면 모듈 이름을 붙이지 않고 내부 함수처럼 쓸 수 있다. 대신 `import`로 선언한 함수만 사용 가능하다.

  ```python
  from 모듈_이름 import 모듈_함수1, 모듈_함수2, ...
  ```

  ```python
  from mod1 import add
  print(add(1, 2))     # 3
  # print(sub(2, 1))   # 에러 발생: add만 import 했다
  ```

- **여러 개를 한 번에** — 쉼표로 구분해 필요한 함수를 나열한다.

  ```python
  from mod1 import add, sub
  print(add(1, 2))   # 3
  print(sub(2, 1))   # 1
  ```

- **전부 불러오기** — `*`는 '모든 것'이라는 뜻으로, 모듈의 모든 함수를 내부 함수처럼 쓰겠다는 의미다.

  ```python
  from mod1 import *
  print(add(1, 2))   # 3
  print(sub(2, 1))   # 1
  ```

> `import`는 **현재 디렉터리에 있는 파일**이나 **파이썬 라이브러리가 저장된 디렉터리에 있는 모듈**만 불러올 수 있다. 파이썬 라이브러리란 파이썬을 설치할 때 자동으로 함께 설치되는 모듈을 말한다. 다른 위치에 있는 모듈을 쓰는 방법은 [아래](#다른-디렉터리에-있는-모듈-불러오기)에서 다룬다.

## 직접 실행과 import 구분(\_\_name\_\_)

모듈 파일 마지막에 출력문을 넣어 보자.

```python
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("import mod1")
```

이 상태에서는 함수만 쓰려고 `import`해도 출력문이 실행된다. **`import`는 모듈 파일을 위에서부터 한 번 쭉 실행하는 동작**이기 때문이다.

```python
import mod1                # import mod1 이 출력된다
from mod1 import add       # 일부만 import 해도 마찬가지로 출력된다
```

`if __name__ == "__main__":` 블록으로 감싸면 이 문제를 막을 수 있다.

```python
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 이 파일을 직접 돌렸을 때만 출력된다.
if __name__ == "__main__":
    print("import mod1")
```

```python
import mod1   # 아무 출력도 나오지 않는다
```

`__name__`은 파이썬이 내부적으로 사용하는 특수 변수다. 그 파일을 **직접 실행하면**(`python3 mod1.py`) `"__main__"`이 들어가고, **다른 파일에서 import하면** 모듈 이름이 들어간다.

```python
print(mod1.__name__)   # mod1: 외부에서 사용할 때는 모듈 이름이 된다
```

즉 `if __name__ == "__main__":` 아래 코드는 직접 실행할 때만 참이 되어 수행되고, import될 때는 거짓이 되어 건너뛴다. 모듈의 테스트 코드나 실행 예제를 여기에 넣는다.

## 클래스나 변수를 포함한 모듈

모듈에는 함수뿐 아니라 변수와 클래스도 담을 수 있다. 사용법은 함수와 똑같이 `모듈_이름.이름` 형태다.

```python
# mod2.py
PI = 3.141592          # 모듈 전역 변수

class Math:            # 모듈 클래스
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):         # 모듈 전역 함수
    return a + b
```

```python
import mod2
print(mod2.PI)   # 3.141592

math = mod2.Math()
solv = math.solv(2)
print(solv)      # 12.566368

result = mod2.add(solv, 4.4)
print(result)    # 16.966368000000003
```

## 다른 디렉터리에 있는 모듈 불러오기

`sub_modules/mod3.py`처럼 다른 디렉터리에 있는 모듈은 그냥 `import`하면 찾지 못한다.

```python
# sub_modules/mod3.py
def call_module_name():
    print(__name__)
```

```python
# import mod3   # ModuleNotFoundError: 그냥 추가하면 에러
```

파이썬은 모듈을 찾을 때 `sys.path`에 담긴 디렉터리 목록을 뒤진다. `sys` 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다.

```python
import sys
print(sys.path)
# ['/Users/yjc/Workspace/Python-dev-notes/Source/modules',
#  '.../python314.zip',
#  '.../python3.14',
#  '.../python3.14/lib-dynload',
#  '/opt/homebrew/lib/python3.14/site-packages']
```

> 목록의 **각 경로 바로 아래**만 찾는다. 하위 디렉터리까지 파고들지 않기 때문에 `sub_modules/mod3.py`가 걸리지 않는 것이다. 결국 해결책은 `mod3.py`가 있는 디렉터리를 이 목록에 넣어 주는 것이며, 방법은 두 가지다.

- **sys.path.append 사용하기** — `sys.path`는 리스트이므로 원하는 경로를 직접 덧붙이면 된다.

  ```python
  import sys
  sys.path.append("/Users/yjc/Workspace/Python-dev-notes/Source/modules/sub_modules")

  import mod3
  mod3.call_module_name()   # mod3: 호출된다
  ```

  > 코드 안에서 처리하므로 그 스크립트에만 적용된다. 단, `import`는 실행 시점에 경로를 찾으므로 `sys.path.append`가 `import mod3`보다 **먼저** 나와야 한다.

- **PYTHONPATH 환경 변수 사용하기** — 셸에서 환경 변수로 경로를 지정하면 코드를 고치지 않아도 된다. 맥·리눅스는 `export`, 윈도우는 `set`을 쓴다.

  ```bash
  $ export PYTHONPATH=~/Workspace/Python-dev-notes/Source/modules/sub_modules
  $ python3
  >>> import mod3
  >>> mod3.call_module_name()
  mod3
  ```

  > `export`는 **그 명령을 친 터미널 세션에만** 적용된다. 새 탭을 열거나 터미널을 껐다 켜면 사라진다. 현재 설정값은 `printenv PYTHONPATH`로 확인할 수 있다.
