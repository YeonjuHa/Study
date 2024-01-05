# # 함수 만들기
# # 함수의 선언(정의)
# def hello():    
#     print('Hello, world!')    # 함수 구문

# # 함수의 호출
# hello()


# # 함수 작성과 함수 호출 순서
# hello()

# def hello():
#     print('Hello, world!')


# # 덧셈함수 만들기
# def add(a, b):
#     print(a+b)

# add(10, 20)

# # 독스트링
# def add(a, b):
#     """"이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
#     return a + b

# x = add(10, 20)
# print(x)

# print(add.__doc__)


# # 함수의 결과를 반환하기
# def add(a, b):
#     return a + b

# x = add(10, 20)
# print(x)

# # 매개변수는 없고 반화값만 있는 함수
# def one():
#     return 1

# x = one()
# print(x)

# # return으로 함수 중간에서 빠져나오기
# def not_ten(a):
#      if a == 10:
#          return
#      print(a, '입니다.', sep='')

# not_ten(5)
# not_ten(10)


# # 함수에서 값을 여러 개 반환하기
# def add_sub(a, b):
#     return a + b, a - b

# x, y = add_sub(10, 20)
# print(x)
# print(y)

# z = add_sub(100, 200)
# z

# # 값 여러 개를 직접 반환하기
# def one_two():
#     return (1, 2)

# print(1, 2)

# def one_two():
#     return 1, 2


# # 리스트
# def one_two():
#     return [1, 2]

# x, y = one_two()
# print(x, y)


# 함수의 호출 과정 알아보기
def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)

x = 10
y = 20
add(x, y)