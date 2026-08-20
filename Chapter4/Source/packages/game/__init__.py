# game/__init__.py

# __init__.py 파일 내에 다른 모듈을 미리 import 하면 패키지 사용 시 간편하게 접근 가능.
from .graphic.render import render_test # 맨 앞의 .은 현재 디렉터리를 의미함.

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 여기에 패키지 초기화 코드를 작성
print("Initializing game...")