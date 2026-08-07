# 패키지(packages)란 관련있는 모듈의 집합이다. 패키지를 사용하면 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있다.
# 파이썬에서 모듈은 하나의 .py 파일이다.

# game 패키지 만들기
# game/__init__.py
# game/sound/__init__.py
# game/sound/echo.py
# game/graphic/__init__.py
# game/graphic/render.py

# 현재 파일(의도적으로 game, main을 분리): main/package.py

# 주의 사항
# 아래 예제들은 명령 프롬프트에서 진행한다. 하나의 예제를 실행 하고 다음 예제를 실행할 때 반드시 인터프리터를 종료(exit() 입력)하고 다시 실행 해야 한다.
# 파이썬은 한번 import한 모듈을 메모리에 저장해 두기 때문에, 인터프리터를 재시작 하지 않으면 이전에 import한 것이 남아있어 예상과 다른 결과가 나올 수 있음

# 패키지 사용해보기(프롬프트)

# 환경 변수 설정(프로젝트 루트에서 시작)
# $ export PYTHONPATH=Source/packages
# $ python3

# echo 모듈 import
# >>> import game.sound.echo # echo 모듈은 echo.py 파일이다.
# >>> game.sound.echo.echo_test()
# echo

# echo 모듈이 있는 디렉터리까지를 from ... import 하는 방법
# >>> from game.sound import echo
# >>> echo.echo_test()
# echo

# echo 모듈의 echo_test 함수를 직접 import하여 실행
# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo

# 다음과 같은 방법은 불가능: import game을 수행하면 game 디렉터리의 __init__.py에 정의된것만 사용 가능
# >>> import game
# >>> game.sound.echo.echo_test()
# Traceback (most recent call last):
#   File "<python-input-1>", line 1, in <module>
#     game.sound.echo.echo_test()
#     ^^^^^^^^^^
# AttributeError: module 'game' has no attribute 'sound'

# 다음과 같은 방법도 불가능: 도트 연산자(.)를 사용해서 import a.b.c처럼 import 할 때 마지막 항목인 c는 반드시 모듈 또는 패키지여야 한다.
# >>> import game.sound.echo.echo_test
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     import game.sound.echo.echo_test
# ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package

# __init__.py 파일의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만양 game, sound, graphic등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.
# python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식 하지만 __init__.py 파일을 생성하는 것이 파이썬 커뮤니티의 일반적 관례이므로 항상 만들어 주는 것이 좋다.
# __init__.py 파일은 패키지 설정이나 초기화 코드를 포함할 수도 있다.
# __init__.py 파일을 수정한 후에는 인터프리터를 재시작 해야 한다.

# game/__init__.py 수정 후 예제
# >>> import game
# >>> print(game.VERSION)
# 3.5
# >>> game.print_version_info()
# The version of this game is 3.5.

# __init__.py 파일 내에 다른 모듈을 미리 import 하면 패키지 사용 시 간편하게 접근 가능.(game/__init__.py 참고)
# >>> import game
# >>> game.render_test()
# render

## 패키지 초기화: __init__.py 파일에 패키지를 처음 불러올 때 실행할 코드를 작성할 수 있음, 예를 들어 데이터베이스 연결이나 설정 파일 로드같은 작업(game/__init__.py 참고)
# >>> import game
# Initializing game...

# 하위 모듈 함수를 import 하는 경우에도 실행된다.
# >>> from game.graphic.render import render_test
# Initializing game...

# 초기화 코드는 한번 실행된 후에는 다시 import 해도 실행되지 않는다.
# >>> import game
# Initializing game...
# >>> from game.graphic.render import render_test # 초기화 코드가 돌지 않음.
# >>> 

# __all__

# 아래의 경우 game.sound 패키지에서 모든 것(*)을 import 했으므로 echo 모듈을 사용할 수 있어야 할것 같은데, echo라는 이름이 정의되지 않았다는 오류가 발생한다.
# >>> from game.sound import *
# Initializing game...
# >>> echo.echo_test()
# Traceback (most recent call last):
#   File "<python-input-1>", line 1, in <module>
#     echo.echo_test()
#     ^^^^
# NameError: name 'echo' is not defined

# 디렉터리(패키지)에서 *를 사용하여 import 하면 파이썬은 해당 디렉터리 안에 어떤 모듈을 가져와야 할지 스스로 판단하지 못한다. 
# 그래서 __all__ 변수를 사용하여 "이 디렉터리에서 *로 import할 때 가져올 모듈 목록"을 직접 알려줘야 한다.(game/sound/__init__.py 참고)
# >>> from game.sound import *
# Initializing game...
# >>> echo.echo_test()
# echo

# 상대 경로 패키지
# graphic 디렉터리의 render.py 모듈에서 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까?(game/graphic/render.py 참고)
# >>> from game.graphic.render import render_test
# Initializing game...
# >>> render_test()
# render
# echo

# game/                 ← .. (부모 디렉터리)
#     __init__.py
#     sound/
#         __init__.py
#         echo.py       ← ..sound.echo로 접근
#     graphic/          ← .  (현재 디렉터리)
#         __init__.py
#         render.py     ← 여기서 import

# ..: 부모 디렉터리
# .: 현재 디렉터리

# 주의: 상대 경로 import는 이 파일에서 직접 실행할 수 없다.
# from ..game.sound import echo
# ImportError: attempted relative import with no known parent package
# 파일을 python3 package.py처럼 직접 실행하면 그 파일은 __main__이 되고 __package__가 비어 있어서
# ..이 가리킬 부모 패키지 자체가 존재하지 않는다. 파일의 위치와는 무관한 문제다.
# 상대 경로 import는 "패키지의 일부로 import될 때"만 동작한다.
# 즉 위 예시처럼 game/graphic/render.py 안에서 from ..sound.echo import echo_test로 쓰고,
# 그 render.py를 직접 실행하는 대신 여기서 game.graphic.render를 import해서 사용해야 한다.

# 참고: 패키지인지 확인하기
# 패키지(디렉터리)로 만들어진 모듈에는 __path__ 속성이 있다.
# >>> import game
# >>> hasattr(game, '__path__')
# True
# >>> import game.sound.echo
# >>> hasattr(game.sound.echo, '__path__')
# False -> echo는 모듈(파일)이라 __path__가 없다