# 표준 라이브러리(standard library)

> 예제 코드: [Source/advanced/standard_library.py](Source/advanced/standard_library.py)

- [표준 라이브러리란](#표준-라이브러리란)
- [datetime.date](#datetimedate)
- [time](#time)
- [math](#math)
- [random](#random)
- [itertools](#itertools)
- [functools.reduce](#functoolsreduce)
- [operator.itemgetter](#operatoritemgetter)
- [shutil](#shutil)
- [glob](#glob)
- [pickle](#pickle)
- [os](#os)
- [zipfile](#zipfile)
- [threading](#threading)
- [tempfile](#tempfile)
- [traceback](#traceback)
- [json](#json)
- [urllib](#urllib)
- [webbrowser](#webbrowser)

## 표준 라이브러리란

파이썬 표준 라이브러리는 파이썬을 설치할 때 자동으로 함께 설치되는 모듈 모음이다. 전 세계 파이썬 고수들이 만든 검증된 코드이므로, 필요한 기능을 직접 만들기 전에 표준 라이브러리에 이미 있는지부터 확인하는 것이 좋다.

모든 라이브러리를 다 알 필요는 없다. **어떤 일을 할 때 어떤 라이브러리를 쓰면 되는지** 정도만 알아 두고, 필요할 때 찾아 쓰면 된다.

> `sys` 모듈은 [프로그램의 입출력(sys.argv)](../Chapter4/ProgramIO.md)에서, `re` 모듈은 정규 표현식에서 따로 다룬다.

## datetime.date

`datetime.date`는 연, 월, 일로 날짜를 표현할 때 사용한다. 날짜 객체끼리 빼면 두 날짜의 차이를, `weekday()`로는 요일을 구할 수 있다.

```python
import datetime

day1 = datetime.date(2026, 8, 5)
day2 = datetime.date(1992, 9, 29)
```

- **날짜 차이** — 날짜 객체끼리 빼면 `datetime.timedelta` 객체가 반환된다. `days` 속성으로 며칠 차이인지 확인한다.

  ```python
  diff = day1 - day2
  print(type(diff))   # <class 'datetime.timedelta'>
  print(diff.days)    # 12363
  ```

- **요일 뽑기** — `weekday()`는 월요일이 0, 일요일이 6이다. 월요일을 1, 일요일을 7로 두려면 `isoweekday()`를 쓴다.

  ```python
  day = datetime.date(2026, 8, 5)
  print(day.weekday())      # 2(수): 0(월) ~ 6(일)
  print(day.isoweekday())   # 3(수): 1(월) ~ 7(일)
  ```

## time

시간과 관련된 `time` 모듈에는 함수가 매우 많다. 그중 자주 쓰는 것만 살펴본다.

- **`time.time`** — 1970년 1월 1일 0시 0분 0초(UTC)를 기준으로 지난 시간을 초 단위 실수로 반환한다.

  ```python
  import time

  now = time.time()
  print(now)   # 1785935404.674016
  ```

- **`time.localtime`** — `time.time()`이 반환한 실숫값을 연, 월, 일, 시, 분, 초 형태로 바꿔 준다. UTC가 아니라 현지 시간 기준으로 변환된다.

  ```python
  localtime = time.localtime(now)
  print(localtime)
  # time.struct_time(tm_year=2026, tm_mon=8, tm_mday=5, tm_hour=22, tm_min=12, tm_sec=20, tm_wday=2, tm_yday=217, tm_isdst=0)
  print(time.localtime())   # 인수가 없으면 현재 시간으로 생성
  ```

- **`time.asctime`** — `time.localtime`이 반환한 튜플 형태의 값을 인수로 받아 알아보기 쉬운 형태로 반환한다.

  ```python
  asctime = time.asctime(localtime)
  print(asctime)          # Wed Aug  5 22:32:32 2026
  print(time.asctime())   # 인수가 없으면 현재 시간으로 생성
  ```

- **`time.ctime`** — 현재 시간의 `asctime`을 바로 뽑아온다. `asctime`과 달리 **항상 현재 시간만** 반환한다.

  ```python
  ctime = time.ctime()
  print(ctime)   # Wed Aug  5 22:34:10 2026
  ```

- **`time.strftime`** — `struct_time`을 받아 포맷 코드에 맞춘 문자열을 반환한다.

  ```python
  print(time.strftime('%x', localtime))   # 08/05/26
  print(time.strftime('%c', localtime))   # Wed Aug  5 22:39:17 2026
  print(time.strftime('%c'))              # 시간 인수가 없으면 현재 시간으로 생성
  ```

  주요 포맷 코드는 다음과 같다.

  | 포맷 코드 | 설명 | 예 |
  | --- | --- | --- |
  | `%a` / `%A` | 요일의 줄임말 / 요일 | Mon / Monday |
  | `%b` / `%B` | 달의 줄임말 / 달 | Jan / January |
  | `%c` | 날짜와 시간 | Thu May 25 10:13:52 2023 |
  | `%d` | 일(day) | [01, 31] |
  | `%H` / `%I` | 시간(24시간 / 12시간) | [00, 23] / [01, 12] |
  | `%j` | 1년 중 누적 날짜 | [001, 366] |
  | `%m` | 달 | [01, 12] |
  | `%M` / `%S` | 분 / 초 | [00, 59] |
  | `%p` | AM / PM | AM |
  | `%U` / `%W` | 1년 중 누적 주(일요일 / 월요일 시작) | [00, 53] |
  | `%w` | 숫자로 된 요일 | [0(일), 6(토)] |
  | `%x` / `%X` | 지역 기반 날짜 / 시간 | 05/25/23 / 17:22:21 |
  | `%Y` / `%y` | 연도 / 세기를 제외한 연도 | 2023 / 01 |
  | `%Z` | 시간대 | 대한민국 표준시 |
  | `%%` | 문자 `%` | % |

- **`time.sleep`** — 넣은 시간만큼 멈춘다. 인수는 실수도 되므로 `0.5`면 0.5초다. 주로 루프 안에서 일정한 간격을 둘 때 쓴다.

  ```python
  start = time.time()   # 시작 시간
  time.sleep(1)         # 1초 대기
  end = time.time()     # 종료 시간
  print(end - start)    # 1.005047082901001: 정확히 1초는 아니지만 거의 1초 차이
  ```

> `time.localtime`, `time.asctime`, `time.strftime`은 입력 인수 없이 사용할 수 있다. 이때는 현재 시각을 기준으로 수행된다.

## math

`math`는 수학과 관련된 함수를 모아 놓은 모듈이다. 여기서는 최대 공약수와 최소 공배수를 구하는 함수를 본다.

- **`math.gcd`** — 최대 공약수(greatest common divisor)를 구한다. 예를 들어 사탕 60개, 초콜릿 100개, 젤리 80개를 남김없이 똑같이 나눠 담을 수 있는 최대 봉지 수가 곧 세 수의 최대 공약수다.

  ```python
  import math

  gcd = math.gcd(60, 100, 80)
  print(gcd)   # 20
  ```

  > `math.gcd`는 파이썬 3.5 버전부터 사용할 수 있다. 3.9 버전부터는 인수를 여러 개 넣을 수 있지만 그 미만에서는 2개까지만 허용된다.

- **`math.lcm`** — 최소 공배수(least common multiple)를 구한다. 15분마다 오는 시내버스와 25분마다 오는 마을버스가 다시 동시에 도착하는 시각은 두 수의 최소 공배수인 75분 후다.

  ```python
  lcm = math.lcm(15, 25)
  print(lcm)   # 75
  ```

  > `math.lcm`은 파이썬 3.9 버전부터 사용할 수 있다.

## random

`random`은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.

```python
import random

print(random.random())        # 0.1601055394682327: 0 ~ 1 사이의 실수 중 난수
print(random.randint(1, 10))  # 8: 1 ~ 10 사이의 정수 중 난수
print(random.randint(1, 55))  # 25: 1 ~ 55 사이의 정수 중 난수
```

- **리스트에서 무작위로 꺼내기** — `randint`로 인덱스를 뽑아 `pop`하면 리스트에서 무작위로 하나를 꺼내 반환하는 함수를 만들 수 있다. 꺼낸 요소는 `pop`에 의해 리스트에서 사라진다.

  ```python
  def random_pop(data):
      # 0 ~ data의 마지막 인덱스 사이의 랜덤
      number = random.randint(0, len(data) - 1)
      return data.pop(number)

  data = [1, 2, 3, 4, 5]
  while data:
      print(random_pop(data))
  # 5
  # 4
  # 2
  # 1
  # 3
  ```

- **`random.choice`** — 입력으로 받은 리스트에서 무작위로 하나를 선택해 반환한다.

  ```python
  data = [1, 2, 3, 4, 5]
  choice = random.choice(data)
  print(choice)   # 1
  ```

  > `random_pop`은 `choice`를 써서 더 직관적으로 만들 수도 있다. `number = random.choice(data)`로 하나 고르고 `data.remove(number)`로 지운 뒤 반환하면 된다.

- **`random.sample`** — 리스트에서 원하는 개수를 꺼내 리스트로 반환한다. 두 번째 인수에 `len(data)`를 넣으면 전체를 무작위로 섞은 결과가 된다.

  ```python
  data = [1, 2, 3, 4, 5]
  sample = random.sample(data, 3)
  print(sample)   # [4, 5, 3]
  ```

## itertools

`itertools`는 반복 가능한 객체를 다루는 함수를 모아 놓은 모듈이다.

- **`itertools.zip_longest(*iterables, fillvalue=None)`** — 내장 함수 `zip`과 똑같이 동작하지만, 길이가 다르면 **긴 객체의 길이에 맞춰** `fillvalue`에 설정한 값을 짧은 쪽에 채운다. `fillvalue`를 지정하지 않으면 `None`으로 채운다.

  ```python
  import itertools

  students = ['한민서', '황지민', '이영철', '이광수', '김승민']   # 5개
  snacks = ['사탕', '초콜릿', '젤리']                              # 3개
  result = itertools.zip_longest(students, snacks, fillvalue="새우깡")
  print(list(result))
  # [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
  # -> 모자란 이광수, 김승민은 fillvalue인 새우깡으로 채워졌다
  ```

  > 내장 `zip`으로 묶으면 더 짧은 `snacks`의 개수만큼인 3개만 묶인다.

- **`itertools.permutations(iterable, r)`** — 반복 가능 객체 중 `r`개를 선택한 **순열**을 이터레이터로 반환한다. 1, 2, 3이 적힌 카드 3장에서 2장을 꺼내 만들 수 있는 두 자리 숫자를 모두 구하는 문제다.

  ```python
  result = itertools.permutations(['1', '2', '3'], 2)
  print(list(result))
  # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
  ```

- **`itertools.combinations(iterable, r)`** — 반복 가능 객체 중 `r`개를 선택한 **조합**을 이터레이터로 반환한다. 1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수를 구하면 다음과 같다.

  ```python
  result = itertools.combinations(range(1, 46), 6)
  print(len(list(result)))   # 8145060
  ```

  > 순열은 순서를 따지고 조합은 따지지 않는다. 카드 3장에서 2장을 뽑을 때 순열은 6가지, 조합은 3가지다.

- **`itertools.combinations_with_replacement(iterable, r)`** — 같은 값을 여러 번 뽑을 수 있는 **중복 조합**을 반환한다. 로또에 중복이 허용된다면 경우의 수가 이만큼 늘어난다.

  ```python
  result = itertools.combinations_with_replacement(range(1, 46), 6)
  print(len(list(result)))   # 15890700
  ```

## functools.reduce

`functools.reduce(function, iterable)`은 함수를 반복 가능한 객체의 요소에 차례대로(왼쪽에서 오른쪽으로) 누적 적용하여 하나의 값으로 줄인다.

```python
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)   # 데이터의 모든 합을 구한다
print(result)   # 15
```

위 코드는 람다 함수를 요소에 차례대로 누적 적용하므로 `((((1+2)+3)+4)+5)`와 같이 계산된다.

- **최댓값 구하기** — 두 값 중 큰 값을 남기는 람다를 넘기면 최댓값이 구해진다.

  ```python
  num_list = [3, 2, 8, 1, 6, 7]
  max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
  print(max_num)   # 8
  ```

  > 최솟값은 `functools.reduce(lambda x, y: x if x < y else y, num_list)`로 구한다.

## operator.itemgetter

`operator.itemgetter`는 요소를 꺼내오는 함수를 만들어 주는 함수다. 주로 `sorted`의 `key` 매개변수에 넣어 다양한 기준으로 정렬할 때 쓴다.

- **리스트 요소가 튜플일 때** — `itemgetter(1)`은 튜플의 두 번째 요소, 즉 나이를 기준으로 정렬하겠다는 의미다.

  ```python
  from operator import itemgetter

  students = [
      ("jane", 22, 'A'),
      ("dave", 32, 'B'),
      ("sally", 17, 'B'),
  ]
  key = itemgetter(1)   # lambda x: x[1]과 같다고 볼 수 있다
  result = sorted(students, key=key)
  print(result)   # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

  result = sorted(students, key=lambda x: x[1])   # 따라서 람다를 넣어도 동일하게 동작한다
  print(result)   # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]
  ```

- **리스트 요소가 딕셔너리일 때** — 인덱스 대신 딕셔너리의 키를 넣는다.

  ```python
  students = [
      {"name": "jane", "age": 22, "grade": 'A'},
      {"name": "dave", "age": 32, "grade": 'B'},
      {"name": "sally", "age": 17, "grade": 'B'},
  ]
  result = sorted(students, key=itemgetter('age'))
  print(result)
  # [{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]
  ```

- **`operator.attrgetter`** — 리스트 요소가 튜플이나 딕셔너리가 아니라 클래스의 객체일 때 사용한다. `attrgetter('age')`는 객체의 `age` 속성으로 정렬하겠다는 의미다.

  ```python
  from operator import attrgetter
  
  class Student:
      def __init__(self, name, age, grade):
          self.name = name
          self.age = age
          self.grade = grade
  
  students = [
      Student('jane', 22, 'A'),
      Student('dave', 32, 'B'),
      Student('sally', 17, 'B'),
  ]
  sorted_students = sorted(students, key=attrgetter('age'))
  mapped = map(lambda student: (student.name, student.age, student.grade), sorted_students)   # 볼 수 있도록 튜플로 변환
  print(list(mapped))   # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]
  ```

## shutil

`shutil`은 파일을 복사하거나 이동할 때 사용하는 모듈이다. 작업 중인 파일을 자동으로 백업하는 기능 등을 만들 때 쓴다.

```python
import shutil
```

- **`shutil.copy(기존_경로, 복사할_경로)`** — 파일을 복사한다.

  ```python
  # temp/a.txt 파일을 temp/backup/a.txt.bak으로 복사
  shutil.copy("temp/a.txt", "temp/backup/a.txt.bak")
  ```

- **`shutil.move(기존_경로, 옮길_경로)`** — 파일을 옮긴다. 휴지통으로 보내는 것 같은 삭제 기능을 만들 때 응용할 수 있다.

  ```python
  # temp/a.txt 파일을 temp/backup/a.txt로 이동
  shutil.move("temp/a.txt", "temp/backup/a.txt")
  ```

> 두 함수 모두 대상 디렉터리가 **이미 있어야** 한다. 없으면 오류가 발생한다.

## glob

`glob`은 특정 디렉터리에 있는 파일 이름을 와일드카드 패턴으로 찾아 리스트로 반환하는 모듈이다.

- **패턴 문법**

  | 패턴 | 의미 | 예 |
  | --- | --- | --- |
  | `*` | 임의의 문자 0개 이상, 단 `/`는 넘지 않는다 | `*.py` |
  | `?` | 임의의 한 글자 | `mod?.py` → `mod1.py`, `mod2.py` |
  | `[seq]` | 괄호 안 문자 중 하나 | `mod[12].py` → `mod1.py`, `mod2.py` |
  | `[!seq]` | 괄호 안 문자가 아닌 것 하나 | `[!_]*.py` → `_`로 시작하지 않는 `.py` |
  | `**` | 하위 디렉터리 전체, `recursive=True`와 함께 써야 모든 깊이를 의미한다 | `Chapter*/Source/**/*.py` |

- **`glob(pathname)`** — 패턴에 맞는 파일 경로를 리스트로 반환한다.

  ```python
  import glob
  
  # Source 바로 아래의 .py만 반환, *는 /를 넘지 않으므로 하위 디렉터리는 포함되지 않는다
  paths = glob.glob("Chapter2/Source/*.py")
  print(paths)   # ['Chapter2/Source/bool.py', 'Chapter2/Source/dictionary.py', ...]
  
  # Source 하위 디렉터리의 .py 반환
  paths = glob.glob("Chapter2/Source/*.py")
  print(paths)
  # ['Chapter2/Source/tuple.py', 'Chapter2/Source/list.py', ...]
  
  # Source 아래 모든 깊이의 .py 반환
  paths = glob.glob("Chapter*/Source/**/*.py", recursive=True)
  print(paths)
  # ['Chapter2/Source/bool.py', 'Chapter5/Source/advanced/built_in_function.py', ...]
  ```

> 주의할 점 세 가지.
> - 정렬 순서는 보장되지 않는다. 필요하면 `sorted()`로 감싼다.
> - 숨김 파일(`.gitignore` 등)은 `*`에 걸리지 않는다. `.*`로 따로 찾아야 한다.
> - 중괄호 확장(`*.{py,md}`)은 셸 문법이라 지원하지 않는다. 두 번 호출해서 합쳐야 한다.

## pickle

`pickle`은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

```python
import pickle

path = "temp/test.txt"

# pickle.dump(데이터, 파일_객체): 데이터를 파일에 저장
with open(path, 'wb') as f:
    data = {1: 'python', 2: 'you need'}
    pickle.dump(data, f)

# pickle.load(파일_객체): 파일에서 불러오기
with open(path, 'rb') as f:
    data = pickle.load(f)
    print(data)   # {1: 'python', 2: 'you need'}
```

> `pickle`이 만드는 결과물 자체가 `bytes`이므로 저장은 `'wb'`, 로드는 `'rb'`로 열어야 한다. `'w'`로 열면 `TypeError`, `'r'`로 열면 `UnicodeDecodeError`가 난다.
>
> ```python
> pickle.dumps({"name": "jane"})
> # b'\x80\x04\x95\x17...}\x94\x8c\x04name\x94\x8c\x04jane\x94s.'
> ```

- **클래스 객체 저장하기** — 딕셔너리뿐 아니라 어떤 자료형이든 저장할 수 있고, 클래스의 객체도 된다.

  ```python
  with open(path, 'wb') as f:
      data = Student("yjc", 35, "A")
      pickle.dump(data, f)
  
  with open(path, 'rb') as f:
      data = pickle.load(f)
      print(data)         # <__main__.Student object at 0x104cbfa80>
      print(data.name)    # yjc
      print(data.age)     # 35
      print(data.grade)   # A
  ```

  단, **클래스 정의(코드)가 저장되는 것은 아니다.** 저장되는 것은 "모듈 이름 + 클래스 이름"이라는 이름표와 인스턴스의 속성값(`__dict__`)뿐이다. 실제 저장된 바이트를 `pickletools.dis()`로 열어 보면 다음 순서로 되어 있다.

  ```python
  # SHORT_BINUNICODE '__main__'   # 이 모듈에서
  # SHORT_BINUNICODE 'Student'    # 이 이름을 찾아라
  # STACK_GLOBAL                  # -> 실제 클래스 객체를 가져온다
  # NEWOBJ                        # __new__로 빈 인스턴스를 만든다(__init__은 호출되지 않는다)
  # SETITEMS / BUILD              # __dict__에 속성값을 채워 넣는다
  ```

  그래서 `load`하는 쪽에 같은 이름의 클래스 정의가 없으면 `AttributeError: module '__main__' has no attribute 'Student'` 오류가 난다. 위 예제가 잘 동작하는 이유는 저장과 로드가 같은 파일 안에서 이뤄져 `Student`가 이미 정의되어 있기 때문이다.

> 클래스를 pickle할 때 주의할 점.
> - `__init__`을 거치지 않으므로 생성자에서 하던 검증이나 초기화는 전부 건너뛴다.
> - 클래스 이름을 바꾸거나 다른 모듈로 옮기면 기존 pkl 파일은 읽을 수 없다. pickle할 클래스는 `__main__`이 아니라 별도 모듈(`models.py` 등)에 두는 것이 안전하다.
> - 나중에 속성을 추가해도 예전에 저장한 파일에는 그 속성이 없다(마이그레이션 개념이 없다).
> - 메서드는 저장되지 않으므로 복원된 객체는 현재 클래스 코드의 메서드를 따른다.
> - `pickle.load`는 파일에 적힌 이름대로 import하고 호출하므로, **신뢰할 수 없는 pkl 파일은 절대 열면 안 된다.**

## os

`os`는 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈이다.

- **`os.environ`** — 현재 시스템의 환경 변숫값을 반환한다. 딕셔너리 형태이므로 키로 원하는 값을 뽑을 수 있다.

  ```python
  import os

  environ = os.environ
  print(environ)          # environ({'COMMAND_MODE': 'unix2003', 'HOME': '/Users/yjc', 'LOGNAME': 'yjc', ...})
  print(environ['HOME'])  # /Users/yjc
  ```

- **`os.getcwd` / `os.chdir`** — 각각 현재 디렉터리 위치를 반환하고, 변경한다.

  ```python
  print(os.getcwd())   # /Users/yjc/Workspace/Python-dev-notes

  os.chdir("Source")
  print(os.getcwd())   # /Users/yjc/Workspace/Python-dev-notes/Source
  os.chdir("..")
  print(os.getcwd())   # /Users/yjc/Workspace/Python-dev-notes
  ```

- **`os.system` / `os.popen`** — `system`은 시스템 명령어를 호출하고, `popen`은 명령어를 호출한 뒤 결괏값을 읽기 모드의 파일 객체로 돌려받는다.

  ```python
  os.system("ls")   # 시스템 명령어 호출

  f = os.popen('ls')
  print(f.read())   # Bool.md                 Dictionary.md           Function.md...
  f.close()
  ```

- **파일과 디렉터리 다루기** — 그 밖에 자주 쓰는 함수는 다음과 같다.

  | 함수 | 설명 |
  | --- | --- |
  | `os.mkdir(디렉터리)` | 디렉터리를 생성한다 |
  | `os.rmdir(디렉터리)` | 디렉터리를 삭제한다. 단, 비어 있어야 삭제할 수 있다 |
  | `os.remove(파일)` | 파일을 지운다 |
  | `os.rename(src, dst)` | `src`라는 이름의 파일을 `dst`라는 이름으로 바꾼다 |

  ```python
  os.mkdir("temp/test")             # 디렉터리 생성
  os.rmdir("temp/test")             # 디렉터리 삭제
  os.remove("temp/test.txt")        # 파일 제거
  os.rename("temp/src", "temp/dst") # 파일 이름 변경
  ```

## zipfile

`zipfile`은 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈이다. `temp` 디렉터리에 `a.txt`, `b.txt`, `c.txt` 세 개의 파일이 있다고 가정한다.

```python
import zipfile
```

- **묶기와 해제** — `write()`로 개별 파일을 추가하고, `extractall()`로 전체를, `extract()`로 특정 파일만 해제한다.

  ```python
  # zip 파일 생성
  with zipfile.ZipFile('temp/abc.zip', 'w') as zip:
      zip.write('temp/a.txt')
      zip.write('temp/b.txt')
      zip.write('temp/c.txt')

  # zip 파일 전체 해제
  with zipfile.ZipFile('temp/abc.zip') as zip:
      zip.extractall()

  # zip 파일 일부 해제
  with zipfile.ZipFile('temp/abc.zip') as zip:
      zip.extract('temp/a.txt')
  ```

- **압축하여 묶기** — 그냥 묶는 것이 아니라 압축까지 하려면 `compression`, `compresslevel` 옵션을 사용한다.

  ```python
  with zipfile.ZipFile('temp/abc_compressed.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as zip:
      zip.write('temp/a.txt')
      zip.write('temp/b.txt')
      zip.write('temp/c.txt')
  ```

  `compresslevel`은 압축 수준으로 1~9를 사용한다. 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도가 가장 느리지만 압축률이 높다. 

  `compression`에는 4가지 종류가 있다.
  
  | 종류 | 설명 |
  | --- | --- |
  | `ZIP_STORED` | 압축하지 않고 zip으로만 묶는다. 속도가 빠르다 |
  | `ZIP_DEFLATED` | 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성이 좋다) |
  | `ZIP_BZIP2` | bzip2 압축으로 압축률이 높고 속도가 느리다 |
  | `ZIP_LZMA` | lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다) |

## threading

컴퓨터에서 동작하고 있는 프로그램을 프로세스(process)라고 한다. 보통 1개의 프로세스는 1가지 일만 하지만, 스레드(thread)를 사용하면 한 프로세스 안에서 2가지 이상의 일을 동시에 수행할 수 있다.

5초가 걸리는 함수를 5회 실행하는 상황을 생각해 보자.

```python
import threading

def long_task(num):   # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)
        print(f"working:{num}-{i}\n")
```

- **직렬 실행** — 그냥 반복문으로 5회 호출하면 5초짜리 작업이 5번 반복되므로 총 25초가 걸린다.

  ```python
  print('Start')
  for i in range(5):
      long_task(i)
  print('End')
  # 실행 결과: 총 25초 소요, 0-0 ~ 4-4까지 순서대로 실행
  # Start
  # working:0-0
  # working:0-1
  # working:0-2
  # ...
  # End
  ```

- **스레드 사용** — `threading.Thread`로 스레드를 만들고 `start()`로 실행하면 5개 작업이 동시에 수행되어 약 5초 만에 끝난다. 다만 실행 순서는 보장되지 않고, `Start`와 `End`가 먼저 출력된다.

  ```python
  print("Start")
  threads = []
  for i in range(5):
      t = threading.Thread(target=long_task, args=(i,))   # 스레드 생성
      threads.append(t)
  for t in threads:
      t.start()   # 스레드 실행
  print("End")
  # 실행 결과: 약 5초 소요, Start, End가 먼저 호출되고 long_task들이 실행된다
  # Start
  # End
  # working:1-0
  # working:0-0
  # working:2-0
  # ...
  ```

- **join으로 대기하기** — `t.join()`은 **`t`가 끝날 때까지 이를 호출한 스레드를 멈춰 세운다.** 스레드가 끝난 뒤에 다음 작업을 이어가야 할 때 쓴다. 아래 예제에서는 메인 스레드가 호출했으므로 메인 스레드가 대기한다.

  ```python
  print("Start")
  threads = []
  for i in range(5):
      t = threading.Thread(target=long_task, args=(i,))
      threads.append(t)
  for t in threads:
      t.start()
  for t in threads:
      t.join()   # join으로 스레드 종료까지 대기
  print("End")
  # 실행 결과: 약 5초 소요, 실행 순서는 보장되지 않는다
  # Start
  # working:1-0
  # working:2-0
  # working:0-0
  # ...
  # End
  ```

  > `join()`이 바꾸는 것은 **호출한 스레드가 어디까지 기다리느냐**이지 총 실행 시간이 아니다. 5개 스레드는 어느 쪽이든 동시에 돌아 약 5초에 끝난다. `join()`이 있으면 호출한 스레드가 그 자리에 멈춰 5개가 모두 끝나기를 기다리므로 `End`가 작업 뒤에 출력되고, 없으면 곧장 다음 줄로 넘어가므로 `End`가 먼저 출력된다.
  >
  > 기본값 `daemon = False`에서는 `join()`이 없어도 인터프리터가 살아 있는 스레드를 기다렸다가 종료하므로 작업 자체는 끝까지 수행된다. 하지만 스레드의 결과를 받아 다음 코드에서 써야 한다면, 그 전에 `join()`으로 종료를 기다려야 한다.

- **Thread에 함수와 인수 넘기기** — `threading.Thread(target=함수, args=(인수,), kwargs={"이름": 값})` 형태로 쓴다. `target`에는 함수를 호출한 **결과가 아니라 함수 자체(함수 객체)** 를 넘긴다.

  ```python
  # target=long_task     -> 함수 객체를 넘긴다(올바름)
  # target=long_task()   -> 지금 당장 실행되고 반환값(None)이 target에 들어간다(잘못됨)
  # args=(3,)            -> long_task(3)
  # kwargs={"num": 3}    -> long_task(num=3)
  ```

  `Thread` 객체는 만들어 두기만 하고, 실제 호출은 `t.start()`를 부를 때 별도 스레드에서 일어난다. 함수에 넘길 인수는 `target`에 같이 쓸 수 없고 `args`나 `kwargs`로 따로 전달한다.

  > 요소가 하나인 튜플은 `args=(i,)`처럼 뒤에 쉼표가 필요하다. `(i)`는 튜플이 아니라 그냥 정수이며, 쉼표를 빠뜨리면 `TypeError: 'int' object is not iterable`이 발생한다.

- **lambda로 넘길 때의 함정** — `lambda` 안의 `i`는 정의 시점이 아니라 **실행 시점**에 값을 읽는다. 스레드는 반복문이 끝난 뒤에 시작되므로 5개 스레드가 모두 마지막 값인 4를 쓰게 된다.

  ```python
  t = threading.Thread(target=lambda: long_task(i))        # 전부 i가 4가 된다
  t = threading.Thread(target=lambda i=i: long_task(i))    # 기본값은 정의 시점에 평가되므로 값이 붙잡힌다
  ```

  인수가 복잡하면 `functools.partial(long_task, i)`를 넘겨도 된다. 그냥 `args=(i,)`를 쓰는 것이 가장 안전하고 읽기도 좋다.

- **데몬 스레드** — 기본값은 `daemon = False`이며, 이 경우 메인 스레드가 마지막 줄에 도달해도 인터프리터가 바로 끝나지 않고 살아 있는 스레드를 모두 기다린 뒤 종료한다. `t.daemon = True`로 두면 메인 스레드가 끝나는 순간 스레드가 강제로 잘리며 프로그램이 즉시 종료된다. 작업이 중간에 끊겨도 되는 백그라운드 감시용 스레드나 무한 루프 스레드에 사용한다.

## tempfile

`tempfile`은 임시 파일을 만들어 사용할 때 유용한 모듈이다.

- **`tempfile.mkstemp`** — 중복되지 않는 임시 파일을 만들고 `(파일 디스크립터, 파일 경로)` 형태의 튜플로 반환한다.

  ```python
  import tempfile

  fd, path = tempfile.mkstemp()
  print(path)   # /var/folders/8n/529r5bmd4yq54qfq6pdqy6fh0000gn/T/tmpzb9rofk8
  ```

- **`tempfile.TemporaryFile`** — 임시 저장 공간으로 사용할 파일 객체를 반환한다. 이 파일은 기본적으로 바이너리 쓰기 모드(`wb`)를 가지며, `close()`가 호출되면 자동으로 삭제된다.

  ```python
  f = tempfile.TemporaryFile()
  f.close()
  ```

## traceback

`traceback`은 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈이다. `format_exc()`는 오류 추적 결과를 문자열로 반환한다.

```python
import traceback

def a():
    return 1/0
def b():
    a()
def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())
main()
# 오류가 발생했습니다.
# Traceback (most recent call last):
#   File ".../Chapter5/Source/advanced/standard_library.py", line 448, in main
#     b()
#     ~^^
#   File ".../Chapter5/Source/advanced/standard_library.py", line 445, in b
#     a()
#     ~^^
#   File ".../Chapter5/Source/advanced/standard_library.py", line 443, in a
#     return 1/0
#            ~^~
# ZeroDivisionError: division by zero
```

> `except`에서 `print("오류가 발생했습니다.")`만 하면 어디서 왜 났는지 알 수 없다. `traceback`을 붙이면 `main` → `b` → `a` 순으로 호출되다가 `1 / 0`에서 `ZeroDivisionError`가 발생했다는 것을 정확히 확인할 수 있다. 예외 처리 자체는 [예외 처리(exception)](HandleException.md)를 참고한다.

## json

`json`은 JSON 데이터를 쉽게 처리하고자 사용하는 모듈이다. 파일을 다루는 `dump`/`load`와 문자열을 다루는 `dumps`/`loads`가 짝을 이룬다.

- **`json.dump` / `json.load`** — 파이썬 자료형을 JSON으로 변환해 파일에 쓰고, 파일을 읽어 딕셔너리로 반환한다.

  ```python
  import json

  data = {"name":"홍길동", "birth":"0525", "age": 30}
  with open('temp/info.json', 'w') as f:
      json.dump(data, f)

  with open('temp/info.json') as f:
      data = json.load(f)
  print(type(data))   # <class 'dict'>
  print(data)         # {'name': '홍길동', 'birth': '0525', 'age': 30}
  ```

- **`json.dumps`** — 파이썬 자료형을 JSON 문자열로 변환한다. 기본적으로 아스키 형태로 저장하므로 한글이 코드처럼 보인다.

  ```python
  data = {"name":"홍길동", "birth":"0525", "age": 30}
  json_data = json.dumps(data)
  print(json_data)   # {"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30}: 한글이 코드로 보인다

  # ensure_ascii=False: 데이터를 아스키 형태로 변환하지 않겠다는 뜻
  json_data2 = json.dumps(data, ensure_ascii=False)
  print(json_data2)  # {"name": "홍길동", "birth": "0525", "age": 30}

  # indent로 보기 좋게 정렬
  json_data3 = json.dumps(data, indent=2, ensure_ascii=False)
  print(json_data3)
  # {
  #   "name": "홍길동",
  #   "birth": "0525",
  #   "age": 30
  # }
  ```

  딕셔너리 외에 리스트나 튜플 같은 자료형도 JSON으로 변환할 수 있다.

  ```python
  print(json.dumps([1,2,3]))   # [1, 2, 3]
  print(json.dumps((4,5,6)))   # [4, 5, 6]
  ```

- **`json.loads`** — JSON 문자열을 딕셔너리로 변환한다. 한글이 아스키로 저장되어 있어도 되돌리는 데는 문제가 없다.

  ```python
  result = json.loads(json_data)
  print(result)   # {'name': '홍길동', 'birth': '0525', 'age': 30}
  ```

## urllib

`urllib`은 URL을 읽고 분석할 때 사용하는 모듈이다. `urllib.request.urlopen(url)`로 리소스를 읽어 파일로 저장할 수 있다.

```python
import urllib.request
import gzip

def get_page(url, filename):
    with urllib.request.urlopen(url) as s:   # 해당 URL에 접근해서 내용 다운로드
        data = s.read()                      # bytes를 반환한다
        # 일부 사이트는 요청하지 않아도 gzip으로 압축해서 응답한다(www.python.org 등).
        # urllib은 압축을 자동으로 풀어주지 않으므로 그대로 저장하면 사람이 읽을 수 없는 파일이 된다.
        # 응답 헤더의 Content-Encoding을 확인해서 gzip이면 직접 풀어준다.
        if s.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(data)     # 압축을 풀어 원래 bytes로 되돌린다
    with open('temp/%s' % filename, 'wb') as f:   # 다운로드한 내용을 파일에 저장
        f.write(data)                             # data는 bytes이므로 파일도 'wb'로 열어야 한다

get_page('https://www.python.org/', 'python_org.html')
```

- **`urllib.request.Request(url, data=None, headers={}, method=None)`** — `urlopen`에 URL 문자열을 바로 넣으면 요청 헤더를 지정할 수 없다. 헤더를 붙이려면 `Request` 객체를 만들어 `urlopen`에 넘긴다.

  ```python
  def get_page_with_request(url, filename, headers):
      request = urllib.request.Request(url, headers=headers)   # 요청 정보를 담은 객체를 만든다
      with urllib.request.urlopen(request) as s:               # 문자열 대신 Request 객체를 넘긴다
          data = s.read()
          if s.headers.get('Content-Encoding') == 'gzip':
              data = gzip.decompress(data)
      with open('temp/%s' % filename, 'wb') as f:
          f.write(data)

  # User-Agent를 지정해서 브라우저인 척한다. 지정하지 않으면 Python-urllib/3.x로 요청된다.
  headers = {'User-Agent': 'Mozilla/5.0'}
  get_page_with_request('https://www.python.org/', 'python_org_ua.html', headers)
  ```

- **Request 객체에 담긴 요청 정보 확인하기**

  ```python
  request = urllib.request.Request('https://www.python.org/', headers=headers)
  print(request.full_url)                    # https://www.python.org/
  print(request.headers)                     # {'User-agent': 'Mozilla/5.0'} -> 키의 첫 글자만 대문자로 정규화된다
  print(request.get_header('User-agent'))    # Mozilla/5.0
  print(request.get_method())                # GET -> data를 넘기면 POST가 된다
  ```

> macOS에서는 `urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]>` 오류가 발생할 수 있다. 로컬 CA 인증서를 제대로 설치하는 것이 정석이며, `ssl._create_unverified_context()`로 검증을 끄는 방법은 보안상 위험하므로 실제 서비스 코드에서는 쓰지 않는다.

## webbrowser

`webbrowser`는 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용하는 모듈이다.

```python
import webbrowser

webbrowser.open_new('http://python.org')   # 새 창으로 열기
webbrowser.open('http://python.org')       # 이미 열려 있는 브라우저로 열기
```
