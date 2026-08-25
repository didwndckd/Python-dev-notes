# 클로저와 데코레이터(closure/decorator)

> 예제 코드: [Source/closure.py](Source/closure.py)

- [클로저란?](#클로저란)
- [일반적인 외부값 참조와 차이](#일반적인-외부값-참조와-차이)
- [함수는 객체이다](#함수는-객체이다)
- [클래스로 곱셈 함수 만들기](#클래스로-곱셈-함수-만들기)
- [클로저로 곱셈 함수 만들기](#클로저로-곱셈-함수-만들기)
- [데코레이터란?](#데코레이터란)
- [@로 데코레이터 적용하기](#로-데코레이터-적용하기)
- [매개변수가 있는 함수에 데코레이터 적용하기](#매개변수가-있는-함수에-데코레이터-적용하기)

## 클로저란?

클로저(closure)는 외부 함수 안에서 만든 내부 함수가 외부 함수의 지역 변수 바인딩을 함께 유지하는 상태를 말한다. 외부 함수의 실행이 끝난 뒤에도 내부 함수는 그 지역 변수를 계속 사용할 수 있다.

```python
def 외부_함수(외부_변수):
    def 내부_함수(매개변수):
        return 외부_변수 * 매개변수
    return 내부_함수
```

## 일반적인 외부값 참조와 차이

모든 함수는 전역 변수처럼 자신보다 바깥 스코프의 값을 사용할 수 있다. 하지만 전역 변수는 프로그램이 실행되는 동안 전역 스코프에 남아 있으므로, 단순히 전역 변수를 참조한다고 클로저가 되는 것은 아니다.

```python
tax = 0.1

def price_with_tax(price):
    return price * (1 + tax)

print(price_with_tax(10000))   # 11000.0
```

클로저는 이미 실행이 끝난 외부 함수의 **지역 변수**를 내부 함수가 계속 사용한다는 점이 다르다.

```python
def make_multiplier(m):
    def multiply(n):
        return m * n
    return multiply

mul3 = make_multiplier(3)   # make_multiplier()는 여기서 종료
print(mul3(10))              # 30, multiply()는 m을 계속 사용
```

> 클로저가 유지하는 것은 값의 단순한 복사본이라기보다 외부 지역 변수의 바인딩이다. 따라서 `nonlocal`을 사용하면 내부 함수에서 그 변수를 변경하며 상태를 유지할 수도 있다.

## 함수는 객체이다

파이썬에서 함수는 숫자나 문자열처럼 객체로 다뤄진다. 따라서 함수는 변수에 저장할 수 있고, 다른 함수의 인수로 전달하거나 함수의 반환값으로 사용할 수 있다. 이 성질 덕분에 `return multiply`로 클로저를 돌려주고, 데코레이터에 기존 함수를 전달할 수 있다.

```python
def say():
    print("안녕하세요.")

func = say       # 함수를 변수에 저장
func()            # 안녕하세요.

def run(function):
    function()    # 함수를 인수로 전달받아 호출

run(say)          # 안녕하세요.
```

특정 수를 곱하는 함수를 매번 따로 만들면 `mul3()`, `mul5()`처럼 비슷한 함수가 계속 늘어난다.

```python
def mul3(n):
    return n * 3

def mul5(n):
    return n * 5
```

## 클래스로 곱셈 함수 만들기

클래스는 곱할 값 `m`을 인스턴스 변수에 저장해 두었다가, `mul()` 메서드를 호출할 때 사용한다. `__call__()`을 정의하면 인스턴스 자체를 함수처럼 호출할 수도 있다.

```python
class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

    def __call__(self, n):
        return self.m * n

mul_3 = Mul(3)
mul_5 = Mul(5)

print(mul_3.mul(10))   # 30
print(mul_5.mul(10))   # 50

print(mul_3(10))       # 30
print(mul_5(10))       # 50
```

> `__call__`은 객체 뒤에 괄호를 붙여 호출했을 때 실행되는 특수 메서드이다. 따라서 `mul_3(10)`은 `mul_3.__call__(10)`과 같이 동작한다.

## 클로저로 곱셈 함수 만들기

클로저를 사용하면 클래스를 만들지 않고도 특정 값을 기억하는 함수를 만들 수 있다. `mul(3)`이 반환한 `wrapper`는 외부 함수가 끝난 뒤에도 `m`의 값인 `3`을 기억한다.

```python
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

mul3_result = mul(3)(10)
print(mul3_result)   # 30

mul5_result = mul(5)(10)
print(mul5_result)   # 50
```

`mul()`처럼 클로저를 만들어 반환하는 함수를 클로저 팩토리 함수라고 한다. 호출할 때마다 각각의 외부 변수 값을 기억하는 새 클로저가 만들어진다.

## 데코레이터란?

데코레이터(decorator)는 클로저를 이용해 기존 함수를 직접 수정하지 않고 기능을 덧붙이는 기법이다. 아래 `elapsed()`는 전달받은 함수의 실행 전후 시간을 기록해 수행 시간을 출력한다.

```python
import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()   # 기존 함수 실행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

elapsed(myfunc)()
# 함수가 실행됩니다.
# 함수 수행시간: 0.000001 초
```

`elapsed(myfunc)`는 `myfunc`를 기억하는 `wrapper` 함수를 반환한다. 반환값을 변수에 담아 호출해도 된다.

```python
decorated_myfunc = elapsed(myfunc)
decorated_myfunc()
```

## @로 데코레이터 적용하기

`@데코레이터_함수`를 함수 정의 바로 위에 붙이면 데코레이터를 간결하게 적용할 수 있다. `@elapsed`는 `myfunc = elapsed(myfunc)`과 같은 의미이다.

```python
@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()
# 함수가 실행됩니다.
# 함수 수행시간: 0.000002 초
```

## 매개변수가 있는 함수에 데코레이터 적용하기

인수를 받는 함수를 `wrapper()`처럼 매개변수 없는 함수로 감싸면 `TypeError`가 발생한다. 데코레이터는 어떤 함수에 붙을지 알 수 없으므로 `*args`, `**kwargs`로 모든 인수를 받아 원래 함수에 다시 전달한다.

```python
def 데코레이터(기존_함수):
    def wrapper(*args, **kwargs):
        return 기존_함수(*args, **kwargs)
    return wrapper
```

```python
def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("⏱️함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed
def myfunc(msg):
    """데코레이터 확인 함수"""
    print("'%s'을 출력합니다." % msg)

myfunc('ㅎㅇㅎㅇ')
# 'ㅎㅇㅎㅇ'을 출력합니다.
# ⏱️함수 수행시간: 0.000002 초
```

- `*args`는 위치 인수를 튜플로 받는다.
- `**kwargs`는 `키=값` 형태의 키워드 인수를 딕셔너리로 받는다.

> 데코레이터 안에서 원래 함수의 반환값을 `return`해야, 값을 반환하는 함수에도 데코레이터를 안전하게 적용할 수 있다.
