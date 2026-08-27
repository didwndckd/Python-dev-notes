# 정규표현식 시작하기

# 메타 문자
# . ^ $ * + ? { } [ ] \ | ( )

import re

# [] 문자 클래스: []안에 있는 문자중 하나
# ex) [abc]: a, b, c 세개중 아무거나 하나 라는 뜻
# ex) "a", "before", "dude"가 [abc]와 어떻게 매치되는지
#   - "a": 매치됨, 문자 "a"가 [abc]안에 포함
#   - "before": 매치됨, 문자 b가 [abc]안에 포함
#   - "dude": 매치 안됨, 문자 [abc]에 포함하는게 없음

p = re.compile("[abc]")
print(p.match("a")) # <re.Match object; span=(0, 1), match='a'>
print(p.match("before")) # <re.Match object; span=(0, 1), match='b'>
print(p.match("dude")) # None

# [-] 범위 지정하기: 하이픈(-)
# []안에 -를 사용하면 범위 지정 가능
# [a-c] -> [abc]
# [0-5] -> [012345]
# [A-Z] -> 모든 대문자 알파벳, A부터 Z까지
# 자주쓰는 범위 표현
# [a-zA-Z]: 모든 알파벳
# [0-9]: 모든 숫자
# [가-힣]: 모든 한글

p = re.compile("[a-zA-Z]")
print(p.match("abAB")) # <re.Match object; span=(0, 1), match='a'>
print(p.match("123")) # None

# [^] 제외하기: ^를 앞에 쓰면 ~가 아닌 이라는 의미 즉, 해당 문자가 아닌것들과 매치된다.
# [^0-9]: 숫자가 아닌 모든 문자
# [^a-c]: a, b, c가 아닌 모든 문자
# [^A-Z]: 대문자가 아닌 모든 문자

# 자주 사용하는 문자 클래스
# \d: 숫자, [0-9]와 동일
# \D: 숫자가 아닌것, [^0-9]와 동일
# \s: 화이트 스페이스, [ \t\n\r\f\v]와 동일, 맨 앞의 빈칸은 공백
# \S: 화이트 스페이스가 아닌것, [^ \t\n\r\f\v]와 동일
# \w: 문자+숫자(alphanumeric), [a-zA-Z0-9_]와 동일
# \W: 문자+숫자(alphanumeric)가 아닌것, [^a-zA-Z0-9_]와 동일
# 대문자는 소문자의 반대인것을 추측할 수 있다.

# .(dot) 문자: \n을 제외한 모든 문자
# a.b: a와 b사이에 어떤 문자가 와도 매치된다 -> a + 모든_문자 + b
# ex) "aab", "a0b", "abc"가 a.b와 어떻게 매치 되는지
#   - "aab": a와 b 사이의 a는 모든 문자에 포함되어 매치
#   - "a0b": a와 b 사이의 0은 모든 문자에 포함되어 매치
#   - "abc": a와 b사이에 문자가 없으므로 노매치
p = re.compile("a.b")
print(p.match("aab")) # <re.Match object; span=(0, 3), match='aab'>
print(p.match("a0b")) # <re.Match object; span=(0, 3), match='a0b'>
print(p.match("abc")) # None

# * 문자: *바로 앞에있는 문자가 0~무한대까지 반복 가능하다. 즉 몇개가 있든 없든 매치된다.
# ex) ca*t 정규식 기준으로
#   - ct: a가 0번 반복되어 매치
#   - cat: a가 1번 반복되어 매치
#   - caaat: a가 3번 반복되어 매치
p = re.compile("ca*t")
print(p.match("ct")) # <re.Match object; span=(0, 2), match='ct'>
print(p.match("cat")) # <re.Match object; span=(0, 3), match='cat'>
print(p.match("caaat")) # <re.Match object; span=(0, 5), match='caaat'>

# + 문자: +바로 앞에 있는 문자가 최소 1번 이상 반복 가능하다. 즉 1개 이상 있으면 매치된다.
# ex) ca+t 정규식 기준으로: "c + a가_1번_이상_반복 + t"
#   - ct: a가 0번 반복되어 노매치
#   - cat: a가 1번 반복되어 매치
#   - caaat: a가 3번 반복되어 매치

p = re.compile("ca+t")
print(p.match("ct")) # None
print(p.match("cat")) # <re.Match object; span=(0, 3), match='cat'>
print(p.match("caaat")) # <re.Match object; span=(0, 5), match='caaat'>

# {} 문자
#   - {n}: 반드시 n번 반복
#   - {m, n}: m~n번 반복
#   - {m,}: m번 이상, {0,}은 *와 동일 / {1,}은 +와 동일
#   - {,n}: n번 이하
# ex) ca{2}t: a가 반드시 2번 반복
p = re.compile("ca{2}t")
print(p.match("cat")) # None
print(p.match("caat")) # <re.Match object; span=(0, 4), match='caat'>
print(p.match("caaat")) # None

# ex) ca{2,5}t: a를 2~5회 반복
p = re.compile("ca{2,5}t")
print(p.match("cat")) # None
print(p.match("caat")) # <re.Match object; span=(0, 4), match='caat'>
print(p.match("caaaaat")) # <re.Match object; span=(0, 7), match='caaaaat'>
print(p.match("caaaaaat")) # None

# ? 문자: {0,1}와 동일 즉, 해당 문자가 한개 있거나 없거나
p = re.compile("ca?t")
print(p.match("ct"))# <re.Match object; span=(0, 2), match='ct'>
print(p.match("cat")) # <re.Match object; span=(0, 3), match='cat'>
print(p.match("caat")) # None


# re 모듈
import re

# compile: 정규식을 빠르게 처리할 수 있는 패턴 객체 생성
p = re.compile("ab*")

# match(): 문자열의 "처음"부터 정규식과 매치되는지 확인, 인덱스 0부터 매치되어야 한다.
p = re.compile("[a-z]+")
m = p.match("python") # 매치
print(m) # <re.Match object; span=(0, 6), match='python'>
m = p.match("3 python") # 맨앞에 "3"이 있어서 노매치
print(m) # None

# search(): 문자열 전체를 검색해서 정규식과 매치되는지 조사
p = re.compile("[a-z]+")
m = p.search("python") # python이 매치
print(m) # <re.Match object; span=(0, 6), match='python'>
m = p.search("3 python") # python부분이 매치
print(m) # <re.Match object; span=(2, 8), match='python'>

# findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환
p = re.compile("[a-z]+")
result = p.findall("life is too short")
print(result) # 'life', 'is', 'too', 'short']

# finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복가능한객체(iterator)로 반환
p = re.compile("[a-z]+")
result = p.finditer("life is too short")
print(result) # <callable_iterator object at 0x108100d30>
for word in result:
    print(word)
# 실행 결과
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

# match 객체: re의 match, search, finditer를 통해 반환되는 매치 객체
# match 객체 메서드
# group()	매치된 문자열을 반환한다.
# start()	매치된 문자열의 시작 위치를 반환한다.
# end()	매치된 문자열의 끝 위치를 반환한다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환한다.

p = re.compile("[a-z]+")
m = p.match("python")
print(m.group()) # python
print(m.start()) # 0
print(m.end()) # 6
print(m.span()) # (0, 6)

m = p.search("3 python 3")
print(m.group()) # python
print(m.start()) # 2
print(m.end()) # 8
print(m.span()) # (2, 8)

# 모듈 단위로 축약하기
m = re.match("[a-z]+", "python")
print(m) # <re.Match object; span=(0, 6), match='python'>


# 컴파일 옵션: 정규식 컴파일 할 때 여러 옵션 사용가능
# DOTALL(S): .(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치될 수 있게 한다.
p = re.compile("a.b") # 옵션 미반영 케이스
m = p.match("a\nb")
print(m) # None: 기본 .(dot)메타는 줄바꿈을 문자로 인식하지 않음

p = re.compile("a.b", re.DOTALL) # 옵션 DOTALL반영, re.S도 가능
m = p.match("a\nb")
print(m) # <re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE(I) - 대소문자에 관계없이 매치될 수 있게 한다.
p = re.compile("[a-z]+") # 옵션 미반영 케이스
m = p.match("PYTHON")
print(m) # None: 대문자는 [a-z]ㅇ에 매칭되지 않음

p = re.compile("[a-z]+", re.IGNORECASE) # 옵션 re.IGNORECASE 반영, re.I도 가능
m = p.match("PYTHON")
print(m) # re.Match object; span=(0, 6), match='PYTHON'>

# MULTILINE(M) - 여러 줄과 매치될 수 있게 한다. ^, $ 메타 문자 사용과 관계 있는 옵션이다.
# ^는 문자열의 처음, $는 문자열의 마지막을 의미함.
# ex) "^python": 문자열이 "python"으로 시작되어야 함.
# ex) "python$": 문자열이 "python"으로 끝나야 함.
data = """python one
life is too short
python two
you need python
python three"""

p = re.compile(r"^python\s\w+") # python으로 시작하고, 화이트 스페이스 이후 1자 이상의 문자가 와야함.
words = p.findall(data)
print(words) # ['python one']: 줄바꿈을 포함해서 한벌의 문자열로 보는듯

p = re.compile(r"^python\s\w+", re.MULTILINE) # re.MULTILINE 옴션 적용, re.M도 가능
words = p.findall(data)
print(words) # ['python one', 'python two', 'python three']: 라인별로 별도의 문자열처럼 동작?

# VERBOSE(X) - verbose 모드를 사용할 수 있게 한다. 정규식을 보기 편하게 만들 수 있고 주석 등을 사용할 수 있게 된다.
# 한줄로 적다보니 알아보기 어려움
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

regex = r"""
^[a-zA-Z0-9._%+-]+  # 이메일 앞자리: 영문/숫자등 1자 이상
@                   # @
[a-zA-Z0-9.-]+      # 도메인: 영문/숫자등 1자 이상
.                   # .
[a-zA-Z]{2,}$       # 마지막 도메인: 영문 2자 이상(com, net등)
"""

email_pattern = re.compile(regex) # 옵션 없이 이메일 패턴 적용(내부에 화이트 스페이스 있음)
m = email_pattern.match("didwndckd@gmail.com")
print(m) # None: 내부 화이트 스페이스때문에 정상적인 이메일이지만 매치되지 않음

email_pattern = re.compile(regex, re.VERBOSE) # re.VERBOSE옵션 적용, re.X 가능
m = email_pattern.match("didwndckd@gmail.com")
print(m) # <re.Match object; span=(0, 19), match='didwndckd@gmail.com'>

# 역슬래시 문제
# ex) "\section" 문자열을 찾기 위한 정규식을 만든다고 가정
p = re.compile("\section") # [ \t\n\r\f\v]ection과 같은 의미임
m = p.match("\section")
print(m) # None

# \을 문자 자체로 사용하려면 \\로 표시해야함
p = re.compile("\\section") # 정규식에 들어가면 \로 취급하기위해 넣은 \\section이 \section으로 바뀜
m = p.match("\\section")
print(m) # None

# 정규식에 들어가서도 \section문자로 취급하기 위해서는 \\\\로 넣어야 함
# 1. 컴파일 내부에서 \\\\section이 \\section으로 변환, \를 진짜 문자열로 취급
p = re.compile("\\\\section") 
m = p.match("\\section")
print(m) # <re.Match object; span=(0, 8), match='\\section'>
print(m.group()) # \section

# 더 편하게 하기 위해서 사용하는 r: r은 내부에 \를 문자로 취급
p = re.compile(r"\\section")
m = p.match(r"\section")
print(m) # <re.Match object; span=(0, 8), match='\\section'>
print(m.group()) # \section

