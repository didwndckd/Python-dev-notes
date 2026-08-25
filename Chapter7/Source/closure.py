# 클로저
# 외부 함수의 변수를 기억하는 내부 함수?

# 일반 함수
def mul3(n):
    return n * 3

def mul5(n):
    return n * 5

# 클래스
class Mul:
    def __init__(self, m):
        self.m = m

    # 일반 함수 정의
    def mul(self, n):
        return self.m * n

    # __call__: 객체를 함수처럼 호출할 수 있게 해주는 특수 메서드
    def __call__(self, n):
        return self.m * n

print("인스턴스 메서드")
mul_3 = Mul(3)
mul_5 = Mul(5)
print(mul_3.mul(10)) # 30
print(mul_5.mul(10)) # 50

print("__call__ 호출")
# __call__ 호출
print(mul_3(10)) # 30
print(mul_5(10)) # 50


# 클로져 반환
print("클로져 반환 함수")
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

mul3_result = mul(3)(10)
print(mul3_result)
mul5_result = mul(5)(10)
print(mul5_result)

# 데코레이터
# 클로저를 활용하여 기존 함수를 수정하지 않고 기능을 덧붙이는 기법
def myfunc():
    print("함수가 실행됩니다.")

myfunc() # 함수가 실행됩니다.

import time
def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간: %f 초" % (end - start))

myfunc()
# 실행 결과
# 함수가 실행됩니다.
# 함수 수행시간: 0.000002 초

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func() # 기존 함수 실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

elapsed(myfunc)()
# 실행 결과
# 함수가 실행됩니다.
# 함수 수행시간 0.000001 초

# 파이썬 데코레이터는 @ 문자를 이용해 함수 위에 적용 가능하다.
@elapsed # 위에 정의한 elapsed 함수를 감싼것
def myfunc():
    print("함수가 실행됩니다.")
myfunc()
# 실행 결과
# 함수가 실행됩니다.
# 함수 수행시간: 0.000002 초


@elapsed
def myfunc(msg):
    print("'%s'을 출력합니다." % msg)
# myfunc("You need python") # TypeError: elapsed.<locals>.wrapper() -> elapsed함수의 매개변수 original_func는 매개변수가 없는 함수를 받아야 해서 타입 에러

def elapsed(original_func):
    def wrapper(*args, **kwargs): # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs) # 전달받은 *args, **kwargs를 입력 파라미터로 기존 함수 수행
        end = time.time()
        print("⏱️함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper
# *arg: 모든 입력 인수를 튜플로 변환하는 매개변수
# **kwargs: 모든 키=값 형태의 인수를 딕셔너리로 변환하는 매개변수

@elapsed
def myfunc(msg):
    """데코레이터 확인 함수"""
    print("'%s'을 출력합니다." % msg)

myfunc('ㅎㅇㅎㅇ')
# 실행 결과
# 'ㅎㅇㅎㅇ'을 출력합니다.
# 함수 수행시간: 0.000002 초

a = 1
def foo():
    return a

print(a)