# 내장 함수(built-in function)

> 예제 코드: [Source/advanced/built_in_function.py](Source/advanced/built_in_function.py)

- [내장 함수란](#내장-함수란)
- [abs](#abs)
- [all](#all)
- [any](#any)
- [chr](#chr)
- [dir](#dir)
- [divmod](#divmod)
- [enumerate](#enumerate)
- [eval](#eval)
- [filter](#filter)
- [hex](#hex)
- [id](#id)
- [input](#input)
- [int](#int)
- [isinstance](#isinstance)
- [len](#len)
- [list](#list)
- [map](#map)
- [max](#max)
- [min](#min)
- [oct](#oct)
- [open](#open)
- [ord](#ord)
- [pow](#pow)
- [range](#range)
- [round](#round)
- [sorted](#sorted)
- [str](#str)
- [sum](#sum)
- [tuple](#tuple)
- [type](#type)
- [zip](#zip)

## 내장 함수란

내장 함수는 파이썬에 이미 만들어져 있는 함수로, 모듈과 달리 `import`가 필요 없어 아무 설정 없이 바로 쓸 수 있다. 이미 배운 `print`, `type`도 내장 함수다. 여기서는 활용 빈도가 높은 함수를 알파벳 순서로 정리한다.

> 새로운 프로그램을 만들기 전에 이미 만들어져 있는지부터 살펴보자. 이미 만들어진 것은 수많은 테스트를 거쳐 검증되어 있다. "이미 있는 것을 다시 만드느라 시간을 낭비하지 말라."

아래 예제의 `#` 주석은 각 식의 결괏값이다.

## abs

`abs(x)`는 숫자를 입력받아 그 숫자의 절댓값을 반환한다.

```python
abs(3)      # 3
abs(-3)     # 3
abs(-1.2)   # 1.2
```

## all

`all(x)`는 반복 가능한 데이터 `x`를 입력받아 요소가 모두 참이면 `True`, 거짓이 하나라도 있으면 `False`를 반환한다.

```python
all([1, 2, 3])      # True
all([1, 2, 3, 0])   # False: 0이 거짓
all([])             # True: 입력 인수가 빈 값인 경우 True
```

> 반복 가능한 데이터란 `for` 문에서 사용할 수 있는 자료형을 말한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다. 자료형의 참과 거짓은 [불(Bool)](Bool.md)을 참고한다.

## any

`any(x)`는 반복 가능한 데이터 `x`를 입력받아 요소 중 하나라도 참이 있으면 `True`, 모두 거짓일 때만 `False`를 반환한다. `all(x)`의 반대로 작동한다.

```python
any([1, 2, 3, 0])   # True: 0만 거짓
any([0, ""])        # False: 모두 거짓이다
any([])             # False: 입력 인수가 빈 값인 경우 False
```

## chr

`chr(i)`는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환한다.

```python
chr(97)      # 'a'
chr(44032)   # '가'
```

> 유니코드는 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준 코드이다.

## dir

`dir(x)`는 객체가 지닌 변수나 함수(메서드)를 보여 준다.

```python
dir([1, 2, 3])    # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', ...]
dir({'1': 'a'})   # ['__class__', '__class_getitem__', '__contains__', '__delattr__', ...]
```

> 앞쪽에는 `__add__` 같은 특별 메서드가 나오고, 뒤쪽에 `append`, `count`, `keys`, `values`처럼 앞에서 배운 메서드들이 이어진다.

## divmod

`divmod(a, b)`는 2개의 숫자 `a`, `b`를 입력받아 `a`를 `b`로 나눈 몫과 나머지를 튜플로 반환한다.

```python
divmod(7, 3)   # (2, 1)
7 // 3         # 2: 몫
7 % 3          # 1: 나머지
```

## enumerate

`enumerate`는 '열거하다'라는 뜻으로, 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력받아 인덱스 값을 포함하는 enumerate 객체를 반환한다. 보통 `for` 문과 함께 사용한다.

```python
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar
```

> 반복되는 구간에서 현재 어느 위치인지 알려 주는 인덱스 값이 필요할 때 매우 유용하다.

## eval

`eval(expression)`은 문자열로 구성된 표현식을 입력받아 그 문자열을 실행한 결괏값을 반환한다.

```python
eval('1+2')            # 3
eval("'hi' + 'a'")     # 'hia'
eval('divmod(4, 3)')   # (1, 1)
```

> `eval`은 입력 문자열을 실제로 실행하므로, 신뢰할 수 없는 외부 입력에는 사용하면 안 된다.

## filter

`filter`는 '무엇인가를 걸러 낸다'라는 뜻이다. 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받아, 요소를 순서대로 함수에 전달하여 **반환값이 참인 것만** 묶어서 반환한다.

```python
filter(함수, 반복_가능한_데이터)
```

0보다 큰 수만 남기는 예를 보자.

```python
# filter에 넣을 함수 정의
def positive(x):
    return x > 0

# filter 수행
filtered = filter(positive, [1, -3, 2, 0, -5, 6])
list(filtered)   # [1, 2, 6]
```

`1`, `2`, `6`만 `x > 0` 조건에 참이므로 `[1, 2, 6]`이 남는다. `filter`는 filter 객체를 반환하므로 결과를 눈으로 확인하려고 `list`를 사용했다.

- **lambda를 쓰면 더 간단하다** — 함수를 따로 정의하지 않아도 된다.

  ```python
  list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))   # [1, 2, 6]
  ```

## hex

`hex(x)`는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 반환한다.

```python
hex(234)   # '0xea'
hex(3)     # '0x3'
```

## id

`id(object)`는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 반환한다.

```python
a = 3
id(a)   # 4379779928
b = a
id(b)   # 4379779928
```

`a`와 `b`의 주솟값이 같다. 즉 둘은 같은 객체를 가리키고 있다. `id(4)`처럼 다른 객체를 넣으면 당연히 다른 값이 나온다.

> 주솟값은 실행 환경과 시점에 따라 달라진다. 위 숫자는 예시일 뿐이다.

## input

`input([prompt])`은 사용자 입력을 받는다. 입력 인수로 문자열을 전달하면 그 문자열이 프롬프트가 된다.

```python
a = input()
b = input("Enter: ")
```

> `[]`는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 자세한 사용법은 [사용자 입출력(input/print)](UserIO.md)을 참고한다.

## int

`int(x)`는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환한다. 정수가 입력되면 그대로 반환한다.

```python
int('3')   # 3
int(3.4)   # 3
int(3.7)   # 3: 반올림하지 않고 소수점을 버린다
```

- **`int(x, radix)`** — `radix` 진수로 표현된 문자열 `x`를 10진수로 변환한다.

  ```python
  int('11', 2)    # 3: 2진수 11
  int('1A', 16)   # 26: 16진수 1A
  ```

## isinstance

`isinstance(object, class)`는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받아 그 객체가 해당 클래스의 인스턴스인지 판단한다.

```python
class Person: pass

a = Person()
isinstance(a, Person)   # True

b = 3
isinstance(b, Person)   # False
```

## len

`len(s)`는 입력값 `s`의 길이(요소의 전체 개수)를 반환한다.

```python
len("python")   # 6
len([1, 2, 3])  # 3
len((1, 'a'))   # 2
```

## list

`list(iterable)`은 반복 가능한 데이터를 입력받아 리스트로 만들어 반환한다.

```python
list("python")   # ['p', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3))  # [1, 2, 3]
```

> 리스트를 입력하면 똑같은 리스트를 **복사하여** 반환한다. `b = list(a)`로 만든 `b`는 `a`와 값은 같지만 다른 객체다.

## map

`map(f, iterable)`은 함수 `f`와 반복 가능한 데이터를 입력받아, 데이터의 각 요소에 함수 `f`를 적용한 결과를 반환한다.

```python
# 요소에 2를 곱한다
def two_items(x):
    return x * 2

mapped = map(two_items, [1, 2, 3, 4])
list(mapped)   # [2, 4, 6, 8]
```

리스트의 첫 번째 요소 `1`이 `two_items`에 들어가 `2`가 되고, 두 번째 요소 `2`가 `4`가 되는 식으로 모든 요소가 처리된다. `map`은 map 객체를 반환하므로 결과 확인에는 `list`를 사용했다.

- **lambda를 쓴 예** — 함수를 따로 정의하지 않아도 된다.

  ```python
  mapped = map(lambda a: a*2, [1, 2, 3, 4])
  list(mapped)   # [2, 4, 6, 8]
  ```

## max

`max(iterable)`는 반복 가능한 데이터를 입력받아 최댓값을 반환한다.

```python
max([1, 2, 3])   # 3
max("python")    # 'y'
```

## min

`min(iterable)`는 `max`와 반대로 최솟값을 반환한다.

```python
min([1, 2, 3])   # 1
min("python")    # 'h'
```

## oct

`oct(x)`는 정수를 8진수 문자열로 바꾸어 반환한다.

```python
oct(34)      # '0o42'
oct(12345)   # '0o30071'
```

## open

`open(filename, [mode])`은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 반환한다. `mode`를 생략하면 기본값인 읽기 모드(`r`)로 파일 객체를 만든다.

| mode | 설명 |
| --- | --- |
| `w` | 쓰기 모드로 파일 열기 |
| `r` | 읽기 모드로 파일 열기 |
| `a` | 추가 모드로 파일 열기 |
| `b` | 바이너리 모드로 파일 열기 |

```python
f = open("binary_file", "rb")   # rb는 '바이너리 읽기 모드'를 의미한다
```

> `b`는 `w`, `r`, `a`와 함께 사용한다. 파일 다루기는 [파일 읽고 쓰기(file I/O)](FileIO.md)에서 자세히 다룬다.

## ord

`ord(c)`는 문자의 유니코드 숫자 값을 반환한다. `chr`과 반대로 동작한다.

```python
ord('a')   # 97
ord('가')   # 44032
```

## pow

`pow(x, y)`는 `x`를 `y`제곱한 결괏값을 반환한다.

```python
pow(2, 4)   # 16
pow(3, 3)   # 27
```

## range

`range([start,] stop [,step])`은 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환한다. `for` 문과 함께 자주 사용한다.

- **인수가 하나일 경우** — 시작 숫자를 지정하지 않으면 0부터 시작한다.

  ```python
  r = range(5)
  list(r)   # [0, 1, 2, 3, 4]
  ```

- **인수가 2개일 경우** — 시작 숫자와 끝 숫자를 나타낸다. 단 끝 숫자는 범위에 포함되지 않는다.

  ```python
  r = range(5, 10)
  list(r)   # [5, 6, 7, 8, 9]
  ```

- **인수가 3개일 경우** — 세 번째 인수는 숫자 사이의 거리다.

  ```python
  r = range(1, 10, 2)
  list(r)   # [1, 3, 5, 7, 9]

  r = range(0, -10, -1)
  list(r)   # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
  ```

> 값이 줄어드는 범위를 만들려면 `step`을 반드시 넣어야 한다. `range(0, -10)`은 빈 범위(`[]`)가 된다.

## round

`round(number [,ndigits])`는 숫자를 입력받아 반올림해 반환한다. 두 번째 인수 `ndigits`는 반올림하여 표시할 소수점 자릿수를 의미한다.

```python
round(4.6)        # 5
round(4.2)        # 4
round(5.678, 2)   # 5.68: 소수점 2자리까지만 반올림
```

## sorted

`sorted(iterable)`는 입력 데이터를 정렬한 후 그 결과를 리스트로 반환한다.

```python
sorted([3, 1, 2])        # [1, 2, 3]
sorted(['a', 'c', 'b'])  # ['a', 'b', 'c']
sorted("zero")           # ['e', 'o', 'r', 'z']
sorted((3, 2, 1))        # [1, 2, 3]
```

> 리스트에도 `sort` 함수가 있다. 하지만 리스트의 `sort`는 리스트 객체 자체를 정렬만 할 뿐 정렬된 결과를 반환하지는 않는다.

## str

`str(object)`는 객체를 문자열 형태로 변환하여 반환한다.

```python
str(3)      # '3'
str('hi')   # 'hi'
```

## sum

`sum(iterable)`은 입력 데이터의 합을 반환한다.

```python
sum([1, 2, 3])   # 6
sum((4, 5, 6))   # 15
```

## tuple

`tuple(iterable)`은 반복 가능한 데이터를 튜플로 바꾸어 반환한다. 입력이 튜플이면 그대로 반환한다.

```python
tuple("abc")      # ('a', 'b', 'c')
tuple([1, 2, 3])  # (1, 2, 3)
tuple((1, 2, 3))  # (1, 2, 3)
```

## type

`type(object)`는 입력값의 자료형이 무엇인지 알려 준다.

```python
type("abc")                     # <class 'str'>
type([])                        # <class 'list'>
type(open("temp/test", 'w'))    # <class '_io.TextIOWrapper'>
```

## zip

`zip(*iterable)`은 동일한 개수로 이루어진 데이터들을 묶어서 반환한다. `*iterable`은 반복 가능한 데이터를 여러 개 입력할 수 있다는 의미다.

```python
zip1 = zip([1, 2, 3], [4, 5, 6])
zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
zip3 = zip("abc", "def")
list(zip1)   # [(1, 4), (2, 5), (3, 6)]
list(zip2)   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip3)   # [('a', 'd'), ('b', 'e'), ('c', 'f')]
```
