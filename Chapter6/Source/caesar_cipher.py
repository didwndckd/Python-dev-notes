# 시저 암호 만들기
# 시저 암호: 알파벳을 일정한 수만큼 밀어서 다른 글자로 바꾸는것.
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z (원본)
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C (3칸)

# ord(): 문자 -> 숫자
print(ord('A')) # 65

# chr(): 숫자 -> 문자
print(chr(65)) # A
print(chr(65 + 3)) # D

# 65 ~ 90: 
print(ord('A')) # 65
print(ord('Z')) # 90

class Caesar_Cipherer:
    def __init__(self, key):
        self.key = key

    # 암호화 결과 반환
    def excute(self, word):
        result = ""
        for char in word:
            result += self.cipher(char)
        return result

    # 문자 하나를 암호화 해서 반환
    def cipher(self, char):
        code = ord(char)
        return chr(code + self.key)

cipher = Caesar_Cipherer(3)
result = cipher.excute('PYTHON')
print(result) # S\WKRQ: Y가 3 밀리면서 알파벳 범위를 벗어나 \로 바뀜

# 보완된 암호화 클래스
class Caesar_Cipherer_V2(Caesar_Cipherer):
    def cipher(self, char):
        code_A = ord('A')
        num = ord(char) - code_A # 0~25 숫자로 변환
        shiffted = (num + self.key) % 26 # key만큼 밀고 알파벳 갯수(26)으로 나눈 나머지
        result = chr(shiffted + code_A) # 문자로 변환, 실제 A값 + shiffted
        return result

cipher = Caesar_Cipherer_V2(3)
result = cipher.excute('PYTHON')
print(result) # SBWKRQ: 보완 되어 \가 B로 나옴

# 알파벳 전수 검사
cipher = Caesar_Cipherer_V2(1)
result = cipher.excute('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(result) # BCDEFGHIJKLMNOPQRSTUVWXYZA