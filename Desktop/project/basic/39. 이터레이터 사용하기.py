# # 반복 가능한 객체 알아보기
# dir([1, 2, 3])
# [1, 2, 3].__iter__()

# it = [1, 2, 3].__iter__()
# it.__next__()

# it1 = 'Hello, world!'.__iter__()
# it1.__next__()
# it2 = {'a': 1, 'b': 2}.__iter__()
# it2.__next__()
# it3 = {1, 2, 3}.__iter__()
# it3.__next__()

# it = range(3).__iter__()
# it.__next__()


# # 이터레이터 만들기
# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < self.stop:
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopIteration
        
# for i in Counter(3):
#     print(i, end=' ')

# print()

# # 이터레이터 언패킹
# a, b, c = Counter(3)
# print(a, b, c)

# a, b, c, d, e = Counter(5)
# print(a, b, c, d, e)

# # 반환값을 _에 저장하는 이유
# _, b = range(2)
# b

# a, _, c, d = range(4)
# a, c, d

# for _ in [1, 2, 3]:     # 값 자체는 이용하지 X
#     print('hello')


# # 인덱스로 접근할 수 있는 이터레이터 만들기
# class Counter:
#     def __init__(self, stop):
#         self.stop = stop
    
#     def __getitem__(self, index):
#         if index < self.stop:
#             return index
#         else:
#             raise IndexError
        
# print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

# for i in Counter(3):
#     print(i, end=' ')


# # iter, next 함수 사용하기
# it = iter(range(3))
# next(it)

# # iter
# import random
# it = iter(lambda : random.randint(0, 5), 2)
# next(it)
# next(it)
# next(it)
# next(it)

# import random
# for i in iter(lambda : random.randint(0, 5), 2):
#     print(i, end=' ')

# print()

# import random

# while True:
#     i = random.randint(0, 5)
#     if i == 2:
#         break
#     print(i, end=' ')


# next
it = iter(range(3))
next(it, 10)