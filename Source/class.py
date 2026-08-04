# 클래스 작성
# class 클래스_이름:
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num): # class의 함수에는 self를 명시적으로 넣어야 한다.(인스턴스 메서드 기준)
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10

# 왜 함수 선언에는 self가 있는데 호출부에서는 self를 넣지 않아도 되는걸까
cal1.add(1) # <- 자동으로 cal1이 self부분에 들어간것
Calculator.add(cal1, 1) # 위 코드와 동일함. 여기서 cal1을 넣어주는 부분이 cal1.add(1)로 호출할때는 자동으로 들어간것.


# 비어있는 클래스 만들기
class Cookie:
    pass
a = Cookie()

# 클래스 내에 선언하지 않은 변수도 할당하고 사용 가능.
a.some_number = 1
a.some_str = "python"
print(a.some_number) # 1
print(a.some_str) # python

# 사칙연산 클래스 만들기
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
# setdata 호출 전에는 first, second를 할당한적이 없기에 접근 시 에러 발생
# print(cal.first) # 4
# print(cal.second) # 2
# print(cal.add())
cal.setdata(4, 2)
print(cal.first) # 4
print(cal.second) # 2
print(cal.add()) # 6
print(cal.sub()) # 2
print(cal.mul()) # 8
print(cal.div()) # 2.0

# 생성자: 객체 생성 시점에 자동으로 호출되는 함수
# def __init__(self, 매개변수1, 매개변수2, ...)
class FourCal:
    def __init__(self, first, second): # 생성자 추가
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

# cal = FourCal() # first, second를 넣어주지 않아 에러 발생
cal = FourCal(4, 2)
print(cal.first) # 4
print(cal.second) # 2
print(cal.add()) # 6
print(cal.sub()) # 2
print(cal.mul()) # 8
print(cal.div()) # 2.0

# 클래스의 상속
# class 클래스_이름(상속할_클래스_이름)
class MoreFourCal(FourCal):
    def pow(self):
        """
        first^second: first의second제곱
        """
        return self.first ** self.second

    # 메서드 오버라이딩: 부모의 메서드를 동일한 이름으로 다시 만드는것
    def div(self):
        """
        부모에는 없는 second(나누는 숫자)가 0인 경우의 예외 처리를 추가
        """
        if self.second == 0: return 0
        return self.first / self.second

# 부모인 FourCal의 모든 기능을 사용 가능
cal = MoreFourCal(4, 2)
print(cal.first) # 4
print(cal.second) # 2
print(cal.add()) # 6
print(cal.sub()) # 2
print(cal.mul()) # 8
print(cal.div()) # 2.0
print(cal.pow()) # 4의 제곱 = 16

cal = MoreFourCal(4, 0)
print(cal.div()) # 0, 나누는 숫자가 0이므로 예외처리하여 0이 나옴


# 클래스 변수
class Family:
    lastname = "양"

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname) # 양
print(b.lastname) # 양

Family.lastname = "박"
print(a.lastname) # 박
print(b.lastname) # 박

a.lastname = "김" # 이건 인스턴스 변수 할당임
print(a.lastname) # 김
print(b.lastname) # 박
print(Family.lastname) # 박