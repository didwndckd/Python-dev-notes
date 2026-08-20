# import: 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 블러올 수 있음
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말함.
# 모듈 전체 사용
# import 모듈_이름
# 모듈 일부만 사용, 내부 모듈처럼 사용
# from 모듈_이름 import 모듈_함수1, 모듈_함수2, ...

# import로 모듈을 추가하면 모듈_이름.함수() 방식으로 호출해야함
import mod1
# print(add(1, 2)) # 에러 발생
print(mod1.add(1, 2)) # 3
print(mod1.sub(2, 1)) # 1

# from, import를 사용하면 내부 함수처럼 사용 가능, 대신 import 선언한 함수만 사용 가능
from mod1 import add
print(add(1, 2)) # 3
# print(sub(2, 1)) # 에러 발생, add만 import 함

# 여러개의 함수를 import 할 수 있음
from mod1 import add, sub
print(add(1, 2)) # 3
print(sub(2, 1)) # 1

# import *를 사용하면 모든 함수를 내부 함수처럼 사용 가능
from mod1 import *
print(add(1, 2)) # 3
print(sub(2, 1)) # 1


# if __name__ == "__main__"
# mod1.py 마지막에 print("import mod1")이라는 코드를 추가했음
import mod1 # 아무것도 하지않고 import mod1만 넣어도 "import mod1"라는 문자가 출력된다.

# from mod1 import add # 일부 함수만 import 해도 결과는 마찬가지로 "import mod1"이라는 문자가 출력된다.

# mod1.py의 출력문을 if __name__ == "__main__": 블록에 넣었다.
import mod1 as mod1 # 아무 출력도 나오지 않는다.

# __name__ 변수: 파이썬이 내부적으로 사용하는 특수 변수 이름, 직접 mod1.py파일을 실행한 경우(python3 mod1.py) __name__변수는 "__main__"이 된다.
print(mod1.__name__) # mod1: 외부 모듈에서 사용할 때 __name__은 모듈 이름이 된다.

# 클래스나 변수 등을 포함한 모듈 사용, 전과 동일하게 모두 사용 하능
import mod2
print(mod2.PI) # 3.141592

math = mod2.Math()
solv = math.solv(2)
print(solv) # 12.566368
result = mod2.add(solv, 4.4)
print(result) # 16.966368000000003

# 다른 경로에 있는 모듈 추가(sub_modules/mod3.py로 실험)
# import mod3 # 그냥 추가하면 에러

# sys.path.append 사용
import sys
print(sys.path) # ['/Users/yjc/Workspace/Python-dev-notes/Chapter4/Source/modules', ...]
# sys.path.append("/Users/yjc/Workspace/Python-dev-notes/Chapter4/Source/modules/sub_modules") # sub_modules 디렉터리 추가

# import mod3
# mod3.call_module_name() # mod3: 호출 된다

# PYTHONPATH 환경 변수 사용하기
# $ export PYTHONPATH=모듈_경로
# $ export PYTHONPATH=~/Workspace/Python-dev-notes/Chapter4/Source/modules/sub_modules
# $ python3                                                                                                                                                                                                                                               ─╯
# Python 3.14.6 (main, Jun 10 2026, 10:03:53) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# Cmd click to launch VS Code Native REPL
# >>> import mod3
# >>> mod3.call_module_name()
# mod3
