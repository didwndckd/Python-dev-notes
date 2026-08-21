# Python-dev-note

점프 투 파이썬([wikidocs.net/book/1](https://wikidocs.net/book/1))을 따라가며 정리한 파이썬 학습 노트.
각 문서는 설명과 예제로 이루어져 있으며, 챕터별 예제 코드는 각 챕터의 `Source/` 폴더에 있다.

## 자료형

- [숫자형(Number)](Chapter2/Numbers.md) — int, float, 진수 표현, 연산자
- [문자열(String)](Chapter2/String.md) — 문자열 생성, 인덱싱/슬라이싱, 포매팅, 관련 함수
- [리스트(List)](Chapter2/List.md) — 리스트 생성, 인덱싱/슬라이싱, 연산, 관련 함수
- [튜플(Tuple)](Chapter2/Tuple.md) — 튜플 생성, 불변성, 인덱싱/슬라이싱, 연산
- [딕셔너리(Dictionary)](Chapter2/Dictionary.md) — Key:Value 쌍, 추가/삭제, 관련 함수
- [집합(Set)](Chapter2/Set.md) — 집합 생성, 중복 제거, 교집합/합집합/차집합, 관련 함수
- [불(Bool)](Chapter2/Bool.md) — True/False, 자료형의 참과 거짓, 논리 연산자
- [변수(Variable)](Chapter2/Variable.md) — 변수 선언, 명명 규칙, 객체 복사와 참조

## 제어문

- [조건문(if)](Chapter3/If.md) — if/elif/else, 들여쓰기, 조건부 표현식, match-case
- [반복문(while)](Chapter3/While.md) — 기본 구조, break/continue, 무한 루프, while-else, 중첩
- [반복문(for)](Chapter3/For.md) — 기본 구조, range, 리스트 컴프리헨션, enumerate, zip

## 입출력

- [함수(function)](Chapter4/Function.md) — def 구조, 매개변수/인수, \*args/\*\*kwargs, 반환값, scope, lambda
- [사용자 입출력(input/print)](Chapter4/UserIO.md) — input, 형변환, print, sep/end 매개변수
- [파일 읽고 쓰기(file I/O)](Chapter4/FileIO.md) — open, 파일 열기 모드, read/readline/readlines, with문, 인코딩
- [프로그램의 입출력(sys.argv)](Chapter4/ProgramIO.md) — 명령행 인수, sys 모듈, argv

## 파이썬 날개 달기

- [클래스(class)](Chapter5/Class.md) — 클래스와 객체, self, 객체변수, 생성자, 상속, 오버라이딩, 클래스 변수
- [모듈(module)](Chapter5/Module.md) — import, from import, \_\_name\_\_, sys.path, PYTHONPATH
- [패키지(package)](Chapter5/Package.md) — 패키지 구조, \_\_init\_\_.py, 패키지 초기화, \_\_all\_\_, 상대 경로 import, pyproject.toml
- [예외 처리(exception)](Chapter5/HandleException.md) — try-except/finally/else, 오류 회피, raise, 예외 만들기
- [내장 함수(built-in function)](Chapter5/BuiltInFunction.md) — abs, all/any, enumerate, filter, map, range, sorted, zip 등
- [표준 라이브러리(standard library)](Chapter5/StandardLibrary.md) — datetime, time, math, random, itertools, os, threading, json, urllib 등
- [외부 라이브러리(external library)](Chapter5/ExternalLibrary.md) — PyPI, pip, Faker, fractions.Fraction, sympy

## 파이썬 프로그래밍, 어떻게 시작해야 할까?

- [구구단 예제](Chapter6/Source/gugu.py)
- [3과 5의 배수의 합](Chapter6/Source/sum_of_multiples.py)
  - [Project Euler에서 문제 풀어보기](https://projecteuler.net/archives)

## 부록: 개발 환경과 도구

점프 투 파이썬에는 없는 내용으로, 파이썬 공식 문서와 각 도구의 공식 문서를 참고해 정리했다.

- [가상 환경(venv)](Appendix/VirtualEnvironment.md) — venv 생성, 활성화, PATH 원리, requirements.txt, PEP 668, VS Code 연동
- [uv](Appendix/Uv.md) — pip 인터페이스, pyproject.toml, uv.lock, 스크립트 인라인 의존성, 파이썬 버전 관리
- [pyproject.toml](Appendix/PyprojectToml.md) — build-system, project 정보, 의존성 문법, 개발 의존성, scripts, tool 설정
