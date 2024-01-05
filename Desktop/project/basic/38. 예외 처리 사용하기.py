# # try except로 사용하기
# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print('결과: ', y)
# except:
#     print('예외가 발생했습니다.')


# # 특정 예외만 처리하기
# y =[10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
#     print('잘못된 인덱스입니다.')



# # 예외의 에러 메시지 받아오기
# y =[10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print('숫자를 0으로 나눌 수 없습니다.', e)
# except IndexError as e:
#     print('잘못된 인덱스입니다.', e)

# except Exception as e:
#     print('예외가 발생했습니다.', e)



# # else와 finally 사용하기
# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x

# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')

# else:
#     print(y)


# # 에외와는 상관없이 항상 코드 실행하기
# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x

# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')

# else:
#     print(y)
# finally:
#     print('코드 실행이 끝났습니다.')


# # 예외 발생시키기
# try:
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)
# except Exception as e:
#     print('예외가 발생했습니다.', e)


# # raise의 처리 과정
# def three_multiple():
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)

# try:
#     three_multiple()
# except Exception as e:
#     print('예외가 발생했습니다.', e)

# three_multiple()


# # 현재 예외를 다시 발생시키
# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0:
#             raise Exception('3의 배수가 아닙니다.')
#         print(x)
#     except Exception as e:
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise

# try:
#     three_multiple()
# except Exception as e:
#     print('스크립트 파일에서 예외가 발생했습니다.', e)


# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0:
#             raise Exception('3의 배수가 아닙니다.')
#         print(x)
#     except Exception as e:
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')


# # 예외 만들기
# class NotThreeMultipleError(Exception):
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.')

# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0:
#             raise NotThreeMultipleError
#         print(x)
#     except Exception as e:
#         print('예외가 발생했습니다.', e)

# three_multiple()