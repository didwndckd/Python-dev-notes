# 이터레이터와 제너레이터(iterator/generator)

> 예제 코드: [Source/iterator_generator.py](Source/iterator_generator.py)

- [이터레이터란?](#이터레이터란)
- [이터레이터 만들기](#이터레이터-만들기)
- [제너레이터란?](#제너레이터란)
- [제너레이터 표현식](#제너레이터-표현식)
- [클래스 이터레이터와 제너레이터](#클래스-이터레이터와-제너레이터)
- [제너레이터 활용하기](#제너레이터-활용하기)

## 이터레이터란?

리스트처럼 `for` 문에서 사용할 수 있는 객체를 반복 가능(iterable) 객체라고 한다. 이터레이터(iterator)는 그중 `next()`로 값을 하나씩 꺼낼 수 있는 객체이며, 모두 꺼내면 `StopIteration` 예외가 발생한다.

```python
a = [1, 2, 3]
# next(a)   # TypeError: 'list' object is not an iterator

ia = iter(a)                  # 반복 가능 객체를 이터레이터로 변환
print(type(ia))                # <class 'list_iterator'>
print(next(ia))                # 1
print(next(ia))                # 2
print(next(ia))                # 3
# print(next(ia))              # StopIteration
```

`for` 문은 내부적으로 `next()` 호출과 `StopIteration` 처리를 자동으로 수행한다.

```python
a = [1, 2, 3]
ia = iter(a)
for i in ia:
    print(i)
# 1
# 2
# 3

for i in ia:
    print(i)
# 아무것도 출력되지 않음
```

> 이터레이터는 현재 위치를 기억하며 앞으로만 진행한다. 모두 소비한 뒤 다시 반복하려면 `iter()`로 새 이터레이터를 만들어야 한다.

## 이터레이터 만들기

클래스로 이터레이터를 만들려면 `__iter__`와 `__next__` 메서드를 구현한다. `iter()`는 `__iter__`를, `next()`는 `__next__`를 자동으로 호출한다.

```python
class 이터레이터_이름:
    def __iter__(self):
        return self

    def __next__(self):
        # 다음 값을 반환하고, 더 이상 없으면 StopIteration 발생
        pass
```

- **순서대로 꺼내기** — `position`으로 현재 위치를 기록한다.

  ```python
  class MyIterator:
      def __init__(self, data):
          self.data = data
          self.position = 0

      def __iter__(self):
          return self

      def __next__(self):
          if self.position >= len(self.data):
              raise StopIteration
          result = self.data[self.position]
          self.position += 1
          return result

  i = MyIterator([1, 2, 3])
  for item in i:
      print(item)
  # 1
  # 2
  # 3
  ```

- **역순으로 꺼내기** — 마지막 인덱스에서 시작해 위치를 하나씩 줄인다.

  ```python
  class ReverseIterator:
      def __init__(self, data):
          self.data = data
          self.position = len(self.data) - 1

      def __iter__(self):
          return self

      def __next__(self):
          if self.position < 0:
              raise StopIteration
          result = self.data[self.position]
          self.position -= 1
          return result

  i = ReverseIterator([1, 2, 3])
  for item in i:
      print(item)
  # 3
  # 2
  # 1
  ```

## 제너레이터란?

제너레이터(generator)는 이터레이터를 간단히 만드는 함수이다. `return` 대신 `yield`를 쓰며, `yield`에서 값을 반환하고 실행 위치를 멈췄다가 다음 호출에서 이어서 실행한다.

```python
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g))   # <class 'generator'>
print(next(g))   # a
print(next(g))   # b
print(next(g))   # c
# print(next(g)) # StopIteration
```

> 제너레이터 객체는 함수를 호출하는 즉시 모든 코드를 실행하지 않는다. `next()`나 `for` 문으로 값을 요청할 때마다 다음 `yield`까지 실행한다.

## 제너레이터 표현식

`yield`를 쓰는 함수 대신, 리스트 컴프리헨션과 비슷한 소괄호 표현식으로도 제너레이터를 만들 수 있다. 소괄호를 사용하지만 튜플이 아니라 제너레이터가 만들어진다.

```python
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9

gen = (i * i for i in range(1, 1000))
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
```

## 클래스 이터레이터와 제너레이터

복잡한 상태나 동작을 구현해야 한다면 클래스 이터레이터가 적합하다. 단순히 값을 순서대로 만들어 내는 경우에는 제너레이터 함수나 표현식이 더 짧고 읽기 쉽다.

```python
# 제너레이터 표현식
gen = (i * i for i in range(1, 1000))

# 같은 동작을 클래스로 구현
class MyIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.data >= 1000:
            raise StopIteration
        result = self.data * self.data
        self.data += 1
        return result
```

## 제너레이터 활용하기

리스트 컴프리헨션은 만들 때 모든 항목을 계산하지만, 제너레이터 표현식은 필요한 항목만 계산한다. 모든 결과가 필요하지 않거나 데이터가 클 때 시간과 메모리를 아낄 수 있다.

```python
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])
# job start  # 5번 출력
# ...
# done        # 첫 번째 결과만 필요해도 약 5초 기다림

gen_job = (longtime_job() for i in range(5))
print(next(gen_job))
# job start
# done        # 첫 번째 작업만 실행하므로 약 1초
```

> 필요한 순간에만 값을 계산하는 방식을 느긋한 계산법(lazy evaluation)이라고 한다. 대용량 데이터, 오래 걸리는 작업, 끝이 없는 데이터 스트림에 특히 유용하다.
