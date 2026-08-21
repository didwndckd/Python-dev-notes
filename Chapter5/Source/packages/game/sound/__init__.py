# game/sound/__init__.py

# 이렇게 하면 from game.sound import *를 수행할 때 __all__에 정의된 echo 모듈을 import 하게 된다.
__all__ = ['echo']
# 착각하기 쉬운것: from game.sound.echo import *는 __all__과 상관없이 import 된다. 이 경우 from의 마지막 항목 echo가 모듈(파일)이므로 모든 함수를 직접 가져올 수 있기 때문.
# form game.sound import * 처럼 from의 마지막항목이 디렉터리(패키지)인 때 뿐이다.
