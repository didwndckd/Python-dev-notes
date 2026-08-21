# 가상 환경(venv)

> 관련 예제 코드: [외부 라이브러리 예제](../Chapter5/Source/advanced/external_library.py)

- [가상 환경이 필요한 이유](#가상-환경이-필요한-이유)
- [가상 환경 만들기](#가상-환경-만들기)
- [활성화와 비활성화](#활성화와-비활성화)
- [활성화의 원리](#활성화의-원리)
- [가상 환경 안인지 확인하기](#가상-환경-안인지-확인하기)
- [가상 환경 폴더의 구조](#가상-환경-폴더의-구조)
- [파이썬 버전은 격리되지 않는다](#파이썬-버전은-격리되지-않는다)
- [패키지 목록 공유하기(requirements.txt)](#패키지-목록-공유하기requirementstxt)
- [externally-managed-environment 오류](#externally-managed-environment-오류)
- [VS Code에서 사용하기](#vs-code에서-사용하기)
- [venv 명령 옵션](#venv-명령-옵션)

## 가상 환경이 필요한 이유

가상 환경은 프로젝트마다 독립된 패키지 설치 공간을 만들어 주는 기능이다. `venv`는 이를 위한 파이썬 표준 모듈이므로 따로 설치할 필요가 없다.

가상 환경 없이 `pip install`을 하면 모든 패키지가 시스템 파이썬 한 곳에 쌓인다. 이때 세 가지 문제가 생긴다.

- **버전 충돌** — A 프로젝트는 `django 4.2`가, B 프로젝트는 `django 5.1`이 필요해도 한 곳에는 하나만 설치할 수 있다.
- **의존성 파악 불가** — 설치된 패키지 목록만 봐서는 어떤 패키지가 어떤 프로젝트의 것인지 구분할 수 없다.
- **패키지 유실** — 파이썬을 새 버전으로 업그레이드하면 이전 버전에 설치해 둔 패키지가 함께 사라진다.

가상 환경은 프로젝트 폴더 안에 별도의 `site-packages`를 두어 이 문제를 해결한다.

## 가상 환경 만들기

`venv` 모듈에 만들 폴더 이름을 넘긴다. 프로젝트당 한 번만 실행하면 된다.

```bash
python3 -m venv .venv
```

폴더 이름은 자유지만 `.venv`가 관례다. 점으로 시작해 숨김 처리되고, 환경 변수 파일인 `.env`와 이름이 겹치지 않으며, 대부분의 편집기가 이 이름을 자동으로 인식한다.

> 잘못 만들었으면 폴더를 지우고 다시 만들면 된다. 가상 환경은 옮기거나 고쳐 쓰는 것이 아니라 **언제든 다시 만드는 일회용**으로 다루는 것이 원칙이다. 폴더를 다른 경로로 옮기면 내부 경로가 어긋나 동작하지 않는다.

## 활성화와 비활성화

만든 뒤에는 활성화해야 그 환경의 파이썬이 사용된다. 셸에 따라 실행할 스크립트가 다르다.

| 운영체제 | 셸 | 명령 |
| --- | --- | --- |
| macOS/리눅스 | bash, zsh | `source .venv/bin/activate` |
| macOS/리눅스 | fish | `source .venv/bin/activate.fish` |
| macOS/리눅스 | csh, tcsh | `source .venv/bin/activate.csh` |
| 윈도우 | cmd | `.venv\Scripts\activate.bat` |
| 윈도우 | PowerShell | `.venv\Scripts\Activate.ps1` |

활성화되면 프롬프트 앞에 환경 이름이 붙는다.

```bash
source .venv/bin/activate
# (.venv) yjc@mac Python-dev-notes %
```

이 상태에서 설치한 패키지는 모두 `.venv` 안에만 들어간다.

```bash
python3 -m pip install Faker
python3 -m pip list          # pip와 Faker만 보인다
```

빠져나올 때는 `deactivate`를 실행한다.

```bash
deactivate
```

> 활성화는 셸 단위로 적용된다. 터미널을 새로 열거나 탭을 바꾸면 풀리므로 그때마다 다시 실행해야 한다.

## 활성화의 원리

활성화 스크립트가 하는 일은 **`PATH` 환경 변수 맨 앞에 `.venv/bin`을 끼워 넣는 것**이다. 그래서 `python3`, `pip` 명령이 시스템 것이 아닌 가상 환경 안의 것으로 연결된다. 마법이 아니라 경로 전환일 뿐이다.

```bash
which python3
# /opt/homebrew/bin/python3                                   ← 활성화 전

source .venv/bin/activate
which python3
# /Users/yjc/Workspace/Python-dev-notes/.venv/bin/python3     ← 활성화 후
```

활성화는 편의 기능이므로 **필수가 아니다.** 경로를 직접 지정하면 활성화 없이도 같은 결과가 나온다.

```bash
.venv/bin/python3 -m pip install Faker
.venv/bin/python3 Chapter5/Source/advanced/external_library.py
```

> CI 스크립트나 Dockerfile에서는 오히려 이 방식을 쓴다. 어떤 파이썬으로 실행되는지 명시적이라 실수가 없다.

## 가상 환경 안인지 확인하기

`sys.prefix`는 현재 파이썬이 패키지를 찾는 경로이고, `sys.base_prefix`는 원본 파이썬의 경로다. 가상 환경 안에서는 이 둘이 달라진다.

```python
import sys

print(sys.prefix)                     # /Users/yjc/Workspace/Python-dev-notes/.venv
print(sys.base_prefix)                # /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14
print(sys.prefix != sys.base_prefix)  # True: 가상 환경 활성화 상태
```

셸에서는 `VIRTUAL_ENV` 환경 변수로도 확인할 수 있다. 활성화 스크립트가 이 값을 설정한다.

```bash
echo $VIRTUAL_ENV
# /Users/yjc/Workspace/Python-dev-notes/.venv
```

## 가상 환경 폴더의 구조

만들어진 `.venv` 안에는 세 가지가 들어 있다.

```
.venv/
├── bin/           ← 실행 파일과 활성화 스크립트 (윈도우는 Scripts/)
├── lib/
│   └── python3.14/
│       └── site-packages/   ← 설치한 패키지가 쌓이는 곳
└── pyvenv.cfg     ← 이 가상 환경의 설정 파일
```

`bin` 폴더의 파이썬은 복사본이 아니라 원본을 가리키는 심볼릭 링크다. 그래서 가상 환경 폴더 자체는 가볍다.

```
python     -> python3.14
python3    -> python3.14
python3.14 -> /opt/homebrew/opt/python@3.14/bin/python3.14   ← 실체는 여기
```

반면 `pip`은 링크가 아닌 실제 파일이다. 가상 환경 전용으로 새로 만들어지며, 설치 경로가 `.venv/lib/python3.14/site-packages`로 고정되어 있다.

`pyvenv.cfg`에는 이 환경이 어느 파이썬에서 만들어졌는지 기록된다.

```
home = /opt/homebrew/opt/python@3.14/bin
version = 3.14.6
include-system-site-packages = false
```

`include-system-site-packages = false`가 격리의 핵심이다. 시스템에 설치된 패키지를 무시한다는 뜻이며, `true`이면 시스템 패키지도 함께 보인다.

> 파이썬 3.13부터는 가상 환경을 만들 때 `.venv/.gitignore` 파일이 자동으로 생성된다. 내용은 `*` 한 줄이라 폴더 전체가 버전 관리에서 제외된다.

## 파이썬 버전은 격리되지 않는다

`venv`는 파이썬을 설치해 주지 않는다. 이미 설치된 파이썬 하나를 골라 그 껍데기를 만들 뿐이므로, **가상 환경을 만들 때 사용한 버전이 그대로 고정된다.**

```bash
python3.11 -m venv .venv   # 이 가상 환경은 3.11
python3.14 -m venv .venv   # 이 가상 환경은 3.14
```

`lib/python3.14`처럼 경로에 버전이 고정되고 `bin`의 링크도 특정 버전을 가리키므로, 다른 버전으로 바꾸려면 폴더를 지우고 다시 만들어야 한다.

정리하면 격리는 두 층으로 나뉜다.

- **파이썬 버전 격리** — `pyenv`, `uv`, Homebrew 등으로 파이썬 자체를 여러 개 설치한다.
- **패키지 격리** — `venv`로 그중 하나를 골라 가상 환경을 만든다.

버전을 여러 개 다뤄야 한다면 파이썬을 먼저 준비한 뒤 가상 환경을 만든다.

```bash
brew install python@3.11   # 설치하면 python3.11 명령이 생긴다
python3.11 -m venv .venv
```

> `--upgrade` 옵션이 있지만 다른 버전으로 갈아타는 기능은 아니다. 쓰던 파이썬이 제자리에서 갱신됐을 때(예: 3.14.6 → 3.14.7) 환경을 거기에 맞춰 주는 용도이고, 설치해 둔 패키지를 옮겨 주지는 않는다.

## 패키지 목록 공유하기(requirements.txt)

`.venv` 폴더는 용량이 크고 내부 경로가 컴퓨터마다 달라 **git에 올리지 않는다.** 대신 설치된 패키지 목록만 파일로 남겨 공유한다.

```bash
python3 -m pip freeze > requirements.txt      # 현재 설치된 목록을 파일로 저장
python3 -m pip install -r requirements.txt    # 파일에 적힌 대로 설치
```

`requirements.txt`에는 버전까지 함께 기록되므로, 다른 사람이나 다른 컴퓨터에서도 같은 구성을 그대로 재현할 수 있다.

```
Faker==40.36.0
```

`.gitignore`에는 가상 환경 폴더를 등록해 둔다.

```
.venv
venv/
```

## externally-managed-environment 오류

Homebrew나 리눅스 패키지 매니저로 설치한 파이썬에 그냥 `pip install`을 하면 다음 오류가 난다.

```bash
python3 -m pip install Faker
# error: externally-managed-environment
#
# × This environment is externally managed
```

파이썬 3.11부터 도입된 [PEP 668](https://peps.python.org/pep-0668/) 규칙이다. 패키지 매니저가 관리하는 파이썬에는 `pip`이 직접 설치하지 못하도록 막아 둔 안전장치로, 여기에 마음대로 설치하면 패키지 매니저가 설치한 다른 도구의 의존성을 덮어써 시스템을 망가뜨릴 수 있기 때문이다.

따라서 이것은 잘못된 동작이 아니라 정상이며, **해결책은 가상 환경을 만드는 것**이다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install Faker   # 이제 오류 없이 설치된다
```

> 오류 메시지가 안내하는 `--break-system-packages` 옵션으로 무시할 수도 있지만, 이름 그대로 시스템이 깨질 수 있으므로 쓰지 않는다. 가상 환경을 만드는 편이 명령 두 줄로 끝난다.
>
> 특정 도구를 명령어로만 쓰고 싶다면(예: `black`, `httpie`) `pipx`를 쓰는 방법도 있다. 도구마다 가상 환경을 자동으로 만들어 관리해 준다.

## VS Code에서 사용하기

인터프리터가 제대로 잡히면 상태 표시줄에 `Python 3.14.6 ('.venv': venv)`처럼 표시된다. 이 상태에서는 재생 버튼으로 실행할 때 활성화 없이도 가상 환경의 파이썬이 사용되고, 새 터미널을 열면 `activate`까지 자동으로 실행된다.

잡히지 않으면 `Cmd+Shift+P` → `Python: Select Interpreter`에서 `.venv/bin/python`을 직접 고른다. 이 선택은 `settings.json`이 아니라 VS Code 내부에 저장되므로 파일에는 보이지 않는다.

`.vscode/settings.json`의 아래 설정이 `system`으로 되어 있으면, 가상 환경을 만들어도 계속 시스템 파이썬을 사용한다.

```json
{
    "python-envs.defaultEnvManager": "ms-python.python:venv"
}
```

값을 바꾼 뒤에는 `Cmd+Shift+P` → `Developer: Reload Window`로 창을 다시 불러와야 반영된다.

## venv 명령 옵션

```bash
python3 -m venv [옵션] 폴더명
```

| 옵션 | 설명 |
| --- | --- |
| `--system-site-packages` | 시스템에 설치된 패키지도 함께 사용한다. 기본값은 사용하지 않음 |
| `--upgrade-deps` | 환경을 만들면서 `pip`을 최신 버전으로 올린다 |
| `--clear` | 같은 이름의 폴더가 이미 있으면 내용을 비우고 다시 만든다 |
| `--upgrade` | 제자리에서 갱신된 파이썬에 맞춰 기존 환경을 갱신한다 |
| `--prompt 이름` | 활성화했을 때 프롬프트에 표시할 이름을 지정한다 |
| `--without-pip` | `pip`을 설치하지 않는다. 기본은 설치함 |
| `--copies` | 심볼릭 링크 대신 실행 파일을 복사한다 |
| `--without-scm-ignore-files` | 자동으로 만들어지는 `.gitignore`를 생성하지 않는다 |

> 참고: [venv — 가상 환경 생성](https://docs.python.org/ko/3/library/venv.html), [파이썬 자습서: 가상 환경 및 패키지](https://docs.python.org/ko/3/tutorial/venv.html)
