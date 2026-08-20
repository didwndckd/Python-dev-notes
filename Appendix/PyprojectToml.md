# pyproject.toml

> 관련 문서: [패키지(package)](../Chapter4/Package.md), [가상 환경(venv)](VirtualEnvironment.md), [uv](Uv.md)

- [pyproject.toml이란](#pyprojecttoml이란)
- [build-system](#build-system)
- [project 기본 정보](#project-기본-정보)
- [의존성 지정 문법](#의존성-지정-문법)
- [선택 의존성과 개발 의존성](#선택-의존성과-개발-의존성)
- [project.scripts 명령어 등록](#projectscripts-명령어-등록)
- [tool 도구 설정 모으기](#tool-도구-설정-모으기)
- [편집 가능 설치](#편집-가능-설치)
- [전체 예시](#전체-예시)

## pyproject.toml이란

프로젝트에 관한 정보를 한곳에 모아 두는 설정 파일이다. 이름, 버전, 필요한 패키지 같은 정보를 적고, 여러 도구가 이 파일을 함께 읽는다.

| 읽는 쪽 | 사용하는 부분 |
| --- | --- |
| pip, uv, Poetry | `[project]`의 의존성 목록 |
| 빌드 도구(hatchling, setuptools) | `[build-system]`, 패키지 정보 |
| ruff, mypy, pytest | `[tool.*]`의 각자 설정 |

예전에는 이 역할을 `setup.py`가 파이썬 코드로 처리했지만, 지금은 `pyproject.toml`이 표준이다. 코드가 아닌 데이터 형식이라 실행하지 않고도 내용을 읽을 수 있다는 점이 큰 차이다.

TOML은 설정 파일을 위한 형식으로, `키 = 값`과 `[테이블]`로 이루어진다. 문자열은 큰따옴표로 감싸고 목록은 대괄호로 적는다.

> 이 파일이 필요한 것은 배포용 라이브러리를 만들 때만이 아니다. 의존성 관리나 도구 설정 용도로도 쓰이므로, 실제 프로젝트를 시작하면 대부분 생긴다. 반대로 스크립트를 모아 둔 공부용 저장소라면 없어도 된다.

## build-system

이 프로젝트를 설치 가능한 패키지로 만들 때 **어떤 도구로 빌드할지** 지정한다. `pip install .`이나 `pip install -e .`를 하면 pip이 이 항목을 보고 빌드 도구를 먼저 설치한 뒤 작업을 넘긴다.

```toml
[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"
```

- `requires` — 빌드에 필요한 도구. 이 목록은 프로젝트 실행에는 쓰이지 않는다.
- `build-backend` — 실제 빌드를 담당할 모듈 경로.

자주 쓰이는 빌드 백엔드는 세 가지다.

| 백엔드 | 설정 |
| --- | --- |
| hatchling | `requires = ["hatchling"]` / `build-backend = "hatchling.build"` |
| setuptools | `requires = ["setuptools"]` / `build-backend = "setuptools.build_meta"` |
| flit | `requires = ["flit_core <4"]` / `build-backend = "flit_core.buildapi"` |

> 어느 것을 골라도 만들어지는 결과물은 같은 형식이다. 새로 시작한다면 설정이 간단한 hatchling이 무난하다.

## project 기본 정보

프로젝트 자체를 설명하는 항목들이다. `name`만 필수이고 나머지는 필요한 것만 적으면 된다.

```toml
[project]
name = "mypkg"
version = "0.1.0"
description = "한 줄 설명"
readme = "README.md"
requires-python = ">=3.11"
license = "MIT"
authors = [
    { name = "홍길동", email = "hong@example.com" },
]
keywords = ["example", "study"]
```

| 항목 | 설명 |
| --- | --- |
| `name` | 패키지 이름. 유일한 필수 항목이며 자동 생성할 수 없다 |
| `version` | 버전. 코드에서 가져오려면 `dynamic`으로 지정한다 |
| `description` | 한 줄 설명 |
| `readme` | 긴 설명으로 쓸 파일 경로 |
| `requires-python` | 지원하는 파이썬 버전 범위 |
| `license` | SPDX 형식의 라이선스 표기(예: `"MIT"`, `"Apache-2.0"`) |
| `authors` | 작성자 목록. `name`, `email`을 가진 테이블의 배열 |
| `classifiers` | PyPI 분류 태그 |

주소는 별도 테이블에 적는다.

```toml
[project.urls]
Homepage = "https://example.com"
Repository = "https://github.com/me/mypkg.git"
"Bug Tracker" = "https://github.com/me/mypkg/issues"
```

버전처럼 빌드 도구가 계산해 주는 값은 `dynamic`에 이름을 적어 둔다. 코드의 `__version__`이나 git 태그에서 가져올 때 쓴다.

```toml
[project]
name = "mypkg"
dynamic = ["version"]
```

## 의존성 지정 문법

프로젝트가 동작하는 데 필요한 패키지를 적는다. [requirements.txt](VirtualEnvironment.md#패키지-목록-공유하기requirementstxt)와 달리 **직접 사용하는 것만** 적고, 버전은 정확한 값 대신 범위로 지정하는 것이 일반적이다.

```toml
[project]
dependencies = [
    "httpx",
    "requests>=2.31,<3",
    "gidgethub[httpx]>4.0.0",
    "django>2.1; os_name != 'nt'",
]
```

| 표기 | 의미 |
| --- | --- |
| `requests` | 버전을 가리지 않음 |
| `requests>=2.31` | 2.31 이상 |
| `requests>=2.31,<3` | 2.31 이상 3 미만. 가장 많이 쓰는 형태 |
| `requests==2.31.0` | 정확히 이 버전 |
| `requests~=2.31` | 2.31 이상이면서 2.x 안에서만. `>=2.31,<3`과 같은 뜻 |
| `requests[socks]` | 그 패키지의 선택 기능(extras)까지 함께 설치 |
| `django; os_name != 'nt'` | 조건에 맞는 환경에서만 설치(환경 마커) |

> 범위로 적는 이유는 이 파일이 "무엇이 필요한가"를 적는 곳이기 때문이다. 정확한 버전 고정은 잠금 파일([uv.lock](Uv.md#프로젝트로-관리하기) 등)이나 `requirements.txt`가 맡는다. 둘의 역할이 다르다.

## 선택 의존성과 개발 의존성

필수는 아니지만 특정 상황에 필요한 패키지를 적는 방법이 두 가지 있다. 목적이 다르므로 구분해서 쓴다.

**선택 의존성(extras)** — 이 패키지를 쓰는 **사용자**에게 제공하는 선택 기능이다.

```toml
[project.optional-dependencies]
gui = ["PyQt5"]
cli = ["rich", "click"]
```

```bash
python3 -m pip install "mypkg[gui]"        # gui 기능까지 함께 설치
```

**개발 의존성(dependency groups)** — 테스트나 린트처럼 **개발할 때만** 필요하고 배포물에는 들어가지 않아야 하는 것들이다.

```toml
[dependency-groups]
coverage = ["coverage[toml]"]
test = ["pytest>7", { include-group = "coverage" }]
docs = ["sphinx"]
```

```bash
python3 -m pip install --group test        # test 그룹만 설치
```

`include-group`으로 다른 그룹을 끌어다 쓸 수 있다. 위 예에서 `test`는 `["pytest>7", "coverage[toml]"]`로 펼쳐진다.

| | `[project.optional-dependencies]` | `[dependency-groups]` |
| --- | --- | --- |
| 대상 | 패키지를 쓰는 사용자 | 프로젝트를 개발하는 사람 |
| 배포물에 포함 | 포함된다 | 포함되지 않는다 |
| 설치 | `pip install "mypkg[gui]"` | `pip install --group test` |
| 그룹 참조 | 불가 | `include-group`으로 가능 |
| 표준 | PEP 621 | PEP 735(2024년 승인) |

> 배포하지 않는 웹 서비스나 사내 프로젝트라면 개발 도구는 `[dependency-groups]`에 넣는 것이 맞다. 예전에는 마땅한 자리가 없어 `optional-dependencies`에 `dev`라는 이름으로 넣는 관행이 있었는데, 지금은 표준이 생겼다.
>
> 비교적 최근에 정해진 규격이라 도구별로 지원 시점이 다르다. uv에서는 `uv add --group test pytest`, `uv sync --group test`처럼 사용한다.

## project.scripts 명령어 등록

패키지 안의 함수를 터미널 명령어로 등록한다. 설치하면 그 이름을 바로 실행할 수 있다.

```toml
[project.scripts]
mycmd = "mypkg.cli:main"
```

`모듈경로:함수이름` 형식이다. 위 설정은 `mypkg/cli.py`의 `main` 함수를 `mycmd` 명령으로 연결한다.

```bash
mycmd --help          # python -m mypkg.cli 대신 이렇게 실행된다
```

창을 띄우는 GUI 프로그램은 `[project.gui-scripts]`에 적는다. 윈도우에서 콘솔 창 없이 실행되는 점만 다르다.

## tool 도구 설정 모으기

`[tool.도구이름]` 형태로 각 도구의 설정을 이 파일에 함께 둘 수 있다. 설정 파일이 프로젝트 루트에 흩어지는 것을 막아 준다.

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.mypy]
strict = true
```

각 도구가 자기 이름의 테이블만 읽으므로, 서로 간섭하지 않는다. 어떤 항목을 쓸 수 있는지는 도구마다 다르니 해당 도구 문서를 확인한다.

## 편집 가능 설치

`pyproject.toml`이 있으면 프로젝트 자체를 패키지로 설치할 수 있다. 이때 `-e`(editable) 옵션을 쓰면 **파일을 복사하지 않고 현재 폴더를 그대로 연결**한다.

```bash
python3 -m pip install -e .
```

이렇게 하면 어느 위치에서 실행하든 `import mypkg`가 동작하고, 코드를 고쳐도 다시 설치할 필요가 없다. `sys.path`나 `PYTHONPATH`를 건드리는 방법보다 안정적이라 실무에서 이 방식을 쓴다. 자세한 내용은 [패키지(package)](../Chapter4/Package.md) 문서에 있다.

> `-e` 없이 `pip install .`을 하면 그 시점의 코드가 복사되어 설치된다. 이후 코드를 고쳐도 반영되지 않는다.

## 전체 예시

앞의 내용을 모은 형태다. 실제로는 이 중 필요한 부분만 적으면 된다.

```toml
[project]
name = "mypkg"
version = "0.1.0"
description = "예제 패키지"
readme = "README.md"
requires-python = ">=3.11"
license = "MIT"
authors = [
    { name = "홍길동", email = "hong@example.com" },
]
dependencies = [
    "requests>=2.31,<3",
    "Faker>=40",
]

[project.optional-dependencies]
cli = ["rich", "click"]

[project.scripts]
mycmd = "mypkg.cli:main"

[project.urls]
Repository = "https://github.com/me/mypkg.git"

[dependency-groups]
test = ["pytest>7", "coverage[toml]"]

[tool.ruff]
line-length = 100

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

> 참고: [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), [Dependency Groups 명세](https://packaging.python.org/en/latest/specifications/dependency-groups/), [PEP 621](https://peps.python.org/pep-0621/), [PEP 735](https://peps.python.org/pep-0735/)
