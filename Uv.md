# uv

> 관련 문서: [가상 환경(venv)](VirtualEnvironment.md), [패키지(package)](Package.md)

- [uv란](#uv란)
- [설치](#설치)
- [기존 방식 그대로 쓰기(pip 인터페이스)](#기존-방식-그대로-쓰기pip-인터페이스)
- [프로젝트로 관리하기](#프로젝트로-관리하기)
- [스크립트 하나만 실행하기](#스크립트-하나만-실행하기)
- [파이썬 버전 관리](#파이썬-버전-관리)
- [명령줄 도구 설치하기](#명령줄-도구-설치하기)
- [명령어 대조표](#명령어-대조표)
- [언제 도입할까](#언제-도입할까)

## uv란

`uv`는 Rust로 작성된 파이썬 패키지·프로젝트 관리자다. 지금까지 각각 다른 도구가 맡던 일을 하나의 명령으로 합친 것이 특징이다.

| 하는 일 | 기존 도구 | uv |
| --- | --- | --- |
| 파이썬 버전 설치 | pyenv | `uv python install` |
| 가상 환경 생성 | `python -m venv` | `uv venv` |
| 패키지 설치 | pip | `uv pip install` |
| 의존성 잠금 | pip-tools | `uv lock`, `uv pip compile` |
| 프로젝트 관리 | Poetry | `uv add`, `uv sync` |
| 명령줄 도구 설치 | pipx | `uv tool install` |

빠른 것도 장점이다. 다운로드를 병렬로 처리하고, 한 번 받은 패키지는 전역 캐시에 두었다가 하드 링크로 연결한다. 같은 패키지를 여러 프로젝트에서 써도 디스크에는 한 번만 저장되고 복사 시간도 들지 않는다.

> 아직 0.x 버전이라 옵션이 바뀌기도 한다. 사용할 때 [공식 문서](https://docs.astral.sh/uv/)를 함께 확인하는 것이 좋다.

## 설치

uv 자체는 파이썬으로 만들어진 프로그램이 아니므로, 파이썬이 없는 상태에서도 설치할 수 있다. 오히려 uv가 파이썬을 설치해 주는 쪽이다.

```bash
brew install uv                            # macOS
curl -LsSf https://astral.sh/uv/install.sh | sh   # 설치 스크립트
```

업데이트는 uv가 직접 처리한다.

```bash
uv self update
```

## 기존 방식 그대로 쓰기(pip 인터페이스)

명령 앞에 `uv`만 붙이면 `venv`, `pip`과 같은 방식으로 쓸 수 있다. 만들어지는 `.venv` 구조도 동일하고 `requirements.txt`도 그대로 사용한다. 개념이 같으므로 기존 프로젝트에 바로 얹을 수 있다.

```bash
uv venv                      # python3 -m venv .venv 와 같다
source .venv/bin/activate
uv pip install Faker         # python3 -m pip install Faker 와 같다
uv pip list
uv pip freeze > requirements.txt
uv pip install -r requirements.txt
```

파이썬 버전을 지정할 수 있고, 그 버전이 시스템에 없으면 uv가 알아서 내려받는다.

```bash
uv venv --python 3.11
```

활성화하지 않아도 동작한다. uv는 `VIRTUAL_ENV` 환경 변수를 먼저 보고, 없으면 현재 디렉터리부터 상위로 올라가며 `.venv` 폴더를 찾는다.

```bash
uv pip install Faker         # 활성화 없이도 .venv를 찾아 설치한다
```

> `uv venv`로 만든 환경에는 `pip`이 설치되지 않는다. uv가 자체 설치기를 쓰기 때문에 필요가 없어서인데, 그래서 이 환경에서 `python3 -m pip`을 실행하면 모듈을 찾지 못한다. `uv pip`을 쓰거나, `pip` 명령이 꼭 필요하면 `--seed` 옵션으로 만든다.
>
> ```bash
> uv venv --seed
> ```
>
> 파이썬 3.12 이상에서는 `pip`만 설치된다. 표준 `venv`가 3.12부터 `setuptools`, `wheel`을 기본 포함하지 않게 바뀐 것과 같은 이유다.

`requirements.txt`를 직접 관리한다면 잠금 명령도 있다. [pip-tools](VirtualEnvironment.md#패키지-목록-공유하기requirementstxt)의 `pip-compile`에 해당한다.

```bash
uv pip compile requirements.in -o requirements.txt   # 직접 의존성 -> 전체 목록 생성
uv pip sync requirements.txt                         # 파일과 환경을 정확히 일치시킨다
```

> `uv pip sync`는 `install`과 다르다. `install`은 없는 것을 추가하기만 하지만, `sync`는 파일에 없는 패키지를 지워서 환경을 파일 그대로 맞춘다.

## 프로젝트로 관리하기

`pyproject.toml`을 중심으로 의존성을 관리하는 방식이다. `pip install` 후 `pip freeze`를 따로 실행하던 두 단계가 한 번으로 합쳐진다.

```bash
uv init hello-world
cd hello-world
```

만들어지는 구조는 다음과 같다.

```
hello-world/
├── .git/
├── .gitignore
├── .python-version      ← 이 프로젝트가 사용할 파이썬 버전
├── pyproject.toml       ← 프로젝트 정보와 직접 의존성
├── README.md
└── src/
    └── hello_world/
        └── __init__.py
```

패키지를 추가하면 설치와 기록이 함께 이루어진다.

```bash
uv add Faker            # 설치 + pyproject.toml 기록 + uv.lock 갱신
uv remove Faker         # 제거 + 기록 정리
uv tree                 # 의존성 관계를 트리로 확인
```

이때 `.venv`와 `uv.lock`이 추가로 생긴다.

```
├── .venv/               ← 가상 환경. 명령 실행 시 자동으로 만들어진다
├── uv.lock              ← 잠금 파일. 정확한 버전 정보가 들어 있다
├── pyproject.toml
├── .python-version
└── src/
```

- **`pyproject.toml`** — 직접 사용하는 의존성만 범위로 적는다(예: `Faker>=40`). 사람이 읽고 관리하는 파일이며, 각 항목의 의미는 [pyproject.toml](PyprojectToml.md) 문서에 정리해 두었다.
- **`uv.lock`** — 딸려 오는 의존성까지 포함한 정확한 버전이 기록된다. 운영체제를 가리지 않는 형식이라 어디서든 같은 구성이 재현된다. 직접 편집하지 않는다.

실행할 때는 `uv run`을 쓴다. 가상 환경이 없으면 만들고, 잠금 파일과 다르면 맞춘 뒤 실행하므로 활성화가 필요 없다.

```bash
uv run python script.py
uv run pytest
```

받는 사람은 한 줄이면 된다. 파이썬 설치부터 가상 환경 생성, 패키지 설치까지 모두 처리된다.

```bash
git clone <저장소>
cd hello-world
uv sync
```

기존 프로젝트를 옮겨 올 때는 `requirements.txt`를 그대로 읽어 들일 수 있다.

```bash
uv add -r requirements.txt
```

> 버전 관리에는 `pyproject.toml`, `.python-version`, `uv.lock`을 함께 커밋하고 `.venv`는 제외한다. 잠금 파일을 커밋해야 팀원 모두가 같은 버전을 쓰게 된다.

## 스크립트 하나만 실행하기

프로젝트를 만들 정도가 아닌 파일 하나짜리 스크립트에도 의존성을 붙일 수 있다. 임시로 필요한 패키지는 `--with`로 지정한다. 설치는 캐시에 남고 프로젝트 환경은 건드리지 않는다.

```bash
uv run --with rich example.py
uv run --with 'rich>12,<13' example.py
```

스크립트 자체에 의존성을 적어 두는 방법도 있다. [PEP 723](https://peps.python.org/pep-0723/)이 정한 형식으로, 주석 블록에 기록한다.

```bash
uv add --script example.py 'requests<3' 'rich'
```

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint
```

이렇게 해 두면 파일 하나만 건네줘도 상대방이 `uv run example.py`로 바로 실행할 수 있다. 필요한 파이썬 버전과 패키지를 uv가 알아서 준비한다.

> `dependencies` 항목은 비어 있더라도 반드시 있어야 한다.

## 파이썬 버전 관리

[가상 환경은 파이썬 버전을 격리하지 않는다](VirtualEnvironment.md#파이썬-버전은-격리되지-않는다). 그 층을 uv가 함께 담당한다.

```bash
uv python list              # 설치 가능한 버전과 설치된 버전 확인
uv python install 3.11      # 특정 버전 설치
uv python pin 3.11          # 이 프로젝트의 버전 고정(.python-version 생성)
uv python uninstall 3.11
```

`uv venv --python 3.11`처럼 버전을 요청했을 때 그 버전이 없으면 자동으로 내려받으므로, 설치 명령을 미리 실행하지 않아도 되는 경우가 많다.

## 명령줄 도구 설치하기

`ruff`, `black`처럼 라이브러리가 아니라 명령어로 쓰는 도구는 프로젝트 의존성과 분리해서 관리한다. pipx가 하던 역할이다.

```bash
uvx ruff check .            # 설치 없이 일회성 실행
uv tool install ruff        # 전역 명령어로 설치
uv tool list
uv tool uninstall ruff
```

`uvx`는 `uv tool run`의 줄임말이다. 한 번 써 보고 말 도구라면 설치하지 않고 이쪽을 쓰면 된다.

## 명령어 대조표

| 기존 | uv |
| --- | --- |
| `python3 -m venv .venv` | `uv venv` |
| `source .venv/bin/activate` | (필요 없음. `uv run` 사용) |
| `python3 -m pip install Faker` | `uv pip install Faker` 또는 `uv add Faker` |
| `python3 -m pip uninstall Faker` | `uv pip uninstall Faker` 또는 `uv remove Faker` |
| `python3 -m pip list` | `uv pip list` |
| `python3 -m pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` |
| `python3 -m pip install -r requirements.txt` | `uv pip install -r requirements.txt` 또는 `uv sync` |
| `pip-compile requirements.in` | `uv pip compile requirements.in -o requirements.txt` |
| `pyenv install 3.11` | `uv python install 3.11` |
| `pipx install ruff` | `uv tool install ruff` |
| `python3 script.py` | `uv run script.py` |

## 언제 도입할까

학습 단계에서는 `venv`와 `pip`으로 먼저 익히는 편이 낫다. `uv sync` 한 줄 뒤에서 어떤 일이 일어나는지 알고 쓰는 것과 모르고 쓰는 것은 문제가 생겼을 때 차이가 크다. `PATH`, `pyvenv.cfg`, `site-packages`의 역할을 이해했다면 uv로 옮겨도 잃는 것이 없다.

실제 프로젝트를 시작할 때는 처음부터 uv로 시작하는 편이 편하다. 특히 여러 사람이 함께 작업한다면 잠금 파일이 있는 쪽이 환경 차이로 생기는 문제를 줄여 준다.

> 참고: [uv 공식 문서](https://docs.astral.sh/uv/), [기능 목록](https://docs.astral.sh/uv/getting-started/features/), [프로젝트 사용법](https://docs.astral.sh/uv/guides/projects/), [스크립트 실행](https://docs.astral.sh/uv/guides/scripts/)
