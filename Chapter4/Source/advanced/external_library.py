# PyPI: 파이썬 패키지 저장소
# pip: 파이썬 패키지 매니저

# 맥: python3 ~
# 윈도우: python ~

# pip install: 파이썬 패키지 설치(기본 최신 버전)
# python3 -m pip install SomePackage

# 특정 버전으로 설치
# python3 -m pip install SomePackage==1.0.4

# 최신 버전으로 업그레이드 하기
# python3 -m pip install --upgrade SomePackage

# 설치된 패키지 확인 하기
# python3 -m pip list

# pip uninstall: 파이썬 패키지 삭제
# python3 -m pip uninstall SomePackage

# 아래 내용들은 가상환경(venv)이 활성화 되어있는 상태로 가정

# Faker(테스트 데이터 만들기) 사용해보기
# python3 -m pip install Faker
from faker import Faker
fake = Faker()
print(fake.name()) # Rebecca Powell: 매번 바뀜

fake = Faker('ko-KR') # 한글로
print(fake.name()) # 강정남: 매번 바뀜

print(fake.address()) # 부산광역시 종로구 역삼04길 375

# 이름과 주소를 쌍으로 하는 30건의 데이터
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data) # [('장혜진', '울산광역시 서구 백제고분가 지하138 (미숙김황읍)'), ('송상훈', '경기도 춘천시 역삼61가 855-50'), ...]

# sympy: 방정식 기호를 사용하게 해주는 라이브러리
# python3 -m pip install sympy
import sympy
# sympy.symbols: 미지수를 나타내는 기호 생성
# x를 미지수로 생성
x = sympy.symbols("x")
# x, y를 미지수로 생성
x, y = sympy.symbols('x y')


# fractions.Fraction: 정확한 유리수 연산
from fractions import Fraction
# Fraction(분자, 분모)
print(Fraction(1, 5)) # 1/5
print(Fraction('1/5')) # 1/5

# 예제: 가진 돈의 2/5로 학용품을 샀다. 학용품을 사는데 쓴 돈이 1,760원이라면 남은돈은?
# 위 예제의 1차 방정식 x * (2/5) = 1760을 코드로 표현
f = sympy.Eq(x*Fraction('2/5'), 1760)
# symp.Eq(a, b)는 a와 b가 같다는 방정식
# Faction은 유리수를 표현할 때 사용하는 표준 라이브러리로 2/5를 정확하게 계산하기 위해 사용
result = sympy.solve(f) # 원래 가진 돈 x를 구함
print(result) # [4400]
remains = result[0] - 1760
print(remains) # 2640

# x^2 = 1과 같은 2차 방정식의 해 구하기
x = sympy.symbols('x')
f = sympy.Eq(x**2, 1)
result = sympy.solve(f)
print(result) # [-1, 1]

# 연립 방정식의 해 구하기
# x + y = 10
# x - y = 4
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
result = sympy.solve([f1, f2])
print(result) # {x: 7, y: 3}

print(x * Fraction('2/5'))



