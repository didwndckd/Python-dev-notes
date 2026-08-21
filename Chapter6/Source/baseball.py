# 이번에는 컴퓨터와 대결하는 숫자 야구 게임을 만들어 보자. 숫자 야구는 상대방이 정한 서로 다른 3자리 숫자를 맞히는 게임이다. 숫자를 추측하면 스트라이크와 볼로 힌트를 알려주고, 이 힌트를 바탕으로 정답을 찾아가는 것이 이 게임의 핵심이다.
# 3자리의 숫자중 0은 제외

# 게임의 규칙
# 스트라이크: 숫자와 위치가 모두 맞음
# 볼: 숫자는 맞지만 위치가 다름
# ex) 324일때 132를 입력하면 숫자 3은 있지만 위치가 다르므로 볼, 숫자 2는 있지만 위치가 다르므로 볼 -> 0스트라이크 2볼
# ex) 324일때 325를 입력하면 -> 2스트라이크 0볼

import random

class BaseballGameResult:
    def __init__(self):
            self.strike = 0
            self.ball = 0

    def increment_strike(self):
        self.strike += 1

    def increment_ball(self):
        self.ball += 1

    def is_win(self):
        return self.strike == 3
    
    def description(self):
        return f"{self.strike} 스트라이크 | {self.ball} 볼"


class BaseballGame:
    def __init__(self):
        self.strike = 0
        self.ball = 0

    def _get_user_input(self, guide="3자리 숫자를 입력 하세요:"):
        """
        유저 입력 -> 숫자 리스트로 반환
        """
        question = input()
        return list(map(int, question))

    def _get_answer(self):
        """
        정답: 1~9 중복 없는 랜덤 3개 숫자
        """
        return random.sample(range(1, 10), 3)

    def _game_result(self, answer, guass):
        """
        answer를 받아서 정답을 반환
        """
        result = BaseballGameResult()

        for i in range(3):
            guass_item = guass[i]
            if guass_item == answer[i]:
                result.increment_strike()
            elif guass_item in answer:
                result.increment_ball()

        return result

    def start(self):
        """
        게임 시작
        """
        
        answer = self._get_answer()
        guass = self._get_user_input()
        result = self._game_result(answer, guass)

        print(f"정답: {answer} | 입력: {guass}")
        print(result.description())

class BaseballGame_V2(BaseballGame):
    # 다른 문자가 들어와도 숫자만 걸러대서 반환하는 버전
    def _get_user_input(self, guide="3자리 숫자를 입력 하세요:"):
        question = input(guide)
        filtered_question = filter(lambda char: char.isdigit(), question)
        # numbers = list(map(lambda char: int(char), filtered_question))
        numbers = list(map(int, filtered_question)) # 클로져 사용할 필요 없음
    
        if len(numbers) < 3:
            return self._get_user_input("유효하지 않습니다. 3자리 숫자를 다시 입력해주세요:")
        
        return numbers

class BaseballGame_V3(BaseballGame_V2):
    # 정확히 세자리 숫자가 들어왔는지 체크, 재입력 유도 버전
    def _get_user_input(self, guide="3자리 숫자를 입력 하세요:"):
        question = input(guide)

        # 3자리 이상 문자열이고 숫자로만 이루어져있는지 확인
        if len(question) < 3 or not question.isdigit():
            return self._get_user_input("유효하지 않습니다. 3자리 숫자를 다시 입력해주세요:")
        # numbers = list(map(lambda char: int(char), question))
        numbers = list(map(int, question)) # 클로져 없이 숫자 변환

        if 0 in numbers:
            return self._get_user_input("0은 포함될 수 없습니다. 3자리 숫자를 다시 입력해주세요:")

        return numbers

class BaseballGame_V4(BaseballGame_V3):
    # v2 + 숫자 중복 여부까지 확인
    def _get_user_input(self, guide="3자리 숫자를 입력 하세요:"):
        numbers = super()._get_user_input(guide)
        if len(numbers) == len(set(numbers)):
            return numbers
        else:
            return self._get_user_input("중복된 숫자는 입력할 수 없습니다. 3자리 숫자를 다시 입력해주세요:")

    # 3스트라이크가 될때까지 무한 루프
    def start(self):
        answer = self._get_answer()
        try_count = 0

        while True:
            try_count += 1
            guass = self._get_user_input()
            result = self._game_result(answer=answer, guass=guass)
            if result.is_win():
                break
            else:
                print(f"{try_count}번쨰 도전 실패!: {result.description()}")

        print(f"정답: {answer} | 입력: {guass}")
        print(f"{try_count}번째 도전에 성공: {result.description()}")

print("V1")
BaseballGame().start()

print("V2")
BaseballGame_V2().start()

print("V3")
BaseballGame_V3().start()

print("V4")
BaseballGame_V4().start()