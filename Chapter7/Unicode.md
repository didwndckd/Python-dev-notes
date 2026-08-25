# 파이썬과 유니코드(unicode)

> 예제 코드: [Source/unicode.py](Source/unicode.py)

- [문자 셋과 아스키코드](#문자-셋과-아스키코드)
- [유니코드](#유니코드)
- [유니코드 문자열과 바이트 문자열](#유니코드-문자열과-바이트-문자열)
- [인코딩하기](#인코딩하기)
- [디코딩하기](#디코딩하기)
- [입출력과 인코딩](#입출력과-인코딩)
- [소스 코드의 인코딩](#소스-코드의-인코딩)

## 문자 셋과 아스키코드

컴퓨터는 숫자로 데이터를 처리하므로 문자를 다루려면 문자와 숫자를 대응시키는 문자 셋(character set)이 필요하다. 아스키(ASCII)는 영문 대소문자, 숫자, 특수문자 등을 포함한 128개 문자를 정의한 초기 표준 문자 셋이다.

```python
print(ord('A'))   # 65
print(chr(65))    # A
```

`ord()`는 문자에 대응하는 유니코드 코드 포인트를, `chr()`는 코드 포인트에 대응하는 문자를 반환한다. 아스키는 영어권 문자 표현에는 충분하지만 한글·한자 같은 문자는 표현할 수 없다.

## 유니코드

유니코드(Unicode)는 전 세계 문자를 하나의 문자 셋으로 정의한 표준이다. 한글, 중국어, 이모지 등도 하나의 문자열 안에서 함께 다룰 수 있다.

파이썬 3부터 `str` 타입의 모든 문자열은 유니코드 문자열이다.

```python
text = "Hello 안녕하세요 こんにちは 你好 😀"
print(type(text))   # <class 'str'>
```

> 유니코드는 문자에 번호를 매기는 약속이고, 인코딩은 그 번호를 실제 바이트로 저장하는 방법이다.

## 유니코드 문자열과 바이트 문자열

프로그램 안에서는 유니코드 문자열을 사용하지만, 파일에 저장하거나 네트워크로 전송할 때는 바이트 문자열이 필요하다. 유니코드 문자열을 바이트 문자열로 바꾸는 과정을 인코딩, 반대 과정을 디코딩이라고 한다.

```python
유니코드_문자열.encode('인코딩_방식')
바이트_문자열.decode('인코딩_방식')
```

```python
text = "Life is too short"
encoded_text = text.encode('utf-8')

print(encoded_text)         # b'Life is too short'
print(type(encoded_text))   # <class 'bytes'>
```

바이트 문자열 앞의 `b`는 `bytes` 타입임을 나타낸다.

## 인코딩하기

`str.encode()`에 인코딩 방식을 전달하면 유니코드 문자열을 바이트 문자열로 변환한다. 보통은 UTF-8을 사용하며, 기존 시스템의 형식에 따라 EUC-KR 등을 쓸 수도 있다.

```python
korean_text = "한글"

print(korean_text.encode('euc-kr'))   # b'\xc7\xd1\xb1\xdb'
print(korean_text.encode('utf-8'))    # b'\xed\x95\x9c\xea\xb8\x80'
```

같은 문자열도 인코딩 방식에 따라 서로 다른 바이트열이 된다. `\x` 뒤의 두 자리는 한 바이트를 16진수로 표현한 값이다.

```python
korean_text = "한글"
# korean_text.encode('ascii')   # UnicodeEncodeError
```

아스키는 한글을 포함하지 않으므로 한글을 `ascii`로 인코딩할 수 없다.

## 디코딩하기

`bytes.decode()`는 바이트 문자열을 유니코드 문자열로 변환한다. 인코딩할 때와 같은 방식을 지정해야 원래 문자열을 올바르게 복원할 수 있다.

```python
korean_text = "한글"
encoded_korean_text = korean_text.encode('euc-kr')
decoded_korean_text = encoded_korean_text.decode('euc-kr')

print(decoded_korean_text)   # 한글
```

```python
# encoded_korean_text.decode('utf-8')   # UnicodeDecodeError
```

> 인코딩 방식을 모르는 바이트 데이터는 올바르게 디코딩할 수 없다. 저장하거나 전송할 때 사용한 인코딩을 함께 알아야 한다.

## 입출력과 인코딩

파일을 읽고 쓸 때 `open()`의 `encoding` 인수로 파일의 인코딩을 지정한다. 프로그램 내부에서는 문자열을 유니코드로 유지하고, 파일이나 네트워크처럼 외부와 데이터를 주고받는 지점에서만 인코딩·디코딩하는 것이 원칙이다.

```python
import pathlib

directory_path = 'temp/unicode'
pathlib.Path(directory_path).mkdir(exist_ok=True)

euc_kr_path = f"{directory_path}/euc_kr.txt"

with open(euc_kr_path, 'w', encoding='euc-kr') as f:
    f.write("test")

with open(euc_kr_path, encoding='euc-kr') as f:
    data = f.read()
    print(data)   # test

data += "\n" + "test line 2"

with open(euc_kr_path, 'a', encoding='euc-kr') as f:
    f.write(data)

with open(euc_kr_path, encoding='euc-kr') as f:
    data = f.read()
    print(data)
    # testtest
    # test line 2
```

`'a'` 모드는 파일 끝에 내용을 덧붙인다. 기존 내용을 수정해서 다시 저장하려면 `'w'` 모드를 사용한다.

> `encoding`을 생략하면 파이썬 3의 기본값인 UTF-8을 사용한다. 다른 인코딩으로 만든 파일을 읽을 때는 반드시 실제 파일의 인코딩을 지정한다.

## 소스 코드의 인코딩

소스 코드 파일도 바이트로 저장되므로 인코딩 방식이 있다. 파이썬 3은 UTF-8을 기본으로 사용하므로 UTF-8 파일이라면 별도 선언이 필요 없다.

```python
# -*- coding: utf-8 -*-
```

EUC-KR처럼 UTF-8이 아닌 방식으로 저장한 소스 파일은 첫째 또는 둘째 줄에 다음처럼 선언한다.

```python
# -*- coding: euc-kr -*-
```

소스 파일의 실제 인코딩과 선언한 인코딩이 다르면 문자열을 처리할 때 오류가 발생할 수 있다.
