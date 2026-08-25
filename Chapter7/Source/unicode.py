# 파이썬 버전 3부터 모든 문자열을 유니코드로 처리한다.

# 인코딩
text = "Life is too short"
encoded_text = text.encode('utf-8')
print(encoded_text) # b'Life is too short'
print(type(encoded_text)) # <class 'bytes'>

korean_text = "한글"
print(korean_text.encode('euc-kr')) # b'\xc7\xd1\xb1\xdb'
print(korean_text.encode('utf-8')) # b'\xed\x95\x9c\xea\xb8\x80'
# encoded_korean_text = korean_text.encode('ascii') # UnicodeEncodeError: 한글은 ascii로 인코딩 할 수 없음


# 디코딩
korean_text = "한글"
encoded_korean_text = korean_text.encode('euc-kr') # euc-kr로 인코딩
decoded_korean_text = encoded_korean_text.decode('euc-kr') # 동일하게 euc-kr로 디코딩
print(decoded_korean_text) # 한글

# 인코딩된것과 다른 방식으로 디코딩 하면 안된다.
# encoded_korean_text.decode('utf-8') # UnicodeDecodeError: euc-kr로 인코딩 되어있으니 euc-kr로 디코딩 해야함


# 입출력과 인코딩
import pathlib
directory_path = 'temp/unicode'
pathlib.Path(directory_path).mkdir(exist_ok=True)

# euc-kr 인코딩으로 파일을 읽고 쓰기
euc_kr_path = f"{directory_path}/euc_kr.txt"
with open(euc_kr_path, 'w', encoding='euc-kr') as f:
    f.write("test")

with open(euc_kr_path, encoding='euc-kr') as f:
    data = f.read()
    print(data)

data += "\n" + "test line 2"

with open(euc_kr_path, 'a', encoding='euc-kr') as f:
    f.write(data)

with open(euc_kr_path, encoding='euc-kr') as f:
    data = f.read()
    print(data)