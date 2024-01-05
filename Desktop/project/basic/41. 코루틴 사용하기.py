# # 메인 루틴과 서브 루틴
# def add(a, b):      # 함수 정의
#     print('add 함수 실행')
#     c = a + b
#     return c        # 결과 반환

# def calc():         # 함수 정의
#     print('calc 함수')
#     r = add(1, 2)
#     print('결과: ', r)

# calc()              # 함수 호출


# # 코루틴에 값 보내기
# def number_coroutine():
#     while(True):
#         x = (yield)
#         print(x)

# co = number_coroutine()
# next(co)

# co.send(1)
# co.send(2)
# co.send(3)


# # 코루틴 바깥으로 값 전달하기
# def sum_coroutine():
#     total = 0
#     while(True):
#         x = (yield total)
#         total += x

# co = sum_coroutine()
# print(next(co))

# print(co.send(1))
# print(co.send(2))
# print(co.send(3))


# # 코루틴을 종료하고 예외 처리하기
# def number_coroutine():
#     while(True):
#         x = (yield)
#         print(x, end=' ')

# co = number_coroutine()
# next(co)

# for i in range(20):
#     co.send(i)

# co.close()


# GeneratorExit 예외 처리하기
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()