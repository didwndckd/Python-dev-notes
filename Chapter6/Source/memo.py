# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장 만들기
# 메모 경로는 temp/memo/

import sys
import pathlib

option = sys.argv[1] # 옵션 꺼내오기: -a
directory_path = 'temp/memo' # 저장 디렉터리 경로
memo_path = f"{directory_path}/memo.txt" # 메모 파일 경로

# 실행 했을 때 메모 파일 생성/내용 추가: python3 Chapter6/Source/memo.py -a "Life is too short"
def add_memo():
    pathlib.Path(directory_path).mkdir(exist_ok=True) # 디렉터리 만들기
    memo = sys.argv[2] # 입력 받은 메모 내용 꺼내오기
    with open(memo_path, 'a') as f:
        f.write(memo) # 파일에 메모 작성
        f.write('\n') # 줄바꿈 추가

# 실행 했을 때 메모 출력: python3 Chapter6/Source/memo.py -v
def read_memo():
    with open(memo_path, 'r') as f:
        memo = f.read()
        print(memo)

# 실행 했을 때 메모 삭제: python3 Chapter6/Source/memo.py -d
def remove_memo():
    pathlib.Path(memo_path).unlink(missing_ok=True)

if option == '-a':
    add_memo()
elif option == '-v':
    try:
        read_memo()
    except FileNotFoundError:
        print("파일이 없습니다.")

elif option == '-d':
    remove_memo()