# 이터레이터(iterator): 반복 가능한 객체
# 이터레이터는 next() 함수로 값을 하나씩 꺼낼 수 있는 객체이다. 모든 값을 꺼내면 StopIteration 예외가 발생한다.

# 반복 가능하다고 해서 이터레이터는 아니다.
a = [1, 2, 3]
# next(a) # TypeError: 'list' object is not an iterator

# 반복 가능한 객체는 iter함수로 이터레이터로 만들 수 있다.
ia = iter(a)
print(type(ia)) # <class 'list_iterator'>

print(next(ia)) # 1
print(next(ia)) # 2
print(next(ia)) # 3
# print(next(ia)) # 더이상 나올것이 없어 StopIteration 예외 raise

# 이터레이터는 반복문을 돌릴 수 있다
a = [1, 2, 3]
ia = iter(a)
for i in ia:
    print(i)
# 실행결과
# 1
# 2
# 3

for i in ia:
    print(i)
# 실행결과: 아무것도 나오지 않음 앞에서 이미 next를 모두 소비해서 나오지 않음

# 이터레이터 만들기
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    # 이터레이터 클래스의 필수 메서드: 이 메서드가 있어야 파이썬이 반복 가능한 객체로 인식한다.
    def __iter__(self):
        return self

    # 이터레이터 클래스의 필수 메서드: 다음 값을 반환한다.
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration

        result = self.data[self.position]
        self.position += 1
        return result

i = MyIterator([1, 2, 3])
for item in i:
    print(item)
# 실행 결과
# 1
# 2
# 3

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
# 실행결과
# 3
# 2
# 1

# 제너레이터
# 이터레이터를 쉽게 만들어주는 함수
# 이터레이터를 클래스로 만들려면 __iter__와 __next__메서드를 구현해야함.
# 제너레이터를 사용하면 함수 하나로 간단하게 이터레이터를 만들 수 있음.

# yield를 사용하여 제너레이터를 만든다.
# 1. yield를 만나면 값을 반환하고 함수 실행을 일시 정지 한다.
# 2. 다시 호출하면 일시 정지 했던 지점부터 실행

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g)) # <class 'generator'>
print(next(g)) # a
print(next(g)) # b
print(next(g)) # c
# print(next(g)) # StopIteration

# 1부터 1000까지의 각각의 숫자를 제곱한 값을 순서대로 반환하는 제너레이터
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
gen = mygen()
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9

# 소괄호를 사용한 제너레이터 표현식
gen = (i * i for i in range(1, 1000))
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9

# gen = (i * i for i in range(1, 1000))를 이터레이터 클래스로 만든 예시
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

import time

def longtime_job():
    print("job start")
    time.sleep(1) 
    return "done"
list_job = [longtime_job() for i in range(5)]
print(list_job[0]) # 첫번째 결과만 필요한 상황
# list를 만들 때 longtime_job()이 실행 되고 그 결과가 리스트에 담긴다. 즉 리스트를 만드는 시간이 5초임
# 실행결과: 총 5초가 걸리고 "job start" 다섯번 출력 후 "done"이 출력
# job start
# job start
# job start
# job start
# job start
# done

# 제너레이터 표현식: 함수를 미리 실행하지 않고 필요할 때 실행
gen_job = (longtime_job() for i in range(5))
print(next(gen_job)) # 첫번째 값만 요청