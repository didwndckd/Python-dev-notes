# 강력한 정규 표현식(advanced regular expression)

> 예제 코드: [Source/regular_expression-3.py](Source/regular_expression-3.py)

- [문자열 소비가 없는 메타 문자](#문자열-소비가-없는-메타-문자)
- [그루핑](#그루핑)
- [그룹 재참조와 이름 붙이기](#그룹-재참조와-이름-붙이기)
- [전방 탐색](#전방-탐색)
- [문자열 바꾸기](#문자열-바꾸기)
- [greedy와 non-greedy](#greedy와-non-greedy)

## 문자열 소비가 없는 메타 문자

앞에서 배운 `+`, `*`, `[]`, `{}`는 매치한 만큼 검색 위치를 앞으로 옮긴다. 반면 아래 메타 문자는 위치 조건을 확인하거나 선택할 뿐, 문자열을 소비하지 않는다.

- **`|`** — `A|B`처럼 A 또는 B와 매치한다.

  ```python
  p = re.compile("Crow|Servo")
  p.match("CrowHello")       # <re.Match object; span=(0, 4), match='Crow'>
  p.findall("CrowServo")     # ['Crow', 'Servo']
  ```

- **`^`** — 문자열의 시작과 매치한다. `re.MULTILINE`을 쓰면 각 줄의 시작에도 적용된다.

  ```python
  re.search("^Life", "Life is too short")  # <re.Match object; span=(0, 4), match='Life'>
  re.search("^Life", "MY Life")            # None
  ```

- **`$`** — 문자열의 끝과 매치한다. `re.MULTILINE`을 쓰면 각 줄의 끝에도 적용된다.

  ```python
  re.search("short$", "Life is too short")                    # <re.Match object; span=(12, 17), match='short'>
  re.search("short$", "Life is too short, you need python")  # None
  ```

- **`\A`** — 전체 문자열의 시작과만 매치한다. `re.MULTILINE`을 사용해도 각 줄의 시작에는 적용되지 않는다.

  ```python
  data = """python one
  life is too short
  python two
  you need python
  python three"""

  re.compile(r"^python", re.MULTILINE).findall(data)   # ['python', 'python', 'python']
  re.compile(r"\Apython", re.MULTILINE).findall(data)  # ['python']
  ```

- **`\Z`** — 전체 문자열의 끝과만 매치한다. `re.MULTILINE`을 사용해도 각 줄의 끝에는 적용되지 않는다.

  ```python
  data = """python one
  life is too short
  python two
  you need python
  python three
  four python"""

  re.compile(r"python$", re.MULTILINE).findall(data)  # ['python', 'python']
  re.compile(r"python\Z", re.MULTILINE).findall(data) # ['python']
  ```

- **`\b`** — 단어 구분자와 매치한다.

  `\b`는 단어의 시작이나 끝을 찾는 단어 구분자다. `\bclass\b`처럼 쓰면 공백으로 구분된 `class`나 문자열 전체가 `class`인 경우에 매치한다.

  ```python
  p = re.compile(r"\bclass\b")
  p.search("no class at all")                 # <re.Match object; span=(3, 8), match='class'>
  p.search("the declassified algorithm")      # None
  p.search("one subclass is")                  # None
  p.search("class")                            # <re.Match object; span=(0, 5), match='class'>
  ```

- **`\B`** — 단어 구분자가 아닌 위치와 매치한다.

  ```python
  p = re.compile(r"\Bclass\B")
  p.search("the declassified algorithm")      # <re.Match object; span=(6, 11), match='class'>
  ```

> `\b`는 일반 파이썬 문자열에서 백스페이스를 뜻하므로, 단어 경계로 사용하려면 반드시 `r"\bclass\b"`처럼 raw 문자열로 쓴다.

## 그루핑

괄호 `()`는 여러 문자를 하나로 묶어 반복하거나, 매치된 문자열의 원하는 부분을 꺼내는 데 사용한다. `group(0)` 또는 `group()`은 전체 매치이고, `group(1)`부터 각 그룹을 가리킨다.

```python
# ABC를 하나의 단위로 묶어 한 번 이상 반복
p = re.compile("(ABC)+")
m = p.match("ABCABCABC OK?")
m.group()  # ABCABCABC

# 이름과 전화번호를 그룹으로 추출
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.match("yjc 010-1234-1234")
m.group(0)  # yjc 010-1234-1234
m.group(1)  # yjc
m.group(2)  # 010-1234-1234
m.group(3)  # 010
```

중첩된 그룹도 왼쪽에서 오른쪽으로 여는 괄호를 만나는 순서대로 번호가 붙는다.

```python
p = re.compile(r"(\w+)\s+([(](\w+)[-]\w+[-]\w+[)])\s+(\w+)")
m = p.match("그룹1 (그룹3-그룹아님-그룹아님) 그룹4")
m.group(1)  # 그룹1
m.group(2)  # (그룹3-그룹아님-그룹아님)
m.group(3)  # 그룹3
m.group(4)  # 그룹4
```

## 그룹 재참조와 이름 붙이기

`\1`, `\2`처럼 이미 만든 그룹을 다시 참조할 수 있다. 그룹이 많아지면 `(?P<이름>...)`으로 이름을 붙여 읽기 쉽게 만들 수 있다.

```python
# 같은 단어가 연속되는 경우 찾기
p = re.compile(r"(\b\w+)\s+\1")
s = p.search("Paris in the the spring")
s.group()  # the the

# 이름으로 그룹 꺼내기와 재참조하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = p.match("yjc 010-1234-1234")
m.group("name")   # yjc
m.group("phone")  # 010-1234-1234

p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
p.search("Pairs in the the spring").group()  # the the
```

## 전방 탐색

전방 탐색은 뒤에 특정 패턴이 있는지 확인하지만, 확인한 문자열을 매치 결과에 포함하지 않는다. `(?=...)`는 긍정형, `(?!...)`는 부정형 전방 탐색이다.

```python
# 콜론이 뒤에 있는지 확인하되, 결과에서는 제외
p = re.compile(".+(?=:)")
p.match("http://google.com").group()  # http
```

부정형 전방 탐색은 제외 조건을 간단하게 표현할 때 유용하다.

```python
files = ["foo.bar", "autoexec.bat", "sendmail.cf", "foo.exe"]

def filter_matched(files: list[str], regex: str) -> list[str]:
    return [file for file in files if re.match(regex, file)]

result = filter_matched(files, r".*[.](?!bat$|exe$).*$")
result  # ['foo.bar', 'sendmail.cf']
```

> `(?!bat$|exe$)`는 점 뒤의 확장자가 `bat`나 `exe`로 끝나지 않아야 한다는 뜻이다. 여러 제외 규칙을 복잡한 문자 클래스로 만들지 않아도 된다.

## 문자열 바꾸기

패턴 객체의 `sub(바꿀_값, 대상_문자열, count=...)`는 매치한 부분을 바꾼다. `subn()`은 바뀐 문자열과 변경 횟수를 튜플로 반환한다.

```python
p = re.compile("blue|white|red")
p.sub('colour', 'blue socks and red shoes')           # colour socks and colour shoes
p.sub('colour', 'blue socks and red shoes', count=1)  # colour socks and red shoes
p.subn('colour', 'blue socks and red shoes')          # ('colour socks and colour shoes', 2)
```

- **그룹 참조로 순서 바꾸기** — 치환 문자열에서 `\g<그룹명>` 또는 `\g<번호>`로 그룹을 다시 사용할 수 있다.

  ```python
  p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
  p.sub(r"\g<phone> \g<name>", "yjc 010-1234-1234")  # 010-1234-1234 yjc
  ```

  ```python
  p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
  p.sub(r"\g<2> \g<1>", "yjc 010-1234-1234")  # 010-1234-1234 yjc
  ```

- **함수로 바꾸기** — 첫 번째 인수에 함수를 전달하면 매치마다 match 객체를 받아 개별적으로 치환할 수 있다.

  ```python
  def hexrepl(match):
      value = int(match.group())
      return hex(value)

  p = re.compile(r'\d+')
  result = p.sub(hexrepl, "Call 65490 for printing, 49152 for user code.")
  result  # Call 0xffd2 for printing, 0xc000 for user code.
  ```

## greedy와 non-greedy

`*`, `+` 같은 반복 메타 문자는 기본적으로 가능한 한 길게 매치하는 greedy 방식이다. 뒤에 `?`를 붙이면 가능한 한 짧게 매치하는 non-greedy 방식이 된다.

```python
s = "<html><head><title>Title</title>"

m = re.match("<.*>", s)
m.span()   # (0, 32)
m.group()  # <html><head><title>Title</title>

m = re.match("<.*?>", s)
m.span()   # (0, 6)
m.group()  # <html>
```

`*?`, `+?`, `??`, `{m,n}?`처럼 반복 메타 문자 뒤에 붙은 `?`는 최소 반복을 뜻한다. 단독 `?`의 `0회 또는 1회` 의미와 구분한다.
