# 구구단 함수 만들기

def gugu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result

print(gugu(2))

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(i * n)
        i += 1
    return result

print(gugu(2))

def gugu(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result

print(gugu(2))