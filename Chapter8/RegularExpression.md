# 정규표현식(regular expression)

> 예제 코드: [Source/regular_expression-1.py](Source/regular_expression-1.py)

- [정규 표현식이란?](#정규-표현식이란)
- [정규 표현식은 왜 필요한가?](#정규-표현식은-왜-필요한가)
- [정규 표현식으로 주민등록번호 뒷자리 가리기](#정규-표현식으로-주민등록번호-뒷자리-가리기)

## 정규 표현식이란?

정규 표현식(regular expression)은 문자열의 패턴을 표현하는 특별한 문법이다. 원하는 문자열의 형태를 짧게 표현해 검색·검증·치환할 수 있으며, 줄여서 정규식이라고도 한다.

```python
\d{6}-\d{7}   # 숫자 6개, 하이픈(-), 숫자 7개
```

> 정규 표현식은 파이썬뿐 아니라 자바스크립트, 자바, C# 등 여러 언어에서 사용하는 문자열 처리 도구이다.

## 정규 표현식은 왜 필요한가?

정규식을 사용하지 않으면 텍스트를 나누고, 각 단어가 주민등록번호 형식인지 검사한 뒤, 다시 조립해야 한다. 찾을 문자열의 규칙이 복잡할수록 이 과정도 길어진다.

```python
data = """
park 800905-1049118
kim  700905-1059119
"""

class ResidentIdMarker:
    def excute(self, data: str) -> str:
        lines: list[str] = data.split("\n")
        results: list[str] = []

        for line in lines:
            marked = self.mark_line(line)
            results.append(marked)

        return "\n".join(results)

    def mark_line(self, origin: str) -> str:
        words: list[str] = []
        for word in origin.split(" "):
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
                word = word[:6] + "-*******"
            words.append(word)

        return " ".join(words)

marker = ResidentIdMarker()
result = marker.excute(data)
result
# park 800905-*******
# kim  700905-*******
```

> 예제 코드의 `word[7:].isdigit`는 메서드를 호출하지 않아 항상 참으로 평가된다. 형식을 정확히 검사하려면 `word[7:].isdigit()`처럼 괄호를 붙인다.

## 정규 표현식으로 주민등록번호 뒷자리 가리기

`re` 모듈로 정규 표현식을 사용한다. `re.compile()`은 패턴 객체를 만들고, `sub(바꿀_문자열, 대상_문자열)`은 일치한 부분을 치환한다.

```python
import re

pat = re.compile(r"(\d{6})-\d{7}")
```

- `(\d{6})` — 숫자 6개를 첫 번째 그룹으로 묶는다.
- `-` — 하이픈 문자와 일치한다.
- `\d{7}` — 숫자 7개와 일치한다.
- `r"..."` — 정규식의 `\d` 같은 백슬래시를 그대로 전달하는 raw 문자열이다.

```python
import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile(r"(\d{6})-\d{7}")
result = pat.sub(r"\g<1>-*******", data)
result
# park 800905-*******
# kim  700905-*******
```

`\g<1>`은 첫 번째 괄호 그룹인 앞 6자리 숫자를 다시 가리킨다. 따라서 앞자리와 하이픈은 유지하고, 뒤 7자리만 `*******`로 바꾼다.
