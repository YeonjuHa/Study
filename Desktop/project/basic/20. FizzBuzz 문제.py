# # 1부터 100까지 숫자 출력하기
# for i in range(1, 101):
#     print(i)

# # 3의 배수일 때와 5의 배수일 때 처리하기
# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# # 3과 5의 공배수 처리하기
# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# # 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
# for i in range(1, 101):
#     if i % 15 == 0:
#     print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# 코드 단축하기
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)