# 문자열 소비가 없는 메타 문자.
# 전에 학습한 +, *, [], {} 같은 메타 문자들은 매치되면 해당 문자들을 "사용해보린다"고 생각하면 된다. 더 자세히 표현하자면 문자열을 읽는 위치(커서)가 매치된만큼 앞으로 이동한다는 뜻.
# 예를 들어 "aac"라는 문자열에서 a+패턴을 찾으면 "aa"부분이 매치되고, 읽는 위치가 "aa" 뒤로 이동하여 그다음부터 남은 "c"에서 다시 탐색을 시작한다.
# 하지만 이번에 학습할 메타문자들은 조건만 확인 하고 실제로는 읽는 위치를 이동시키지 않는 성질을 가졌다.

import re

# |: or과 동일한 의미로 사용.
# ex) A|B: A또는 B
p = re.compile("Crow|Servo")
m = p.match("CrowHello")
print(m) # <re.Match object; span=(0, 4), match='Crow'>

m = p.findall("CrowServo")
print(m) # ['Crow', 'Servo']

# ^: 맨 처음과 일치한다는것을 의미, 컴파일옵션 re.MULTILINE을 사용할 경우 여러줄의 문자열일 때 각 줄의 처음과 일치
s = re.search("^Life", "Life is too short")
print(s) # <re.Match object; span=(0, 4), match='Life'>

s = re.search("^Life", "MY Life")
print(s) # None

# $: ^ 메타문자와 반대로 문자열의 끝과 매치한다는것을 의미
s = re.search("short$", "Life is too short")
print(s) # <re.Match object; span=(12, 17), match='short'>

s = re.search("short$", "Life is too short, you need python")
print(s) # None

# \A: 문자열의 처음과 매치된다는것을 의미, ^ 메타문자와 동일한 의미이지만, re.MULTILINE 옵션을 사용하더라도 줄과 상관없이 문자열 전체의 처음하고만 매치된다.
data = """python one
life is too short
python two
you need python
python three"""

p = re.compile(r"^python", re.MULTILINE) # ^의 경우
f = p.findall(data)
print(f) # ['python', 'python', 'python']

p = re.compile(r"\Apython", re.MULTILINE) # \A의 경우
f = p.findall(data)
print(f) # ['python']

# \Z: 문자열의 끝과 매치된다는것을 의미, \A와 동일하게 re.MULTILINE옵션을 사용하더라도 문자열 전체의 끝만 매치된다.

data = """python one
life is too short
python two
you need python
python three
four python"""

p = re.compile(r"python$", re.MULTILINE) # ^의 경우
f = p.findall(data)
print(f) # []'python', 'python']

p = re.compile(r"python\Z", re.MULTILINE) # \Z의 경우
f = p.findall(data)
print(f) # ['python']

# \b: 단어 구분자(word boundary). 보통 단어는 화이트스페이스에 의해 구분됨

p = re.compile(r"\bclass\b") # class의 앞뒤에 화이트 스페이스가 있어야 매치
s = p.search("no class at all")
print(s) # <re.Match object; span=(3, 8), match='class'>

s = p.search("the declassified algorithm") # declassified에 class는 있지만 앞뒤로 화이트 스페이스가 없음
print(s) # None

s = p.search("one subclass is") # subclass class는 있지만 뒤에만 화이트 스페이스가 있음
print(s) # None

s = p.search("class") # class만 있는 경우 앞 뒤로 화이트스페이스가 붙는듯
print(s) # <re.Match object; span=(0, 5), match='class'>

# \B: \b와 반대로 화이트 스페이스로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r"\Bclass\B") # class 앞뒤로 화이트 스페이스가 아닌 다른 문자가 있어야함
s = p.search("no class at all")
print(s) # None

s = p.search("the declassified algorithm")
print(s) # <re.Match object; span=(6, 11), match='class'>

s = p.search("one subclass is")
print(s) # None

s = p.search("class")
print(s) # None

# () 그루핑: 목적은 크게 두가지
# 1. 여러 문자를 하나로 묶어서 반복 처리하기 위해
# 2. 매치된 문자열에서 원하는 부분만 추출

# 여러 문자를 하나로 묶어서 반복 처리하기
# ABC라는 세글자가 하나의 단위로 취급되어 ABC가 한번 이상 반복되는 패턴을 찾는 케이스
p = re.compile("(ABC)+")
m = p.match("ABCABCABC OK?")
print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group()) # ABCABCABC

# 매치된 문자열에서 특정 부분만 추출
# 정규식에 그룹 지정: 그루핑 하고싶은 부분을 ()로 감싼다.
# 지정된 그룹 꺼내오기: group(n) -> n번째 그룹을 꺼내온다, 0은 매치된 전체 문자열, 1부터 그룹 시작
# r"\w+\s+\d+[-]\d+[-]\d+": 이름 + 공백 + 전화번호

# 이름만 그루핑
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+") # 맨 앞 이름에 해당하는 \w+만 그루핑 한 케이스
m = p.match("yjc 010-1234-1234")
print(m.group(0)) # yjc 010-1234-1234
print(m.group(1)) # yjc

# 이름, 전화번호 그루핑
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)") # 맨 앞 이름에 해당하는 \w+, 전화번호에 해당하는 \d+[-]\d+[-]\d+에 그루핑
m = p.match("yjc 010-1234-1234")
print(m.group(0)) # yjc 010-1234-1234
print(m.group(1)) # yjc
print(m.group(2)) # 010-1234-1234

# 이름, 전화번호, 국번 그루핑(중첩)
# 그루핑 안에 그루핑이 중첩된 경우 순서는 바깥부터 시작해 안으로 들어갈수록 인덱스 값이 증가함
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)") # 맨 앞 이름에 해당하는 \w+, 전화번호에 해당하는 \d+[-]\d+[-]\d+에 그루핑, 전화번호 안에 국번에 해당하는 첫번째 \d+ 그루핑
m = p.match("yjc 010-1234-1234")
print(m.group(0)) # yjc 010-1234-1234
print(m.group(1)) # yjc
print(m.group(2)) # 010-1234-1234
print(m.group(3)) # 010

# 그룹 인덱스 순서는 왼쪽에서부터 오른쪽으로 가면서 (를 만나면 즉시 번호를 붙인다.
# 그룹1 그룹2(그룹3-그룹아님-그룹아님) 그룹4
p = re.compile(r"(\w+)\s+([(](\w+)[-]\w+[-]\w+[)])\s+(\w+)")
m = p.match("그룹1 (그룹3-그룹아님-그룹아님) 그룹4")
print(m.group(0)) # 그룹1 (그룹3-그룹아님-그룹아님) 그룹4
print(m.group(1)) # 그룹1
print(m.group(2)) # (그룹3-그룹아님-그룹아님)
print(m.group(3)) # 그룹3
print(m.group(4)) # 그룹4

# \n: 그루핑된 문자열 재참조하기 
p = re.compile(r"(\b\w+)\s+\1") # (그룹) + " " + 그룹과 동일한 단어(\1)
s = p.search("Paris in the the spring")
print(s.group()) # the the
# 위 예제의 단계
# 1. (\b\w+)가 "Paris"와 매치되어 그룹 1에 "Paris"가 저장됨
# 2. \s+가 공백과 매치
# 3. \1이 그룹 1의 값인 "Paris"를 참조하여 다음 단어와 비교하지만 "in"이므로 매치 실패
# 4. 같은 방식으로 "in", "the"를 처리
# 5. (\b\w+)가 "the"와 매치되어 그룹1에 "the"가 저장되고, \s+뒤의 \1이 다음 단어 "the"와 일치하므로 최종 매치가 성공
# 두번째 그룹을 참조 하려면 \2를 사용하면 된다.

# (?P<그룹이름>) 그루핑된 문자열에 이름 붙이기: 인덱스가 아닌 이름으로 접근 가능
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = p.match("yjc 010-1234-1234")
print(m.group("name")) # yjc
print(m.group("phone")) # 010-1234-1234

# (?P=그룹이름) 그룹 이름 재참조
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
s = p.search("Pairs in the the spring")
print(s.group()) # the the

# 전방 탐색

# (?=매치문자) 긍정형 전방탐색: 뒤에 "매치문자"가 오는지 탐색 하되 결과에는 포함하지 않는다.
# 예제: http:로 시작하는지 체크 하고 매치 결과는 http만 가져오고 싶은 경우

# 전방 탐색을 사용하지 않은 경우
p = re.compile(".+:") # 한글자 이상의 문자 + :
m = p.match("http://google.com")
print(m.group()) # http:

# 긍정형 전방탐색을 사용한 경우
p = re.compile(".+(?=:)")
m = p.match("http://google.com")
print(m.group()) # http

# (!=매치문자) 부정형 전방탐색: 뒤에 "매치문자"가 오지않는지 탐색 하되 결과에는 포함하지 않는다.
# 예제: 아래 files에서 .bat을 제외하고싶은 경우
files = ["foo.bar", "autoexec.bat", "sendmail.cf"]

# 파일 리스트를 받아서 정규식에 매치되는 파일명만 반환.
def filter_matched(files: list[str], regex: str) -> list[str]:
    result = []
    p = re.compile(regex)
    for file in files:
        m = p.match(file) 
        if m: result.append(m.group())
    return result

# 모든 파일 매치
result = filter_matched(files, ".*[.].*$")
print(result) # ['foo.bar', 'autoexec.bat', 'sendmail.cf']

# b로 시작하지않는 확장자 매치
result = filter_matched(files, ".*[.][^b].*$")
print(result) # ['sendmail.cf']: b로 시작하는 확장자 foo.bar까지 미매치 -> 실패

# 첫글자가 b이거나 두번째가 a이거나 세번째가 t이거나 하는 케이스 배제
result = filter_matched(files, ".*[.]([^b]..|.[^a].|..[^t])$")
print(result) # ['foo.bar']: 확장자가 두글자인 sendmail.cf까지 미매치 -> 실패

# 두글자까지 처리
result = filter_matched(files, ".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
print(result) # 'foo.bar', 'sendmail.cf']: 정상처리됨, 하지만 이후 .exe 파일도 제외하라는 요구사항이 들어온다면? 너무 복잡해진다.

# 부정형 전방탐색 사용시
result = filter_matched(files, ".*[.](?!bat$).*$")
print(result) # ['foo.bar', 'sendmail.cf']: 정상 처리

# 부정형 전방탐색 여러개: bat, exe 제외 예시
files.append("foo.exe") # 예시를 위해 exe 파일 추가
result = filter_matched(files, ".*[.](?!bat$|exe$).*$")
print(result) # ['foo.bar', 'sendmail.cf']: 정상 처리

# 문자열 바꾸기
# sub: sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있음
p = re.compile("blue|white|red")
result = p.sub('colour', 'blue socks and red shoes')
print(result) # colour socks and colour shoes: blue, red -> colour로 변경

result = p.sub('colour', 'blue socks and red shoes', count=1) # 가장 먼저 만나는 한개만 변경
print(result) # colour socks and red shoes -> 맨앞의 blue만 변경

# sub와 유사한 subn: sub와 동일한 기능을 하지만 (변경된 문자열, 변경 횟수) 형태의 튜플로 반환함
result = p.subn('colour', 'blue socks and red shoes')
print(result) # ('colour socks and colour shoes', 2)

# sub 사용 시 참조 구문 사용
# 그룹 참조 이름 사용
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
result = p.sub(r"\g<phone> \g<name>", "yjc 010-1234-1234")
print(result) # 010-1234-1234 yjc

# 그룹 참조 번호
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
result = p.sub(r"\g<2> \g<1>", "yjc 010-1234-1234")
print(result) # 010-1234-1234 yjc

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
result = p.sub(hexrepl, "Call 65490 for printing, 49152 for user code.")
print(result) # Call 0xffd2 for printing, 0xc000 for user code.
# 동작 흐름
# 1. \d+ 패턴이 "65490"과 매치 -> hexrpl 함수에 match객체 전달 -> hex(65490) 반환 -> 0xffd2로 교체
# 2. \d+ 패턴이 "49152"과 매치 -> hexrpl 함수에 match객체 전달 -> hex(49152) 반환 -> 0xc000로 교체

# greedy와 non-greedy
# 정규식에는 '탐욕스러운(greedy)'이라는 표현을 종종 쓴다.
s = "<html><head><title>Title</title>"
print(len(s)) # 32
m = re.match("<.*>", s)
print(m.span()) # (0, 32)
print(m.group()) # <html><head><title>Title</title>
# <.*>정규식의 매치 결과로 <html> 문자열을 반환하기를 기대했지만 *메타는 매우 탐욕스러워서 최대한의 문자열인 <html><head><title>Title</title> 문자열을 모두 소비해버림

# ? 탐욕을 제한하는 방법
# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용할 수 있다.
m = re.match("<.*?>", s)
print(m.span()) # (0, 6)
print(m.group()) # <html>
# ?는 단독으로 사용될 때 "0회 또는1회 반복"을 의미하지만 여기서는 *, +등 반복 메타 문자 뒤에 붙어 "최소한으로 반복하라"는 의미로 사용된다.