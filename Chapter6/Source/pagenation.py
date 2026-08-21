# A 씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 개수와 한 페이지에 보여 줄 게시물 수를 입력받아 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.
# 이렇게 게시판의 페이지 수를 구하는 것을 '페이징'이라고 부른다.

# 잘못된 예시
def get_total_page(total_item_count, per_page):
    return total_item_count // per_page + 1

print(get_total_page(5, 10)) # 1
print(get_total_page(15, 10)) # 2
print(get_total_page(25, 10)) # 3
print(get_total_page(30, 10)) # 4 -> 3이어야 하는데 4가 나옴

print("="*20)

# 잘된 예시
def get_total_page(total_item_count, per_page):
    divided = total_item_count // per_page
    if total_item_count == 0 or per_page == 0: 
        return 0

    if total_item_count % per_page == 0:
        return divided
    else:
        return divided + 1

print(get_total_page(5, 10)) # 1
print(get_total_page(15, 10)) # 2
print(get_total_page(25, 10)) # 3
print(get_total_page(30, 10)) # 3