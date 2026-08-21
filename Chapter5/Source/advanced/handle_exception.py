# handle_expectation.py

# 오류는 언제 발생 하는가?
# 존재하지 않는 파일 열기
# f = open("없는파일", 'r')
# 실행 결과
# Traceback (most recent call last):
#   File "/Users/yjc/Workspace/Python-dev-notes/Source/handle_expectation.py", line 4, in <module>
#     f = open("없는파일", 'r')
#         ~~~~^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: '없는파일'

# 0으로 나누기
# 4 / 0
# 실행 결과
# Traceback (most recent call last):
#   File "/Users/yjc/Workspace/Python-dev-notes/Source/handle_expectation.py", line 14, in <module>
#     4 / 0
#     ~~^~~
# ZeroDivisionError: division by zero

# 인덱스 아웃
# a = [1, 2, 3]
# a[3]
# 실행 결과
# Traceback (most recent call last):
#   File "/Users/yjc/Workspace/Python-dev-notes/Source/handle_expectation.py", line 24, in <module>
#     a[3]
#     ~^^^
# IndexError: list index out of range

# 오류 예외 처리 기법
# try-except 문
# try:
#   ...
# except [발생오류 [as 오류 변수]]:
#   ...
# try 블록 수행중 오류가 발생하면 except 블록이 실행된다.

# except 구문
# except [발생오류 [as 오류변수]]:
# 위 구문에서 []는 괄호 안의 내용을 생략할 수 있다는 관례적 표기법이다.
# 즉 except 구문은 다음과 같이 쓸 수 있다.

# try-except만 쓰는 방법
# try:
#   ...
# except:
#   ...

# 발생 오류만 포함한 except문
# try:
#   ...
# except 발생오류:
#   ...

# 발생 오류와 오류 변수까지 포함한 except 문
# try:
#   ...
# except 발생오류 as 오류변수:
#   ...

# 실 예시 코드
try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

# try-finally 문
# try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
try:
    f = open('temp/foo.txt', 'w')
    # code
finally:
    f.close() # 중간에 오류가 발생 하더라도 무조건 실행된다.

try:
    print("나누기 전")
    4 / 0
    print("나누기 후")
except ZeroDivisionError:
    print("오류가 발생했습니다.")
finally:
    print("finally 실행!")
# 실행결과
# 나누기 전
# 오류가 발생했습니다.
# finally 실행!

# 여러 개의 오류 처리하기
# try:
#   ...
# except 발생오류1:
#   ...
# except 발생오류2:
#   ...

try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
# 실행결과
# 인덱싱 할 수 없습니다.

try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# 실행결과
# list index out of range

# 다음과같이 여러 에러를 함께 처리할 수도 있다.
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 실행결과
# list index out of range

# try-else 구문
# try:
#   ...
# except [발생오류 [as 오류변수]]:
#   ...
# else: # 오류가 없을 경우에만 수행
#   ...
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
# 실행결과 1: 정상 처리
# 나이를 입력하세요: 30
# 환영합니다.
# 실행결과 2: 입력 오류
# 나이를 입력하세요: ㅁㅁ
# 입력이 정확하지 않습니다.
# 실행결과 3: 입력 오류는 아니지만 예외 처리
# 나이를 입력하세요: 10
# 미성년자는 출입금지입니다.

# 오류 회피하기
students = ["김철수", "이영희", "박민수", "최유진"]
for student in students:
    try:
        with open(f"{student}_성적.txt", 'r') as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue # 다음 학생으로 넘어감
# 실행결과
# 김철수의 성적 파일이 없습니다. 건너뜁니다.
# 이영희의 성적 파일이 없습니다. 건너뜁니다.
# 박민수의 성적 파일이 없습니다. 건너뜁니다.
# 최유진의 성적 파일이 없습니다. 건너뜁니다.

try:
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass # 설정 파일이 없어도 계속 진행
# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")
# 실행결과
# 프로그램이 정상적으로 실행됩니다.

# 오류 일부러 발생시키기
# 예시 Bird의 자식 클래스의 fly 함수 구현을 강제하고 싶다.
class Bird:
    def fly(self):
        raise NotImplementedError # 파이썬에 이미 정의되어 있는 오류임

class Eagle(Bird):
    pass
eagle = Eagle()
# eagle.fly() # NotImplementedError 발생

class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly() # very fast

# 예외 만들기: Exception을 상속받는 class
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보': raise MyError()
    print(nick)

try:
    say_nick('천사') # 천사
    say_nick('바보') # MyError 발생
except MyError as e:
    print(e) # 아무것도 안나옴

# 오류 내용을 출력하고싶으면 __str__을 구현해야 한다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick('천사') # 천사
    say_nick('바보') # MyError 발생
except MyError as e:
    print(e) # 허용되지 않는 별명입니다.