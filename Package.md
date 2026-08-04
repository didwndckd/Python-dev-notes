# 패키지(package)

> 예제 코드: [Source/packages/](Source/packages) — [main/package.py](Source/packages/main/package.py), [game/\_\_init\_\_.py](Source/packages/game/__init__.py), [game/sound/\_\_init\_\_.py](Source/packages/game/sound/__init__.py), [game/sound/echo.py](Source/packages/game/sound/echo.py), [game/graphic/render.py](Source/packages/game/graphic/render.py)

- [패키지 구조](#패키지-구조)
- [패키지 만들기](#패키지-만들기)
- [패키지 안의 함수 실행하기](#패키지-안의-함수-실행하기)
- [\_\_init\_\_.py 파일의 용도](#__init__py-파일의-용도)
- [\_\_all\_\_](#__all__)
- [상대 경로로 import하기](#상대-경로로-import하기)
- [실무에서는](#실무에서는)

## 패키지 구조

패키지란 관련 있는 **모듈의 집합**이다. 패키지를 사용하면 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있다. 파일을 폴더로 묶어 정리하는 것과 같은 개념으로, 모듈이 많아져 이름이 겹치거나 관리가 어려워질 때 유용하다.

파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다. 다음은 예제로 만들 `game` 패키지의 구조다.

```
game/                    ← 루트 패키지
├── __init__.py
├── sound/               ← 서브패키지
│   ├── __init__.py
│   └── echo.py          ← 모듈
└── graphic/             ← 서브패키지
    ├── __init__.py
    └── render.py        ← 모듈
```

`game`, `sound`, `graphic`은 디렉터리이고 확장자가 `.py`인 파일은 모듈이다. 간단한 프로그램이 아니라면 패키지 구조로 만드는 편이 공동 작업이나 유지 보수에 유리하고, 다른 모듈과 이름이 겹쳐도 안전하게 사용할 수 있다.

> `sound`, `graphic`도 각각 **패키지**다. `game` 아래에 있으니 서브패키지라고 부를 뿐, `__init__.py`를 가진 디렉터리는 위치와 상관없이 모두 패키지다. 파이썬은 `__path__` 속성을 가진 모듈을 패키지로 취급한다.
>
> ```python
> import game.sound.echo
> print(hasattr(game, '__path__'))              # True: 패키지
> print(hasattr(game.sound, '__path__'))        # True: 패키지
> print(hasattr(game.sound.echo, '__path__'))   # False: 모듈
> ```

## 패키지 만들기

각 디렉터리에는 `__init__.py` 파일을 만들어 둔다. 이 파일이 있어야 파이썬이 해당 디렉터리를 패키지로 인식한다(내용은 비워 둬도 된다). 모듈 파일은 평범한 `.py` 파일이다.

```python
# game/sound/echo.py
def echo_test():
    print("echo")
```

```python
# game/graphic/render.py
def render_test():
    print("render")
```

패키지를 어디서든 import할 수 있도록 `game`의 **상위 디렉터리**를 `PYTHONPATH`에 추가하고 인터프리터를 실행한다. 여기서는 프로젝트 루트 기준으로 `Source/packages`가 그 위치다.

```bash
$ export PYTHONPATH=Source/packages   # 윈도우는 set PYTHONPATH=...
$ python3
>>>
```

> 아래 예제들은 **명령 프롬프트에서 파이썬 인터프리터를 실행해** 진행한다. 그리고 하나의 예제를 실행하고 다음 예제로 넘어갈 때는 반드시 인터프리터를 종료(`exit()`)하고 다시 실행해야 한다. 파이썬은 한번 import한 모듈을 메모리에 저장해 두기 때문에, 재시작하지 않으면 이전에 import한 것이 남아 있어 예상과 다른 결과가 나올 수 있다. `__init__.py`를 수정한 뒤에도 마찬가지다.

## 패키지 안의 함수 실행하기

`echo.py`의 `echo_test` 함수를 실행하는 방법은 3가지다.

- **모듈까지 전부 import하기** — 호출할 때도 전체 경로를 다 적어야 한다.

  ```python
  import game.sound.echo
  game.sound.echo.echo_test()   # echo
  ```

- **모듈이 있는 디렉터리까지 from import하기**

  ```python
  from game.sound import echo
  echo.echo_test()   # echo
  ```

- **함수를 직접 import하기**

  ```python
  from game.sound.echo import echo_test
  echo_test()   # echo
  ```

반면 다음 두 가지는 불가능하다.

```python
import game
game.sound.echo.echo_test()
# AttributeError: 'module' object has no attribute 'sound'
```

```python
import game.sound.echo.echo_test
# ModuleNotFoundError: No module named 'game.sound.echo.echo_test';
#                      'game.sound.echo' is not a package
```

> `import game`을 수행하면 `game` 디렉터리의 `__init__.py`에 정의된 것만 참조할 수 있다. 또한 도트 연산자(`.`)로 `import a.b.c`처럼 쓸 때 **마지막 항목 `c`는 반드시 모듈 또는 패키지**여야 한다. 함수는 올 수 없다.

## \_\_init\_\_.py 파일의 용도

`__init__.py`는 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 이 파일이 없으면 패키지로 인식되지 않는다.

> 파이썬 3.3부터는 `__init__.py`가 없어도 패키지로 인식하지만, 만들어 두는 것이 파이썬 커뮤니티의 일반적인 관례다.

내용을 비워 둬도 되지만 패키지 설정이나 초기화 코드를 담을 수도 있다.

- **패키지 변수 및 함수 정의** — 패키지 수준의 공통 변수나 함수를 정의해 둘 수 있다.

  ```python
  # game/__init__.py
  VERSION = 3.5

  def print_version_info():
      print(f"The version of this game is {VERSION}.")
  ```

  ```python
  import game
  print(game.VERSION)         # 3.5
  game.print_version_info()   # The version of this game is 3.5.
  ```

- **패키지 내 모듈을 미리 import** — 패키지 안의 다른 모듈을 미리 import해 두면 패키지 사용 시 간편하게 접근할 수 있다.

  ```python
  # game/__init__.py
  from .graphic.render import render_test   # 맨 앞의 .은 현재 디렉터리를 의미한다.

  VERSION = 3.5

  def print_version_info():
      print(f"The version of this game is {VERSION}.")
  ```

  ```python
  import game
  game.render_test()   # render
  ```

- **패키지 초기화** — 패키지를 처음 불러올 때 실행할 코드를 작성할 수 있다. 데이터베이스 연결이나 설정 파일 로드 같은 작업이 여기에 해당한다.

  ```python
  # game/__init__.py
  from .graphic.render import render_test

  VERSION = 3.5

  def print_version_info():
      print(f"The version of this game is {VERSION}.")

  # 여기에 패키지 초기화 코드를 작성
  print("Initializing game...")
  ```

  ```python
  import game   # Initializing game...
  ```

  하위 모듈의 함수를 import할 때도 패키지 초기화 코드는 실행된다.

  ```python
  from game.graphic.render import render_test   # Initializing game...
  ```

  > 단, 초기화 코드는 **한 번만** 실행된다. `import game` 이후에 하위 모듈을 다시 import해도 초기화 코드가 또 실행되지는 않는다.

## \_\_all\_\_

패키지에서 `*`로 import하면 예상과 달리 모듈을 쓸 수 없다.

```python
from game.sound import *   # Initializing game...
echo.echo_test()
# NameError: name 'echo' is not defined
```

디렉터리(패키지)에서 `*`로 import하면 파이썬은 그 안의 어떤 모듈을 가져와야 할지 스스로 판단하지 못하기 때문이다. 그래서 `__all__` 변수로 "`*`로 import할 때 가져올 모듈 목록"을 직접 알려줘야 한다.

```python
# game/sound/__init__.py
__all__ = ['echo']
```

```python
from game.sound import *   # Initializing game...
echo.echo_test()           # echo
```

> 착각하기 쉬운데 `from game.sound.echo import *`는 `__all__`과 상관없이 import된다. 마지막 항목 `echo`가 모듈(파일)이므로 파이썬이 그 안의 모든 함수를 직접 가져올 수 있기 때문이다. `__all__`이 필요한 경우는 **`from`의 마지막 항목이 디렉터리(패키지)일 때뿐**이다.

## 상대 경로로 import하기

`graphic` 디렉터리의 `render.py`에서 `sound` 디렉터리의 `echo.py`를 사용하고 싶다면 전체 경로로 import하면 된다.

```python
# render.py
from game.sound.echo import echo_test

def render_test():
    print("render")
    echo_test()
```

같은 패키지 안이라면 상대 경로로 쓸 수도 있다. `..`은 `render.py`의 부모 디렉터리, 즉 `game`을 의미한다.

```python
# render.py
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()
```

어느 쪽으로 쓰든 실행 결과는 같다.

```python
from game.graphic.render import render_test   # Initializing game...
render_test()
# render
# echo
```

`render.py`를 기준으로 `.`과 `..`이 가리키는 위치는 다음과 같다.

```
game/                    ← ..  (부모 디렉터리)
├── __init__.py
├── sound/
│   ├── __init__.py
│   └── echo.py          ← ..sound.echo 로 접근
└── graphic/             ← .   (현재 디렉터리)
    ├── __init__.py
    └── render.py        ← 여기서 import
```

| 접근자 | 설명 |
| --- | --- |
| `..` | 부모 디렉터리 |
| `.` | 현재 디렉터리 |

## 실무에서는

위 예제는 패키지가 어떻게 인식되는지 보여주려고 최소 구성으로 만든 것이다. 디렉터리로 계층을 나누고 `__init__.py`를 두는 **구조 자체는 실무와 같지만**, 경로를 잡는 방법과 `__init__.py`에 넣는 내용은 다르다.

```
myproject/
├── pyproject.toml       ← 프로젝트 설정. pip install -e . 로 설치한다
├── src/
│   └── mypkg/           ← 위키 예제의 game/
│       ├── __init__.py  ← 공개 API 재수출 정도만
│       ├── sound/
│       │   ├── __init__.py
│       │   └── echo.py
│       └── graphic/
│           ├── __init__.py
│           └── render.py
└── tests/
```

- **경로는 `PYTHONPATH` 대신 설치로 잡는다** — `pyproject.toml`에 패키지 정보를 적고 `pip install -e .`로 설치하면 어느 위치에서 실행하든 `import mypkg`가 동작한다. 환경 변수는 터미널 세션마다 다시 설정해야 해서 실무에서는 거의 쓰지 않는다.

  ```toml
  # pyproject.toml
  [project]
  name = "mypkg"
  version = "0.1.0"
  requires-python = ">=3.11"
  dependencies = ["requests>=2.31"]

  [build-system]
  requires = ["hatchling"]
  build-backend = "hatchling.build"
  ```

  > 예전에는 `setup.py`에 파이썬 코드로 적었지만 지금은 `pyproject.toml`이 표준이다. `ruff`, `mypy`, `pytest` 같은 도구 설정도 이 파일에 함께 모아 둔다.

- **`__init__.py`는 공개 API를 만드는 용도로 쓴다** — 하위 모듈을 미리 import해 두면 사용자가 내부 구조를 몰라도 된다. 위에서 본 "패키지 내 모듈을 미리 import"가 실무에서 가장 많이 쓰이는 형태다.

  ```python
  # mypkg/__init__.py
  from .graphic.render import render_test

  __all__ = ["render_test"]   # 이 패키지의 공개 API
  ```

  ```python
  from mypkg import render_test   # 내부 경로를 몰라도 된다
  ```

- **import 시점에 부작용을 만들지 않는다** — `print`, DB 연결, 설정 파일 로드처럼 "패키지 초기화" 예제로 나온 코드는 실무에서 피한다. import만 했는데 뭔가 실행되면 import가 느려지고 테스트도 어려워진다. 그런 작업은 명시적인 함수로 빼서 프로그램 시작 지점에서 호출한다.

- **`import *`는 쓰지 않는다** — 이름이 어디서 왔는지 알 수 없어 린터도 경고한다. 따라서 `__all__`도 `*`를 위해서가 아니라, 위 예처럼 **공개 API 표식**으로 쓰는 경우가 대부분이다.

- **실행은 인터프리터 대신 진입점으로 한다** — `python -m mypkg`로 실행하거나, `pyproject.toml`의 `[project.scripts]`에 명령어를 등록해 터미널에서 바로 호출한다.

> 요즘은 `uv init`을 실행하면 `pyproject.toml`과 가상환경이 함께 만들어진다. 배포할 라이브러리가 아니어도 프로젝트를 시작할 때 기본으로 생기는 파일에 가깝다. 반대로 스크립트 몇 개를 모아 둔 저장소나 공부용 예제라면 없어도 된다.
