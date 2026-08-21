# 예외 처리(exception)

> 예제 코드: [Source/advanced/handle_exception.py](Source/advanced/handle_exception.py)

- [오류는 언제 발생하는가](#오류는-언제-발생하는가)
- [try-except 문](#try-except-문)
- [try-finally 문](#try-finally-문)
- [여러 개의 오류 처리하기](#여러-개의-오류-처리하기)
- [try-else 문](#try-else-문)
- [오류 회피하기](#오류-회피하기)
- [오류 일부러 발생시키기](#오류-일부러-발생시키기)
- [예외 만들기](#예외-만들기)

## 오류는 언제 발생하는가

오류가 발생하는 이유는 프로그램이 잘못 동작하는 것을 막기 위한 파이썬의 배려이다. 오타로 인한 구문 오류가 아니라, 실제 프로그램에서 자주 만나는 오류들을 먼저 살펴보자.

- **존재하지 않는 파일 열기** — `FileNotFoundError`가 발생한다.

  ```python
  f = open("없는파일", 'r')
  # Traceback (most recent call last):
  #   File "handle_exception.py", line 4, in <module>
  #     f = open("없는파일", 'r')
  # FileNotFoundError: [Errno 2] No such file or directory: '없는파일'
  ```

- **0으로 나누기** — `ZeroDivisionError`가 발생한다.

  ```python
  4 / 0
  # Traceback (most recent call last):
  #   File "handle_exception.py", line 14, in <module>
  #     4 / 0
  # ZeroDivisionError: division by zero
  ```

- **인덱스 범위를 벗어난 접근** — `a[3]`은 네 번째 요솟값을 가리키는데 `a`에는 값이 3개뿐이므로 `IndexError`가 발생한다.

  ```python
  a = [1, 2, 3]
  a[3]
  # Traceback (most recent call last):
  #   File "handle_exception.py", line 24, in <module>
  #     a[3]
  # IndexError: list index out of range
  ```

파이썬은 이런 오류가 발생하면 프로그램을 중단하고 오류 메시지를 보여 준다.

## try-except 문

`try` 블록 수행 중 오류가 발생하면 `except` 블록이 수행된다. 오류가 발생하지 않으면 `except` 블록은 수행되지 않는다.

```python
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
```

> `[]`는 괄호 안의 내용을 생략할 수 있다는 관례적 표기법이다. 리스트를 뜻하는 대괄호가 아니라 "이 부분은 써도 되고 안 써도 된다"는 의미이다.

따라서 `except` 구문은 다음 3가지 방법으로 쓸 수 있다.

- **try-except만 쓰는 방법** — 오류의 종류에 상관없이 오류가 발생하면 `except` 블록을 수행한다.

  ```python
  try:
      ...
  except:
      ...
  ```

- **발생 오류만 포함한 except 문** — 지정한 오류와 동일한 오류일 경우에만 `except` 블록을 수행한다.

  ```python
  try:
      ...
  except 발생오류:
      ...
  ```

- **발생 오류와 오류 변수까지 포함한 except 문** — 오류의 내용까지 알고 싶을 때 사용한다.

  ```python
  try:
      ...
  except 발생오류 as 오류변수:
      ...
  ```

4를 0으로 나누면 `ZeroDivisionError`가 발생하여 `except` 블록이 실행되고, 오류 변수 `e`에 담긴 오류 메시지를 출력할 수 있다.

```python
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)   # division by zero
```

## try-finally 문

`finally` 절은 `try` 문 수행 도중 예외 발생 여부에 상관없이 **항상 수행된다**. 보통 사용한 리소스를 close해야 할 때 많이 사용한다.

```python
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.
finally:
    f.close()   # 중간에 오류가 발생하더라도 무조건 실행된다.
```

`finally` 절이 실제로 어떻게 동작하는지 구체적인 예로 확인해 보자.

```python
try:
    print("나누기 전")
    4 / 0
    print("나누기 후")
except ZeroDivisionError:
    print("오류가 발생했습니다.")
finally:
    print("finally 실행!")
# 나누기 전
# 오류가 발생했습니다.
# finally 실행!
```

`4 / 0`에서 오류가 발생해 `print("나누기 후")`는 건너뛰었지만 `finally` 절은 실행되었다. 오류가 발생하지 않더라도 `finally` 절은 항상 실행된다.

## 여러 개의 오류 처리하기

`except` 절을 여러 개 나열하면 오류 종류별로 다르게 처리할 수 있다.

```python
try:
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
```

```python
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
# 인덱싱 할 수 없습니다.
```

`a`는 요솟값이 2개이므로 `a[3]`에서 `IndexError`가 먼저 발생한다. 이 시점에 `try` 블록을 빠져나오므로 `4 / 0`은 실행되지 않고 `ZeroDivisionError`도 발생하지 않는다.

- **오류 메시지 확인하기** — `as`로 오류 변수를 받으면 된다.

  ```python
  try:
      a = [1, 2]
      print(a[3])
      4/0
  except ZeroDivisionError as e:
      print(e)
  except IndexError as e:
      print(e)
  # list index out of range
  ```

- **여러 오류를 함께 처리하기** — 2개 이상의 오류를 동일하게 처리하려면 괄호로 묶는다.

  ```python
  try:
      a = [1, 2]
      print(a[3])
      4/0
  except (ZeroDivisionError, IndexError) as e:
      print(e)
  # list index out of range
  ```

## try-else 문

`try` 문 수행 중 오류가 발생하면 `except` 절이, 오류가 발생하지 않으면 `else` 절이 수행된다.

```python
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else:   # 오류가 없을 경우에만 수행
    ...
```

```python
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
# 나이를 입력하세요: 30
# 환영합니다.

# 나이를 입력하세요: ㅁㅁ
# 입력이 정확하지 않습니다.

# 나이를 입력하세요: 10
# 미성년자는 출입금지입니다.
```

> "그냥 `try` 블록 안에 넣으면 되지 않나?"라고 생각할 수 있다. 하지만 `else` 절에 넣은 코드는 `except`의 대상이 되지 않는다. 덕분에 `try` 블록에서 발생할 수 있는 오류만 정확히 잡고, 나머지 코드에서 발생하는 의도치 않은 오류가 `except`에 잡히는 것을 막을 수 있다.

## 오류 회피하기

특정 오류가 발생해도 그냥 통과시켜야 할 때가 있다. 여러 파일을 처리하는 중 일부 파일이 없더라도 프로그램을 계속 실행하고 싶은 경우가 그렇다.

```python
students = ["김철수", "이영희", "박민수", "최유진"]
for student in students:
    try:
        with open(f"{student}_성적.txt", 'r') as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue   # 다음 학생으로 넘어감
# 김철수의 성적 파일이 없습니다. 건너뜁니다.
# 이영희의 성적 파일이 없습니다. 건너뜁니다.
# 박민수의 성적 파일이 없습니다. 건너뜁니다.
# 최유진의 성적 파일이 없습니다. 건너뜁니다.
```

오류를 완전히 무시하고 싶을 때는 `pass`를 사용한다.

```python
try:
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass   # 설정 파일이 없어도 계속 진행

# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")
# 프로그램이 정상적으로 실행됩니다.
```

> `pass`는 신중하게 사용해야 한다. 중요한 오류까지 무시하면 나중에 더 큰 문제가 될 수 있다.

## 오류 일부러 발생시키기

파이썬은 `raise` 문으로 오류를 강제로 발생시킬 수 있다. 잘못된 인수가 들어왔을 때 그 자리에서 알리거나, 처리할 수 없는 상태를 호출한 쪽에 넘기는 등 "여기서 더 진행하면 안 된다"는 사실을 드러내야 할 때 두루 쓴다.

그중 한 가지 예로, 여러 명이 함께 작업할 때 자식 클래스가 반드시 구현해야 할 기능을 빠뜨리는 실수를 막는 데 쓸 수 있다. `Bird` 클래스를 상속받는 자식 클래스가 반드시 `fly` 메서드를 구현하도록 강제해 보자.

```python
class Bird:
    def fly(self):
        raise NotImplementedError   # 파이썬에 이미 정의되어 있는 오류다

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
# Traceback (most recent call last):
#   File "handle_exception.py", line 191, in <module>
#     eagle.fly()
#   File "handle_exception.py", line 186, in fly
#     raise NotImplementedError
# NotImplementedError
```

`Eagle`은 `fly`를 오버라이딩하지 않았으므로 부모인 `Bird`의 `fly`가 수행되어 `NotImplementedError`가 발생한다. 오류가 나지 않게 하려면 `fly`를 직접 구현해야 한다.

```python
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()   # very fast
```

> `NotImplementedError`는 꼭 작성해야 하는 부분이 구현되지 않았을 때 일부러 오류를 발생시키기 위해 파이썬이 미리 만들어 둔 오류다. 상속받는 클래스에서 메서드를 다시 구현하는 것은 [메서드 오버라이딩](Class.md#메서드-오버라이딩)이다.

## 예외 만들기

특수한 경우에만 예외 처리를 하려고 예외를 직접 만들어 쓰기도 한다. 예외는 파이썬 내장 클래스인 `Exception`을 상속하여 만든다.

```python
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보': raise MyError()
    print(nick)

try:
    say_nick('천사')   # 천사
    say_nick('바보')   # MyError 발생
except MyError as e:
    print(e)          # 아무것도 출력되지 않는다
# 천사
```

`say_nick('바보')`에서 `MyError`가 발생해 `except` 블록이 실행되지만, 별도의 오류 메시지를 정의하지 않았으므로 `print(e)`는 빈 문자열을 출력한다.

오류 메시지가 보이게 하려면 `__str__` 메서드를 구현해야 한다. `__str__`은 `print(e)`처럼 오류 메시지를 `print` 문으로 출력할 때 호출되는 메서드이다.

```python
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick('천사')   # 천사
    say_nick('바보')   # MyError 발생
except MyError as e:
    print(e)
# 천사
# 허용되지 않는 별명입니다.
```

> 오류 메시지가 필요 없다면 `except MyError:`로 받아 원하는 문장을 직접 출력해도 된다.
>
> ```python
> try:
>     say_nick('천사')
>     say_nick('바보')
> except MyError:
>     print("허용되지 않는 별명입니다.")
> ```
