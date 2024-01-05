# # 29.7 연습문제: 몫과 나머지를 구하는 함수 만들기
# # 다음 소스 코드를 완성하여 x를 y로 나누었을 때의 몫과 나머지가 출fur되게 만드세요.

# x = 10
# y = 3
# def get_quotient_remainder(a, b):
#     return a // b, a % b

# quotient, remainder = get_quotient_remainder(x, y)
# print( '몫: {0}, 나머지: {1}'.format(quotient, remainder))


# # 29.8 심사문제: 사칙 연산 함수 만들기
# # 표준 입력으로 숫자 두 개가 입력됩니다.
# #  다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요.
# #  이때 나눗셈의 결과는 실수라야 합니다.

# x, y = map(int, input().split())10

# def calc(a, b):
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return add, sub, mul, div

# a, s, m, d = calc(x, y)
# print( '덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))



# # 추가 문제
c = int(input('덧셈1, 뺄셈2, 곱셈3, 나눗셈4: '))
a = int(input('첫 번째 값을 입력: '))
b = int(input('두 번째 값을 입력: '))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def clac(a, b):
    if c == 1:
        return print('결과값: {0} + {1} = {2}'.format(a, b, add(a, b)))
    elif c == 2:
        return print('결과값: {0} - {1} = {2}'.format(a, b, sub(a, b)))
    elif c == 3:
        return print('결과값: {0} * {1} = {2}'.format(a, b, mul(a, b)))
    elif c == 4:
        return print('결과값: {0} / {1} = {2}'.format(a, b, div(a, b)))
    else:
        pass


print('-----------------------------')
print('입력값: {0}, {1}'.format(a, b))
clac(a, b)
print('-----------------------------')