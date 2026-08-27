# 정규 표현식 시작하기(regular expression)

> 예제 코드: [Source/regular_expression-2.py](Source/regular_expression-2.py)

- [메타 문자](#메타-문자)
- [문자 클래스 `[]`](#문자-클래스-)
- [임의의 문자 `.`](#임의의-문자-)
- [반복 메타 문자](#반복-메타-문자)
- [`re` 모듈과 패턴 객체](#re-모듈과-패턴-객체)
- [문자열 검색 메서드](#문자열-검색-메서드)
- [match 객체](#match-객체)
- [컴파일 옵션](#컴파일-옵션)
- [역슬래시 문제](#역슬래시-문제)

## 메타 문자

정규식에서 메타 문자(meta character)는 문자 자체가 아니라 특별한 규칙을 뜻한다. `.` , `*`, `+`, `?`, `{}`, `[]`, `\` 등이 대표적인 메타 문자이다.

```python
. ^ $ * + ? { } [ ] \ | ( )
```

정규식과 문자열의 규칙이 맞으면 **매치된다**고 한다. 예를 들어 패턴 `abc`는 문자열 `abc`와 매치된다.

## 문자 클래스 `[]`

`[]` 안에 넣은 문자 중 하나와 매치된다. 범위를 지정할 때는 `-`을 쓰고, `^`를 맨 앞에 쓰면 해당 범위를 제외한다.

```python
import re

p = re.compile("[abc]")
p.match("a")       # <re.Match object; span=(0, 1), match='a'>
p.match("before")  # <re.Match object; span=(0, 1), match='b'>
p.match("dude")    # None
```

- `[a-c]` — `a`, `b`, `c` 중 하나와 매치된다.
- `[0-9]` — 숫자 하나와 매치된다.
- `[a-zA-Z]` — 영문 알파벳 하나와 매치된다.
- `[가-힣]` — 한글 글자 하나와 매치된다.
- `[^0-9]` — 숫자가 아닌 문자 하나와 매치된다.

자주 쓰는 문자 클래스는 짧은 표기법도 제공한다.

```python
\d  # 숫자, [0-9]
\D  # 숫자가 아닌 문자, [^0-9]
\s  # 공백 문자, [ \t\n\r\f\v]
\S  # 공백이 아닌 문자
\w  # 영문자·숫자·밑줄, [a-zA-Z0-9_]
\W  # \w가 아닌 문자
```

> 소문자 표기와 대문자 표기는 서로 반대 의미인 경우가 많다. 예를 들어 `\d`는 숫자, `\D`는 숫자가 아닌 문자이다.

## 임의의 문자 `.`

`.`은 줄바꿈(`\n`)을 제외한 임의의 한 문자와 매치된다.

```python
import re

p = re.compile("a.b")
p.match("aab")  # <re.Match object; span=(0, 3), match='aab'>
p.match("a0b")  # <re.Match object; span=(0, 3), match='a0b'>
p.match("abc")  # None
```

> 마침표 자체를 찾으려면 `a[.]b` 또는 `a\.`처럼 메타 문자 의미를 없애야 한다.

## 반복 메타 문자

반복 메타 문자는 바로 앞 요소의 반복 횟수를 정한다.

```python
*       # 바로 앞 요소가 0회 이상
+       # 바로 앞 요소가 1회 이상
{n}     # 정확히 n회
{m, n}  # m회 이상 n회 이하
{m,}    # m회 이상
{,n}    # n회 이하
?       # 0회 또는 1회, {0, 1}과 같음
```

```python
p = re.compile("ca*t")
p.match("ct")     # <re.Match object; span=(0, 2), match='ct'>
p.match("cat")    # <re.Match object; span=(0, 3), match='cat'>
p.match("caaat")  # <re.Match object; span=(0, 5), match='caaat'>

p = re.compile("ca{2,5}t")
p.match("cat")       # None
p.match("caat")      # <re.Match object; span=(0, 4), match='caat'>
p.match("caaaaat")   # <re.Match object; span=(0, 7), match='caaaaat'>

p = re.compile("ca?t")
p.match("ct")    # <re.Match object; span=(0, 2), match='ct'>
p.match("cat")   # <re.Match object; span=(0, 3), match='cat'>
p.match("caat")  # None
```

## `re` 모듈과 패턴 객체

`re.compile()`은 정규식 문자열을 재사용하기 좋은 패턴 객체로 만든다. 같은 패턴으로 여러 번 검색할 때 유용하다.

```python
import re

p = re.compile("ab*")
```

한 번만 사용할 때는 `re.match()`처럼 모듈 함수로 축약할 수 있다.

```python
m = re.match("[a-z]+", "python")
m  # <re.Match object; span=(0, 6), match='python'>
```

## 문자열 검색 메서드

패턴 객체는 `match()`, `search()`, `findall()`, `finditer()` 메서드로 문자열을 검색한다.

- **`match()`** — 문자열의 처음부터 매치되는지 확인한다.
- **`search()`** — 문자열 전체에서 처음 매치되는 부분을 찾는다.
- **`findall()`** — 매치되는 모든 문자열을 리스트로 반환한다.
- **`finditer()`** — 매치 결과를 차례로 꺼낼 수 있는 반복자를 반환한다.

```python
p = re.compile("[a-z]+")
p.match("python")     # <re.Match object; span=(0, 6), match='python'>
p.match("3 python")   # None

p.search("python")    # <re.Match object; span=(0, 6), match='python'>
p.search("3 python")  # <re.Match object; span=(2, 8), match='python'>

p.findall("life is too short")
# ['life', 'is', 'too', 'short']

list(p.finditer("life is too short"))
# [<re.Match object; span=(0, 4), match='life'>,
#  <re.Match object; span=(5, 7), match='is'>,
#  <re.Match object; span=(8, 11), match='too'>,
#  <re.Match object; span=(12, 17), match='short'>]
```

## match 객체

`match()`, `search()`, `finditer()`가 성공하면 match 객체를 돌려준다. 이 객체로 매치된 문자열과 위치를 확인한다.

```python
p = re.compile("[a-z]+")
m = p.search("3 python 3")

m.group()  # python
m.start()  # 2
m.end()    # 8
m.span()   # (2, 8)
```

> 검색에 실패하면 `None`이 반환된다. 따라서 `m.group()`을 호출하기 전에는 `if m:`처럼 결과가 있는지 확인한다.

## 컴파일 옵션

`re.compile(패턴, 옵션)`으로 옵션을 지정할 수 있으며, 긴 이름과 짧은 이름을 모두 사용할 수 있다.

### DOTALL(S)

`.`이 줄바꿈까지 포함해 모든 문자와 매치되게 한다.

```python
# DOTALL 미적용: .은 줄바꿈과 매치하지 않는다.
p = re.compile("a.b")
p.match("a\nb")  # None

# DOTALL 적용: .이 줄바꿈까지 포함한다.
p = re.compile("a.b", re.DOTALL)
p.match("a\nb")  # <re.Match object; span=(0, 3), match='a\nb'>
```

### IGNORECASE(I)

대소문자를 구분하지 않고 매치한다.

```python
# IGNORECASE 미적용: [a-z]는 대문자와 매치하지 않는다.
p = re.compile("[a-z]+")
p.match("PYTHON")  # None

# IGNORECASE 적용: 대소문자를 구분하지 않는다.
p = re.compile("[a-z]+", re.IGNORECASE)
p.match("PYTHON")  # <re.Match object; span=(0, 6), match='PYTHON'>
```

### MULTILINE(M)

`^`는 문자열의 시작, `$`는 문자열의 끝을 뜻한다. 기본적으로는 전체 문자열의 시작과 끝에만 적용되지만, `re.MULTILINE`을 사용하면 각 줄의 시작과 끝에도 적용된다.

```python
^python  # 문자열(또는 각 줄)이 python으로 시작
python$  # 문자열(또는 각 줄)이 python으로 끝
```

```python
data = """python one
life is too short
python two
you need python
python three"""

# MULTILINE 미적용: 문자열 전체의 첫 줄만 ^와 매치한다.
p = re.compile(r"^python\s\w+")
p.findall(data)
# ['python one']

# MULTILINE 적용: 각 줄의 시작에 ^를 적용한다.
p = re.compile(r"^python\s\w+", re.MULTILINE)
p.findall(data)
# ['python one', 'python two', 'python three']
```

### VERBOSE(X)

공백과 주석을 사용해 여러 줄 패턴을 읽기 좋게 작성한다.

```python
regex = r"""
^[a-zA-Z0-9._%+-]+  # 이메일 앞자리
@                   # @
[a-zA-Z0-9.-]+      # 도메인
\.                  # 점(.) 자체
[a-zA-Z]{2,}$       # 마지막 도메인
"""

# VERBOSE 미적용: 공백과 주석까지 패턴에 포함되어 매치하지 않는다.
email_pattern = re.compile(regex)
email_pattern.match("didwndckd@gmail.com")  # None

# VERBOSE 적용: 공백과 주석을 무시해 읽기 쉬운 여러 줄 패턴을 쓸 수 있다.
email_pattern = re.compile(regex, re.VERBOSE)
email_pattern.match("didwndckd@gmail.com")
# <re.Match object; span=(0, 19), match='didwndckd@gmail.com'>
```

> `re.VERBOSE`에서는 공백과 `#` 뒤 주석이 무시된다. 문자 클래스 `[]` 안의 공백은 예외이며, 점 자체를 찾으려면 `.`이 아니라 `\.`을 사용한다.

## 역슬래시 문제

역슬래시는 파이썬 문자열 리터럴과 정규식 엔진에서 각각 해석된다. 따라서 문자열 `\section`을 문자 그대로 찾으려면 역슬래시가 두 단계를 모두 통과하도록 작성해야 한다.

```python
# 실패 1: `\s`는 파이썬에서 권장되지 않는 이스케이프 표기이며,
# 정규식 엔진에는 \section이 전달되어 \s가 공백 문자로 해석된다.
p = re.compile("\section")
p.match("\section")  # None

# 실패 2: 파이썬 문자열의 \\가 \ 하나로 변환되므로 결과는 위와 같다.
p = re.compile("\\section")
p.match("\\section")  # None

# 성공: 파이썬 문자열 변환 뒤 정규식 엔진에 \\section이 전달됨
p = re.compile("\\\\section")
p.match("\\section")
# <re.Match object; span=(0, 8), match='\\section'>
```

raw 문자열을 사용하면 파이썬 문자열 단계에서 역슬래시를 그대로 유지하므로 더 읽기 쉽다.

```python
p = re.compile(r"\\section")
m = p.match(r"\section")
m.group()  # \section
```

> `r`은 **파이썬 문자열 리터럴**의 이스케이프 처리를 막을 뿐, 정규식 엔진의 해석까지 막지는 않는다. 따라서 리터럴 역슬래시 하나를 찾는 정규식에는 raw 문자열에서도 `\\`가 필요하다.
