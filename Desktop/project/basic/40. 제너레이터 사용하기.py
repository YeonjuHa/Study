# # 제너레이터와 yield 알아보기
# def number_generator():
#     yield 0
#     yield 1
#     yield 2

# for i in number_generator():
#     print(i)


# # 제너레이터 객체가 이터레이터인지 확인하기
# g = number_generator()
# g
# dir(g)


# def hello():
#     print('hello')
#     print('안녕')
#     print('hi')

# hello()

# yield의 동작 과정 알아보기
def number_generator():
    yield 0
    yield 1
    yield 2

g = number_generator()

a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)


# # 제너레이터와 return
# def one_generator():
#     yield 1
#     return 'return에 지정한 값'

# try:
#     g = one_generator()
#     next(g)
#     next(g)
# except StopIteration as e:
#     print(e)    # return에 지정한 값


# # 제너레이터 만들기
# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1

# for i in number_generator(3):
#     print(i)


# #  yield에서 함수 호출하기
# def upper_generator(x):
#     for i in x:
#         yield i.upper()

# fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
# for i in upper_generator(fruits):
#     print(i)


# # yield from으로 값을 여러 번 바깥으로 전달하기
# def number_generator():
#     x = [1, 2, 3]
#     for i in x:
#         yield i

# for i in number_generator():
#     print(i)

# print()

# def number_generator():
#     x = [1, 2, 3]
#     yield from x

# for i in number_generator():
#     print(i)


# # yield from에 제너레이터 객체 지정하기
# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1

# def three_generator():
#     yield from number_generator(3)

# for i in three_generator():
#     print(i)