# 정규표현식의 필요성
# 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.

data: str = """
park 800905-1049118
kim  700905-1059119
"""

# 정규 표현식 사용하지 않는 버전
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
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit:
                word = word[:6] + "-*******"
                words.append(word)
            else:
                words.append(word)

        return " ".join(words)

marker = ResidentIdMarker()
result = marker.excute(data)
print(result)
# 실행 결과
# park 800905-*******
# kim  700905-*******

import re

# 정규 표현식 사용하는 버전
class ResidentIdMarker_V2(ResidentIdMarker):
    def excute(self, data):
        pat = re.compile(r"(\d{6})-\d{7}")
        result = pat.sub(r"\g<1>-*******", data)
        return result

marker = ResidentIdMarker_V2()
result = marker.excute(data)
print(result)