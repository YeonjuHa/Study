# # 재귀호출 사용하기
# def hello():
#     print('Hello, world!')
#     hello()

# hello()


# # 재귀호출에 종료 조건 만들기
# # 함수 정의
# def hello(count):
#     if count == 0:    # count 0이면
#         return None   # 호출한 곳을 반환
    
#     print('Hello, world!', count)

#     count -= 1
#     hello(count)

# # 함수 호출
# hello(5)


# # 재귀호출로 팩토리얼 구하기
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# x = factorial(5)
# print(x)