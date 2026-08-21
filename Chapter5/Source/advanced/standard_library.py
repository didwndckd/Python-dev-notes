# standard_library.py

# datetime.date
from builtins import print
import datetime
# datetime.date 객체 만들기
day1 = datetime.date(2026, 8, 5)
day2 = datetime.date(1992, 9, 29)

# 날짜 차이
diff = day1 - day2
print(type(diff)) # <class 'datetime.timedelta'>
print(diff.days) # 12363

# 요일 뽑기
day = datetime.date(2026, 8, 5)
print(day.weekday()) # 2(수): 0(월) ~ 6(일)
print(day.isoweekday()) # 3(수): 1(월) ~ 7(일)

# time
import time
# time.time(): 현재 시간(UTC)
now = time.time()
print(now) # 1785935404.674016

# time.localtime: time.time()이 반환한 실수값을 연, 월, 일, 시, 분, 초로 바꿔주는 함수, 이건 UTC 말고 현지 시간인듯
localtime = time.localtime(now)
print(localtime) # time.struct_time(tm_year=2026, tm_mon=8, tm_mday=5, tm_hour=22, tm_min=12, tm_sec=20, tm_wday=2, tm_yday=217, tm_isdst=0)
print(time.localtime()) # 인수가 없으면 현재 시간으로 생성

# time.asctime: time.localtime이 반환한 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 반환
asctime = time.asctime(localtime)
print(asctime) # Wed Aug  5 22:32:32 2026
print(time.asctime()) # 인수가 없으면 현재 시간으로 생성

# time.ctime: 현재 시간의 asctime을 바로 뽑아오기
ctime = time.ctime()
print(ctime) # Wed Aug  5 22:34:10 2026

# time.strftime: _TimeTuple | struct_time을 받아 포맷에 맞춰 문자열 반환
print(time.strftime('%x', localtime)) # 08/05/26
print(time.strftime('%c', localtime)) # Wed Aug  5 22:39:17 2026
print(time.strftime('%c')) # 시간 인수가 없으면 현재 시간으로 생성

# time.sleep: 넣은 시간만큼 멈춘다.
start = time.time() # 시작 시간
# time.sleep(1) # 1초 대기
end = time.time() # 종료 시간
print(end - start) # 1.005047082901001: 정확히 1초는 아니지만 거의 1초 차이


# math
import math

# math.gcd: 최대 공약수(greatest common divisor) 구하기
# 파이썬 3.5 버전부터 사용 가능
# 파이썬 3.9 버전부터는 여러개의 인수를 입력할 수 있지만 3.9 미만에서는 2개까지만 허용된다.
# 60, 100, 80의 최대 공약수 구하기
gcd = math.gcd(60, 100, 80)
print(gcd) # 20

# math.lcm: 최소 공배수(least common multiple) 구하기
# 파이썬 3.9 버전부터 사용 가능
lcm = math.lcm(15, 25)
print(lcm) # 75

# random: 난수 발생 모듈
import random

# random.random(): 0 ~ 1 사이의 실수중 난수값 반환
print(random.random()) # 0.1601055394682327

# random.randint: 정수 난수 반환
print(random.randint(1, 10)) # 8: 1 ~ 10 사이의 정수중 난수 반환
print(random.randint(1, 55)) # 25: 1 ~ 55 사이의 정수중 난수 반환

# random 모듈을 사용해서 함수 만들기
def random_pop(data):
    # 0 ~ data의 마지막 인덱스 사이의 랜덤
    number = random.randint(0, len(data) - 1)
    return data.pop(number)
data = [1, 2, 3, 4, 5]
while data:
    print(random_pop(data))
# 실행 결과
# 5
# 4
# 2
# 1
# 3

# random.choice: 입력으로 받은 리스트에서 무작위로 하나를 선택해서 반환
data = [1, 2, 3, 4, 5]
choice = random.choice(data)
print(choice) # 1

# random.sample: 입력으로 전달받은 리스트에서 원하는 갯수를 꺼내서 리스트로 반환
data = [1, 2, 3, 4, 5]
sample = random.sample(data, 3)
print(sample) # [4, 5, 3]


# itertools
import itertools
# itertools.zip_longest(*iterables, fillvalue=None): 여러개의 반복 가능한 객체 묶어준다 zip과 다르게 길이가 다른 객체 묶을 때 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 채운다.
students = ['한민서', '황지민', '이영철', '이광수', '김승민'] # 5개
snacks = ['사탕', '초콜릿', '젤리'] # 3개
result = itertools.zip_longest(students, snacks, fillvalue="새우깡")
print(list(result)) # [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')] -> 뒤에 이광수, 김승민은 fillvalue인 새우깡으로 채워짐

# itertools.permutations(iterable, r): 반복 가능 객체 중 r개를 선택한 순열을 이터레이터로 반환
# 예제: 1, 2, 3이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구한다.
result = itertools.permutations(['1', '2', '3'], 2)
print(list(result)) # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# itertools.combinations(iterable, r): 반복 가능 객체중 r개를 선택한 조합을 이터레이터로 반환
# 예제: 1 ~ 45중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고 그 개수를 출력
result = itertools.combinations(range(1, 46), 6)
print(len(list(result))) # 8145060

# itertools.combinations_with_replacement(iterable, r): 반복 가능한 객체중 r개를 선택한 조합(중복 가능)을 이터레이터로 반환
result = itertools.combinations_with_replacement(range(1, 46), 6)
print(len(list(result))) # 15890700

# functools
import functools
# functools.reduce(function, iterable): 함수(function)를 반복가능한 객체의 요소에 차례대로 누적 적용하여 하나의 값으로 반환
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data) # 데이터의 모든 합을 구함
print(result) # 15
# functools.reduce로 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num) # 8

# operator.itemgetter: 꺼내오는 함수를 만들어주는 함수, 람다 대신 넣을 수 있다.
from operator import itemgetter
# 이름, 나이, 성정 등의 정보를 가진 리스트를 나이순으로 정렬 하려고 한다면?
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
key = itemgetter(1) # 다음 람다와 같다고 볼 수 있다. lambda x: x[1]
result = sorted(students, key=key)
print(result) # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

result = sorted(students, key=lambda x: x[1]) # 따라서 itemgetter 대신 람다를 넣어도 동일하게 동작 한다.
print(result) # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

# 딕셔너리 리스트일 때
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
result = sorted(students, key=itemgetter('age'))
print(result) # [{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]

# operator.attrgetter: 리스트 요소가 튜플이나 딕셔너리등이 아닌 클래스일 때 사용
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
mapped = map(lambda student: (student.name, student.age, student.grade), sorted_students) # 볼 수 있도록 튜플로 변환
print(list(mapped)) # [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

# shutil: 파일을 복사 하거나 이동할 때 사용하는 모듈
import shutil
import pathlib
# 테스트를 위해 임시 디렉터리 생성
pathlib.Path("temp").mkdir(exist_ok=True) 
pathlib.Path("temp/backup").mkdir(exist_ok=True)
# a.txt 파일 생성
with open("temp/a.txt", 'w') as f:
    f.write("test")

# shutil.copy(기존_경로, 복사할_경로): 파일 복사하기(디렉터리는 이미 있어야함)
# temp/a.txt 파일을 temp/backup/a.txt.bak으로 복사한다고 가정
shutil.copy("temp/a.txt", "temp/backup/a.txt.bak")

# shutil.move(기존_경로, 옮길_경로): 파일 옮기기(디렉터리는 이미 있어야함)
# temp/a.txt 파일을 temp/backup/a.txt로 옮기기
shutil.move("temp/a.txt", "temp/backup/a.txt")

# glob: 와일드카드 패턴으로 파일 경로를 찾는 모듈
import glob
# 패턴 문법
# *: 임의의 문자 0개 이상, 단 /는 넘지 않는다. 예) *.py
# ?: 임의의 한 글자. 예) mod?.py -> mod1.py, mod2.py
# [seq]: 괄호 안 문자 중 하나. 예) mod[12].py -> mod1.py, mod2.py
# [!seq]: 괄호 안 문자가 아닌 것 하나. 예) [!_]*.py -> _로 시작하지 않는 .py
# **: 하위 디렉터리 전체, recursive=True를 함께 써야 모든 깊이를 의미한다. 예) Chapter*/Source/**/*.py
# 주의
# 정렬 순서는 보장되지 않는다. 필요하면 sorted()로 감싼다.
# 숨김 파일(.gitignore 등)은 *에 걸리지 않는다. .* 로 따로 찾아야 한다.
# 중괄호 확장(*.{py,md})은 셸 문법이라 지원하지 않는다. 두 번 호출해서 합쳐야 한다.

# glob(pathname): 디렉터리에 있는 파일들을 리스트로 만들기
# Source 바로 아래의 .py만 반환, *는 /를 넘지 않으므로 하위 디렉터리는 포함되지 않는다.
paths = glob.glob("Chapter2/Source/*.py")
print(paths) # ['Chapter2/Source/bool.py', 'Chapter2/Source/dictionary.py', ...]

# Source 하위 디렉터리의 .py 반환
paths = glob.glob("Chapter2/Source/*.py")
print(paths) # ['Chapter2/Source/tuple.py', 'Chapter2/Source/list.py', ...]

# Source 아래 모든 깊이의 .py 반환
paths = glob.glob("Chapter*/Source/**/*.py", recursive=True)
print(paths) # ['Chapter2/Source/bool.py', 'Chapter5/Source/advanced/built_in_function.py', ...]

# pickle: 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
# pickle이 만드는 결과물 자체가 bytes이므로 저장은 'wb', 로드는 'rb'로 해야 한다.
# pickle.dumps({"name": "jane"}) -> b'\x80\x04\x95\x17...}\x94\x8c\x04name\x94\x8c\x04jane\x94s.'
# 'w'로 열면 TypeError, 'r'로 열면 UnicodeDecodeError가 난다.
path = "temp/test.txt"
# pickle.dump(데이터, 파일객체): 데이터를 파일에 저장
with open(path, 'wb') as f:
    data = {1: 'python', 2: 'you need'}
    pickle.dump(data, f)

# pickle.load(파일객체): 파일 로드
with open(path, 'rb') as f:
    data = pickle.load(f)
    print(data) # {1: 'python', 2: 'you need'}

# class로도 가능함
# 단, 클래스 정의(코드)가 저장되는 것은 아니다.
# 저장되는 것은 "모듈 이름 + 클래스 이름"이라는 이름표와 인스턴스의 속성값(__dict__)뿐이다.
# 실제 저장된 바이트를 pickletools.dis()로 열어보면 다음 순서로 되어 있다.
#   SHORT_BINUNICODE '__main__'  # 이 모듈에서
#   SHORT_BINUNICODE 'Student'   # 이 이름을 찾아라
#   STACK_GLOBAL                 # -> 실제 클래스 객체를 가져온다
#   NEWOBJ                       # __new__로 빈 인스턴스를 만든다(__init__은 호출되지 않는다)
#   SETITEMS / BUILD             # __dict__에 속성값을 채워 넣는다
# 그래서 load하는 쪽에 같은 이름의 클래스 정의가 없으면 다음 오류가 난다.
#   AttributeError: module '__main__' has no attribute 'Student'
# 여기서 잘 동작하는 이유는 저장과 로드가 같은 파일 안에서 이뤄져 Student가 이미 정의되어 있기 때문이다.
# 주의할 점
# __init__을 거치지 않으므로 생성자에서 하던 검증이나 초기화는 전부 건너뛴다.
# 클래스 이름을 바꾸거나 다른 모듈로 옮기면 기존 pkl 파일은 읽을 수 없다.
#   -> pickle할 클래스는 __main__이 아니라 별도 모듈(models.py 등)에 두는 것이 안전하다.
# 나중에 속성을 추가해도 예전에 저장한 파일에는 그 속성이 없다(마이그레이션 개념이 없음).
# 메서드는 저장되지 않으므로 복원된 객체는 현재 클래스 코드의 메서드를 따른다.
# pickle.load는 파일에 적힌 이름대로 import하고 호출하므로, 신뢰할 수 없는 pkl 파일은 절대 열면 안 된다.
with open(path, 'wb') as f:
    data = Student("yjc", 35, "A")
    pickle.dump(data, f)

with open(path, 'rb') as f:
    data = pickle.load(f)
    print(data) # <__main__.Student object at 0x104cbfa80>
    print(data.name) # yjc
    print(data.age) # 35
    print(data.grade) # A

# os: 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈
import os

# os.environ: 현재 시스템의 환경 변숫값을 반환
environ = os.environ
print(environ) # environ({'COMMAND_MODE': 'unix2003', 'HOME': '/Users/yjc', 'LOGNAME': 'yjc', ...})
# environ은 딕셔너리 형태로 key로 원하는 값을 뽑을 수 있음
print(environ['HOME']) # /Users/yjc

# os.getcwd: 현재 자신의 디렉터리 위치 반환
print(os.getcwd()) # /Users/yjc/Workspace/Python-dev-notes

# os.chdir: 현재 디렉터리 위치 변경
os.chdir("Source")
print(os.getcwd()) # /Users/yjc/Workspace/Python-dev-notes/Source
os.chdir("..")
print(os.getcwd()) # /Users/yjc/Workspace/Python-dev-notes

# os.system: 시스템 명령어 호출
os.system("ls")

# os.popen: 시스템 명령어를 호출하고 결과값을 돌려받는다
f = os.popen('ls')
print(f.read()) # Bool.md                 Dictionary.md           Function.md...
f.close()

# os.mkdir: 디렉터리 생성
os.mkdir("temp/test")

# os.rmdir: 디렉터리 삭제, 디렉터리가 비어있어야 삭제 가능
os.rmdir('temp/test')

# os.remove: 파일 제거
# 임시로 파일 생성
with open("temp/test.txt", 'w') as f:
    f.write("test")
os.remove("temp/test.txt")

# os.rename(src, dst): src라는 파일의 이름을 dst라는 이름으로 바꾼다.
# 임시 파일 생성
with open("temp/src", 'w') as f:
    f.write("test")
os.rename("temp/src", "temp/dst")

# zipfile: 여러개의 파일을 zip형식으로 합치거나 이를 해제할 때 사용
import zipfile

# a.txt, b.txt, c.txt 세개의 임시 파일 생성
for name in ['a', 'b', 'c']:
    with open(f"temp/{name}.txt", 'w') as f:
        f.write(name)

# # zip 파일 생성
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

# 파일 압축하여 묶고싶은 경우 compression, compresslevel 옵션 사용 가능
with zipfile.ZipFile('temp/abc_compressed.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as zip:
    zip.write('temp/a.txt')
    zip.write('temp/b.txt')
    zip.write('temp/c.txt')
# compresslevel: 압축 수준, 1~9 사용 -> 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도가 가장 느리지만 압축률이 높다
# compression
# ZIP_STORED: 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
# ZIP_DEFLATED: 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성이 좋다).
# ZIP_BZIP2: bzip2 압축으로 압축률이 높고 속도가 느리다.
# ZIP_LZMA: lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다)

# threading
import threading
# 예제: 5초의 시간이 걸리는 함수 5회 실행 하는 상황
def long_task(num):
    for i in range(5):
        time.sleep(1)
        print(f"working:{num}-{i}\n")

# 직렬 실행
# print('Start')
# for i in range(5):
#     long_task(i)
# print('End')
# 실행결과: 총 25초 소요, 0-0 ~ 4-4 까지 순서대로 실행
# Start
# working:0-0
# working:0-1
# working:0-2
# ...
# End

# threading.Thread(target=함수, args=(인수,), kwargs={"이름": 값})
# target에는 함수를 호출한 결과가 아니라 함수 자체(함수 객체)를 넘긴다.
# target=long_task   -> 함수 객체를 넘긴다(올바름)
# target=long_task() -> 지금 당장 실행되고 반환값(None)이 target에 들어간다(잘못됨)
# Thread 객체는 만들어 두기만 하고, 실제 호출은 t.start()를 부를 때 별도 스레드에서 일어난다.
# 함수에 넘길 인수는 target에 같이 쓸 수 없고 args나 kwargs로 따로 전달한다.
# args=(3,)          -> long_task(3)
# kwargs={"num": 3}  -> long_task(num=3)
# 주의: 요소가 하나인 튜플은 args=(i,)처럼 뒤에 쉼표가 필요하다. (i)는 튜플이 아니라 그냥 정수다.
#       쉼표를 빠뜨리면 TypeError: 'int' object is not iterable 이 발생한다.
# lambda로 넘길 때의 함정
# t = threading.Thread(target=lambda: long_task(i))
# lambda 안의 i는 정의 시점이 아니라 실행 시점에 값을 읽는다.
# 스레드는 반복문이 끝난 뒤에 시작되므로 5개 스레드가 모두 마지막 값인 4를 쓰게 된다.
# 굳이 lambda를 쓰려면 기본값으로 값을 붙잡아 둬야 한다. 기본값은 정의 시점에 평가되기 때문.
# t = threading.Thread(target=lambda i=i: long_task(i))
# 인수가 복잡하면 functools.partial(long_task, i)를 넘겨도 된다.
# 그냥 args=(i,)를 쓰는 것이 가장 안전하고 읽기도 좋다.

# 스레드 사용
# print("Start")
# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task, args=(i,)) # 스레드 생성
#     threads.append(t)
# for t in threads:
#     t.start() # 스레드 실행
# print("End")
# 실행 결과: 약 5 소요, 실행 순서는 보장되지 않음
# Start, End가 먼저 호출되고 long_task들이 실행됨
# Start
# End
# working:1-0
# working:0-0
# working:2-0
# ...

# 스레드 사용 + 대기
# print("Start")
# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task, args=(i,)) # 스레드 생성
#     threads.append(t)
# for t in threads:
#     t.start() # 스레드 실행
# for t in threads:
#     t.join() # join으로 스레드 종료까지 대기
# print("End")
# 실행 결과: 약 5초 소요, 실행 순서 보장되지 않음
# Start -> task -> End 순으로 작업 완료 대기
# Start
# working:1-0
# working:2-0
# working:0-0
# ...
# End
# join()은 총 실행 시간이 아니라 End가 출력되는 순서만 바꾼다.
#   join() 있음: End가 맨 마지막(5초 후)에 출력
#   join() 없음: End가 먼저 출력되고, 스레드가 끝나는 5초 후에 프로그램 종료
# 즉 join()이 없어도 작업 자체는 끝까지 수행된다.

# 데몬 스레드
# 기본값은 daemon = False이며, 이 경우 메인 스레드가 마지막 줄에 도달해도 인터프리터가 바로 끝나지 않고
# 살아 있는 스레드를 모두 기다린 뒤 종료한다.
# t.daemon = True로 두면 메인 스레드가 끝나는 순간 스레드가 강제로 잘리며 프로그램이 즉시 종료된다.
#   -> 작업이 중간에 끊겨도 되는 백그라운드 감시용 스레드나, 무한 루프 스레드에 사용한다.

# tempfile: 임시 파일을 만들어 사용하기 위한 모듈
import tempfile
# tempfile.mkstemp: 중복되지 않는 임시 파일을 만들고 (파일 디스크립터, 파일 경로) 형태의 튜플로 반환
fd, path = tempfile.mkstemp()
print(path) # /var/folders/8n/529r5bmd4yq54qfq6pdqy6fh0000gn/T/tmpzb9rofk8

# tempfile.TemporaryFile(): 
# 임시 저장 공간으로 사용할 파일 객체 반환
# 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# close()가 호출되면 이 파일은 자동으로 삭제된다.
f = tempfile.TemporaryFile()
f.close()

# traceback: 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈
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
# 실행 결과
# 오류가 발생했습니다.
# Traceback (most recent call last):
#   File "/Users/yjc/Workspace/Python-dev-notes/Chapter5/Source/advanced/standard_library.py", line 448, in main
#     b()
#     ~^^
#   File "/Users/yjc/Workspace/Python-dev-notes/Chapter5/Source/advanced/standard_library.py", line 445, in b
#     a()
#     ~^^
#   File "/Users/yjc/Workspace/Python-dev-notes/Chapter5/Source/advanced/standard_library.py", line 443, in a
#     return 1/0
#            ~^~
# ZeroDivisionError: division by zero

# json: JSON 데이터를 쉽게 처리하고자 사용하는 모듈
import json
# json.dump: 파이썬 자료형을 JSON으로 변환하여 파일에 작성
data = {"name":"홍길동", "birth":"0525", "age": 30}
with open('temp/info.json', 'w') as f:
    json.dump(data, f)

# json.load: 데이터를 딕셔너리 자료형으로 반환
with open('temp/info.json') as f:
    data = json.load(f)
print(type(data)) # <class 'dict'>
print(data) # {'name': '홍길동', 'birth': '0525', 'age': 30}

# json.dumps: 파이썬 자료형을 JSON 문자열로 변환
data = {"name":"홍길동", "birth":"0525", "age": 30}
json_data = json.dumps(data)
print(json_data) # {"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30}: 한글이 코드로 보임
# 한글이 코드로 변환되는것을 방지 하는것도 가능
json_data2 = json.dumps(data, ensure_ascii=False) # ensure_ascii=False: 데이터를 아스키 형태로 변환하지 않겠다는 뜻
print(json_data2) # {"name": "홍길동", "birth": "0525", "age": 30}
# JSON을 보기좋게 정렬 하려면
json_data3 = json.dumps(data, indent=2, ensure_ascii=False)
print(json_data3)
# {
#   "name": "홍길동",
#   "birth": "0525",
#   "age": 30
# }
# 딕셔너리 외에 리스트나 튜블같은 자료형도 JSON 변환 가능
print(json.dumps([1,2,3])) # [1, 2, 3]
print(json.dumps((4,5,6))) # [4, 5, 6]

# json.loads: JSON 문자열 딕셔너리로 변환
result = json.loads(json_data)
print(result) # {'name': '홍길동', 'birth': '0525', 'age': 30}

# urllib: URL을 읽고 분석할 때 사용하는 모듈
import urllib.request
# 페이지를 받아서 html 조회, 다운로드 후 파일로 쓰기
import gzip
def get_page(url, filename):
    with urllib.request.urlopen(url) as s: # 해당 URL에 접근해서 내용 다운로드
        data = s.read() # bytes를 반환한다
        # 일부 사이트는 요청하지 않아도 gzip으로 압축해서 응답한다(www.python.org 등).
        # urllib은 압축을 자동으로 풀어주지 않으므로 그대로 저장하면 사람이 읽을 수 없는 파일이 된다.
        # 응답 헤더의 Content-Encoding을 확인해서 gzip이면 직접 풀어준다.
        if s.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(data) # 압축을 풀어 원래 bytes로 되돌린다
    with open('temp/%s' % filename, 'wb') as f: # 다운로드 받은 내용을 파일에 저장
        f.write(data) # data는 bytes이므로 파일도 'wb'로 열어야 한다

get_page('https://www.python.org/', 'python_org.html')

# urllib.request.Request(url, data=None, headers={}, method=None)
# 위처럼 urlopen에 URL 문자열을 바로 넣으면 요청 헤더를 지정할 수 없다.
# 헤더를 붙이려면 Request 객체를 만들어 urlopen에 넘긴다.
def get_page_with_request(url, filename, headers):
    request = urllib.request.Request(url, headers=headers) # 요청 정보를 담은 객체를 만든다
    with urllib.request.urlopen(request) as s: # 문자열 대신 Request 객체를 넘긴다
        data = s.read()
        if s.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(data)
    with open('temp/%s' % filename, 'wb') as f:
        f.write(data)

# User-Agent를 지정해서 브라우저인 척한다. 지정하지 않으면 Python-urllib/3.x로 요청된다.
headers = {'User-Agent': 'Mozilla/5.0'}
get_page_with_request('https://www.python.org/', 'python_org_ua.html', headers)

# Request 객체에 담긴 요청 정보 확인하기
request = urllib.request.Request('https://www.python.org/', headers=headers)
print(request.full_url) # https://www.python.org/
print(request.headers) # {'User-agent': 'Mozilla/5.0'} -> 키의 첫 글자만 대문자로 정규화된다
print(request.get_header('User-agent')) # Mozilla/5.0
print(request.get_method()) # GET -> data를 넘기면 POST가 된다

# webbrowser: 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용
import webbrowser
# 새창 열기
webbrowser.open_new('http://python.org')
# 이미 열려있는 브라우저로 열기
webbrowser.open('http://python.org')
