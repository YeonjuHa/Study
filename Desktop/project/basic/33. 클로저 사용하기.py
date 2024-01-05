# # 변수의 사용 범위 알아보기
# x = 10        # 전역 변수
# def foo():
#     print(x)  # 전역 변수 출력

# foo()         # 함수 호출
# print(x)      # 전역 변수 출력



# def foo():
#     x = 10    # foo의 지역 변수
#     print(x)  # foo의 지역 변수 출력

# foo()         # 함수 호출
# print(x)      # 에러 발생


# # 함수 안에서 전역 변수 변경하기
# x = 10        # 전역 변수
# def foo():
#     x = 20    # foo의 지역 변수
#     print(x)  # foo의 지역 변수 출력

# foo()         # 함수 호출
# print(x)      # 전역 변수 출력


# x = 10        # 전역 변수
# def foo():
#     global x  # x를 전역 변수로 만듦
#     x = 20    # x는 전역 변수
#     print(x)  # 전역 변수 출력

# foo()
# print(x)      # 전역 변수 출력


# # 전역 변수 x가 없는 상황
# def foo():
#     global x  # x를 전역 변수로 만듦
#     x = 20    # x는 전역 변수
#     print(x)  # 전역 변수 출력

# foo()
# print(x)      # 전역 변수 출력


# # 네임스페이스
# x = 10
# locals()


# # 함수 안에서 함수 만들기
# def print_hello():
#     hello = 'Hello, world!'
#     def print_message():
#         print(hello)
#     print_message()

# print_hello()


# # 지역 변수 변경하기
# def A():
#     x = 10      # A의 지역 변수
#     def B():
#         x = 20  # x에 20 할당

#     B()
#     print(x)    # A의 지역 변수 x 출력

# A()


# # nonlocal
# def A():
#     x = 10      # A의 지역변수
#     def B():
#         nonlocal x
#         x = 20
    
#     B()
#     print(x)

# A()


# # nonlocal이 변수를 찾는 순서
# def A():
#     x = 10      # A의 지역변수
#     y = 100
#     def B():
#         x = 20
#         def C():
#             nonlocal x
#             nonlocal y
#             x = x + 30
#             y = y + 300
#             print(x)
#             print(y)

#         C()
#     B()

# A()


# # global로 전역 변수 사용하기
# x = 1
# def A():
#     x = 10
#     def B():
#         x = 20
#         def C():
#             global x
#             x = x + 30
#             print(x)
#         C()
#     B()

# A()


# 클로저 사용하기
def calc():
    a = 3       # 함수 calc의 지역 변수
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))


# lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b

c = calc()
print(c(1), c(2), c(3), c(4), c(5))


# 클로저의 지역 변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
c(3)