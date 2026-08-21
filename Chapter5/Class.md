# 클래스(class)

> 예제 코드: [Source/advanced/class.py](Source/advanced/class.py)

- [클래스는 왜 필요한가](#클래스는-왜-필요한가)
- [기본 구조](#기본-구조)
- [클래스와 객체](#클래스와-객체)
- [self는 무엇인가](#self는-무엇인가)
- [사칙 연산 클래스 만들기](#사칙-연산-클래스-만들기)
- [생성자(\_\_init\_\_)](#생성자__init__)
- [클래스의 상속](#클래스의-상속)
- [메서드 오버라이딩](#메서드-오버라이딩)
- [클래스 변수](#클래스-변수)

## 클래스는 왜 필요한가

계산기는 이전에 계산한 결괏값을 어딘가에 기억하고 있어야 한다. 함수만으로 만들면 결괏값을 전역 변수에 담아야 하는데, 계산기가 2대 필요해지는 순간 전역 변수와 함수를 각각 따로 만들어야 한다.

```python
result1 = 0
result2 = 0

def add1(num):     # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):     # 계산기2
    global result2
    result2 += num
    return result2
```

계산기가 3개, 5개, 10개로 늘어나면 그때마다 전역 변수와 함수를 추가해야 한다. 클래스를 사용하면 객체를 하나 더 만드는 것만으로 해결된다.

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))   # 3
print(cal1.add(4))   # 7
print(cal2.add(3))   # 3
print(cal2.add(7))   # 10
```

`cal1`과 `cal2`는 같은 클래스로 만들었지만 각자의 `result`를 독립적으로 유지한다. 기능을 추가하고 싶으면 클래스에 메서드를 하나 더 넣으면 된다.

> 클래스는 함수나 자료형처럼 반드시 필요한 요소는 아니다. C 언어에는 클래스가 없고, 클래스 없이 작성한 파이썬 프로그램도 많다. 다만 적재적소에 쓰면 얻는 이익이 크다.

## 기본 구조

`class` 예약어로 선언하고, 클래스 안에 구현된 함수를 **메서드(method)**라고 부른다. 메서드는 클래스에 포함되어 있다는 점만 빼면 일반 함수와 다르지 않다.

```python
class 클래스_이름:
    def 메서드_이름(self, 매개변수):
        실행 코드
```

## 클래스와 객체

클래스(class)는 똑같은 무언가를 계속 만들어 낼 수 있는 **설계 도면**(과자 틀)이고, 객체(object)는 그 클래스로 만들어 낸 **피조물**(과자 틀로 찍어 낸 과자)이다. 클래스 하나로 무수히 많은 객체를 만들 수 있으며, 각 객체는 서로 전혀 영향을 주지 않는다.

`pass`만 있는 껍질뿐인 클래스도 객체를 만드는 기능은 가지고 있다.

```python
class Cookie:
    pass

a = Cookie()   # Cookie()의 반환값을 받은 a가 객체
```

- **객체와 인스턴스의 차이** — `a = Cookie()`로 만든 `a`는 객체이고, 동시에 `Cookie`의 인스턴스이다. 인스턴스라는 말은 특정 객체가 어떤 클래스로부터 나왔는지 **관계 위주로** 설명할 때 쓴다. "a는 객체이다", "a는 Cookie의 인스턴스이다"라는 표현이 자연스럽다.

- **선언하지 않은 변수도 할당할 수 있다** — 클래스 안에 정의해 두지 않은 변수도 객체에 나중에 붙일 수 있다.

  ```python
  a.some_number = 1
  a.some_str = "python"
  print(a.some_number)   # 1
  print(a.some_str)      # python
  ```

## self는 무엇인가

메서드의 첫 번째 매개변수 `self`에는 **그 메서드를 호출한 객체 자신**이 자동으로 전달된다. 그래서 정의할 때는 `self`를 적지만 호출할 때는 넘기지 않는다.

```python
cal1.add(1)              # self 자리에 cal1이 자동으로 들어간다
Calculator.add(cal1, 1)  # 위 코드와 동일. 이때는 cal1을 직접 넘겨야 한다
```

`객체.메서드()` 형태로 호출하면 `self`를 반드시 생략하고, `클래스.메서드()` 형태로 호출하면 객체를 첫 번째 인수로 꼭 전달해야 한다.

> `self`라는 이름은 관례일 뿐 다른 이름을 써도 동작한다. 첫 번째 매개변수 `self`를 명시적으로 적는 것은 파이썬만의 독특한 특징으로, 자바 같은 언어에는 없다.

## 사칙 연산 클래스 만들기

두 숫자를 지정하고 더하기·빼기·곱하기·나누기를 수행하는 `FourCal` 클래스를 만들어 보자. 연산에 쓸 두 숫자는 `setdata` 메서드로 객체에 지정한다.

```python
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

cal = FourCal()
cal.setdata(4, 2)
print(cal.first)    # 4
print(cal.second)   # 2
print(cal.add())    # 6
print(cal.sub())    # 2
print(cal.mul())    # 8
print(cal.div())    # 2.0
```

`cal.setdata(4, 2)`를 호출하면 `self`에 `cal`이 전달되므로 수행문은 `cal.first = 4`, `cal.second = 2`로 해석된다. 이렇게 객체에 생기는 변수를 **객체변수**(인스턴스 변수, 속성)라고 한다.

- **객체변수는 객체마다 독립적이다** — 한 객체의 값을 바꿔도 다른 객체는 영향을 받지 않는다.

  ```python
  a = FourCal()
  b = FourCal()
  a.setdata(4, 2)
  b.setdata(3, 7)
  print(a.first)   # 4: b의 값에 영향받지 않는다
  print(b.first)   # 3
  ```

> `setdata`를 호출하기 전에는 `first`, `second`가 아직 만들어지지 않았으므로 접근하면 오류가 난다.
>
> ```python
> # print(cal.first)   # AttributeError: 'FourCal' object has no attribute 'first'
> # print(cal.add())   # AttributeError
> ```

## 생성자(\_\_init\_\_)

생성자(constructor)는 **객체가 생성되는 시점에 자동으로 호출되는 메서드**이다. 메서드 이름을 `__init__`으로 지으면 생성자가 된다. 위의 `setdata`처럼 초깃값 설정을 별도 메서드에 맡기면 호출을 깜빡했을 때 오류가 나므로, 생성자를 쓰는 편이 안전하다.

```python
def __init__(self, 매개변수1, 매개변수2, ...):
    실행 코드
```

```python
class FourCal:
    def __init__(self, first, second):   # 생성자 추가
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

cal = FourCal(4, 2)
print(cal.first)    # 4
print(cal.second)   # 2
print(cal.add())    # 6
print(cal.sub())    # 2
print(cal.mul())    # 8
print(cal.div())    # 2.0
```

> 생성자에 매개변수가 있으면 객체를 만들 때 값을 반드시 전달해야 한다.
>
> ```python
> # cal = FourCal()
> # TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
> ```

`__init__`도 다른 메서드와 마찬가지로 첫 번째 매개변수 `self`에 생성되는 객체가 자동으로 전달된다. `__init__`의 `init` 앞뒤에 붙은 `__`는 밑줄(`_`) 2개다.

## 클래스의 상속

상속(inheritance)은 다른 클래스의 기능을 물려받는 것이다. 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣는다.

```python
class 클래스_이름(상속할_클래스_이름):
    실행 코드
```

```python
class MoreFourCal(FourCal):
    def pow(self):
        """
        first^second: first의 second제곱
        """
        return self.first ** self.second

cal = MoreFourCal(4, 2)
print(cal.first)    # 4
print(cal.second)   # 2
print(cal.add())    # 6
print(cal.sub())    # 2
print(cal.mul())    # 8
print(cal.div())    # 2.0
print(cal.pow())    # 16: 4의 2제곱
```

부모인 `FourCal`의 모든 기능을 그대로 쓰면서 `pow` 기능만 추가되었다.

> 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 상속을 쓸까? 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 써야 한다. 상속은 기존 클래스는 그대로 둔 채 기능을 확장할 때 주로 사용한다.

## 메서드 오버라이딩

부모 클래스에 있는 메서드를 **동일한 이름으로 다시 만드는 것**을 메서드 오버라이딩(method overriding)이라고 한다. 오버라이딩하면 부모의 메서드 대신 새로 만든 메서드가 호출된다.

`FourCal`의 `div`는 나누는 값이 0이면 `ZeroDivisionError`가 발생한다. 오류 대신 0을 반환하도록 자식 클래스에서 다시 작성해 보자.

```python
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

    # 메서드 오버라이딩: 부모의 메서드를 동일한 이름으로 다시 만드는 것
    def div(self):
        """
        부모에는 없는 second(나누는 숫자)가 0인 경우의 예외 처리를 추가
        """
        if self.second == 0: return 0
        return self.first / self.second

cal = MoreFourCal(4, 0)
print(cal.div())   # 0: 나누는 숫자가 0이므로 예외 처리하여 0이 나온다
```

## 클래스 변수

클래스 안에 변수를 선언하면 클래스 변수가 된다. 객체변수와 달리 **클래스로 만든 모든 객체가 공유**한다. `클래스_이름.클래스변수` 또는 `객체.클래스변수`로 접근한다.

```python
class Family:
    lastname = "양"

print(Family.lastname)   # 양

a = Family()
b = Family()
print(a.lastname)   # 양
print(b.lastname)   # 양

Family.lastname = "박"   # 클래스 변수를 바꾸면 모든 객체에 반영된다
print(a.lastname)   # 박
print(b.lastname)   # 박
```

- **동일한 이름의 객체변수를 만들면** — 클래스 변수가 바뀌는 것이 아니라, 그 객체에 같은 이름의 객체변수가 새로 생긴다.

  ```python
  a.lastname = "김"        # 클래스 변수 변경이 아니라 인스턴스 변수 할당
  print(a.lastname)        # 김
  print(b.lastname)        # 박
  print(Family.lastname)   # 박
  ```

> 클래스 변수를 가장 마지막에 다루는 이유는 실무에서 클래스 변수보다 객체변수를 쓰는 비율이 훨씬 높기 때문이다.
