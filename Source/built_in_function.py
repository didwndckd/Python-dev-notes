# built_in_function.py

# abs(x): 절대값 반환
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

# all(x): 반복 가능한 데이터 x를 입력값으로 받아 x의 요소가 모두 참이면 True, 거짓이면 False를 반환
# 반복 가능한 자료형: for 문에서 사용 가능한 자료형, 리스트, 튜플, 문자열, 딕셔너리, 집합 등
print(all([1, 2, 3])) # True
print(all([1, 2, 3, 0])) # False: 0이 거짓
print(all([])) # True: 입력 인수가 빈 값인 경우 True

# any(x): 반복 가능한 데이터 x를 입력 받아 하나라도 참이 있으면 True, 모두 거짓인 경우 False
print(any([1, 2, 3, 0])) # True: 0만 거짓
print(any([0, ""])) # False: 모두 거짓임
print(any([])) # False: 입력 인수가 빈값인 경우 False

# chr(i): 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자 반환
print(chr(97)) # a
print(chr(44032)) # 가

# dir(x): 객체가 지닌 변수나 함수를 보여주는 함수. 다음 예는 리스트와 딕셔너리가 지닌 함수(메서드)를 보여준다.
print(dir([1, 2, 3])) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', ...]
print(dir({'1': 'a'})) # ['__class__', '__class_getitem__', '__contains__', '__delattr__', ...]

# divmod(a, b): 2개의 숫자 a, b를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7, 3)) # (2, 1)
print(7 // 3) # 2
print(7 % 3) # 1

# enumerate(l): '열거하다'라는 뜻, 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체 반환
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 실행결과
# 0 body
# 1 foo
# 2 bar

# eval: eval(expression)은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값 반환
print(eval('1+2')) # 3
print(eval("'hi' + 'a'")) # hia
print(eval('divmod(4, 3)')) # (1, 1)

# filter(함수, 반복_가능한_데이터): 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다. 반복 가능한 데이터의 요소를 순서대로 함수에 전달하여 반환값이 참인 것만 묶어서 반환한다.
# 예: 0보다 큰 수만 남긴다.
# filter에 넣을 함수 정의
def positive(x):
    return x > 0
# filter 수행
filtered = filter(positive, [1, -3, 2, 0, -5, 6])
print(list(filtered)) # [1, 2, 6]

# hex(x): 정수를 입력받아 16진수 문자열로 변환하여 반환
print(hex(234)) # 0xea
print(hex(3)) # 0x3

# id(object): 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 반환
# 아래 예시는 모두 같은 주소를 나타냄(참조 개념), 실행 시점에 따라 달라질 수 있음
a = 3
print(id(a)) # 4379779928
print(id(a)) # 4379779928
b = a
print(id(b)) # 4379779928

# input([prompt]): 사용자 입력을 받는다.
# []는 괄호 안의 내용을 생략할 수 있다는 관례표기법이다.
# a = input()
# b = input("Enter: ")

# int(x): 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환, 정수가 입력되면 그대로 반환
print(int('3')) # 3
print(int(3.4)) # 3
print(int(3.7)) # 3: 반올림도 하지 않음, 소수점은 버린다.

# isinstance(object, class): 첫번째 인수로 객체, 두번째 인수로 클래스를 받고 입력받은 객체가 해당 클래스의 인스턴스인지 판단
class Person: pass
a = Person()
print(isinstance(a, Person)) # True
b = 3
print(isinstance(b, Person)) # False

# len(s): 입력값 s의 길이(요소의 전체 개수)를 반환
print(len("python")) # 6
print(len([1, 2, 3])) # 3
print(len((1, 'a'))) # 2

# list(iterable): 반복 가능한 데이터를 입력받아 리스트로 반환
print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3))) # [1, 2, 3]

# map(f, iterable): 함수(f)와 반복 가능한 데이터를 입력으로 받는다. 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 반환.
# 예시: 요소에 2 곱한다.
def two_items(x): 
    return x * 2
mapped = map(two_items, [1, 2, 3, 4])
print(list(mapped)) # [2, 4, 6, 8]

# 람다를 사용한 예시
mapped = map(lambda a: a*2, [1, 2, 3, 4])
print(list(mapped)) # [2, 4, 6, 8]

# max(iterable): 반복 가능한 데이터를 입력받아 최댓값을 반환
print(max([1, 2, 3])) # 3
print(max("python")) # y

# min(iterable): max와 반대로 반복 가능한 데이터를 입력받아 최솟값을 반환
print(min([1, 2, 3])) # 1
print(min("python")) # h

# oct(x): 정수를 8진수 문자열로 바꾸어 반환하는 함수.
print(oct(34)) # 0o42
print(oct(12345)) # 0o30071

# open(filename, [mode]): 파일 이름과 읽기 방법을 입력받아 파일 객체를 반환, mode를 생략하면 기본값인 읽기 모드(r)로 파일 객체를 만들어 반환.
# w: 쓰기 모드
# r: 읽기 모드
# a: 추가 모드
# b: 바이너리 모드
# f = open("binary_file", "rb") # rb는 '바이너리 읽기 모드'를 의미함.

# ord(c): 문자의 유니코드 숫자 값을 반환.
print(ord('a')) # 97
print(ord('가')) # 44032

# pow(x, y): x를 y제곱한 결과값을 반환
print(pow(2, 4)) # 16
print(pow(3, 3)) # 27

# range([start], stop, [step]): for 문과 함께 자주 사용하는 함수, 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환
# 시작 숫자를 지정하지 않으면 0부터
r = range(5)
print(list(r)) # [0, 1, 2, 3, 4]
# 2개 인수면 시작 숫자와 끝 숫자를 나타낸다, 단 끝숫자는 해당 범위에 포함되지 않는다.
r = range(5, 10)
print(list(r)) # [5, 6, 7, 8, 9]

# 세 번째 인수는 숫자 사이의 거리를 말한다.
r = range(1, 10, 2)
print(list(r)) # [1, 3, 5, 7, 9]
# r = range(0, -10) -> [] -로 range 만들려면 step을 반드시 넣어야함.
r = range(0, -10, -1)
print(list(r)) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# round(number, [,ndigits]): 숫자를 입력받아 반올림해 반환.
print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(5.678, 2)) # 5.68: 소수점 2자리까지만 반올림.

# sorted(iterable): 입력 데이터를 정렬한 후 결과를 리스트로 반환.
print(sorted([3, 1, 2])) # [1, 2, 3]
print(sorted(['a', 'c', 'b'])) # ['a', 'b', 'c']
print(sorted("zero")) # ['e', 'o', 'r', 'z']
print(sorted((3, 2, 1))) # [1, 2, 3]

# str(object): 객체를 문자열 형태로 변환하여 반환
print(str(3)) # '3'
print(str('hi')) # 'hi'

# sum(iterable): 입력 데이터의 합을 반환
print(sum([1, 2, 3])) # 6
print(sum((4, 5, 6))) # 15

# tuple(iterable): 반복 가능한 데이터를 튜플로 바꾸어 반환, 입력이 튜플인 경우 그대로 반환.
print(tuple("abc")) # ('a', 'b', 'c')
print(tuple([1, 2, 3])) # (1, 2, 3)
print(tuple((1, 2, 3))) # (1, 2, 3)

# type(object): 입력값의 자료형이 무엇인자 알려주는 함수
print(type("abc")) # <class 'str'>
print(type([])) # <class 'list'>
print(type(open("temp/test", 'w'))) # <class '_io.TextIOWrapper'>

# zip(*iterable): 동일한 개수로 이루어진 데이터들을 묶어서 반환
zip1 = zip([1, 2, 3], [4, 5, 6])
zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
zip3 = zip("abc", "def")
print(list(zip1)) # [(1, 4), (2, 5), (3, 6)]
print(list(zip2)) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip3)) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
