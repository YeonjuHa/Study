# # 위치 인수와 리스트 언패킹 사용하기
# print(10, 20, 30)

# # 위치 인수를 사용하는 함수를 만들고 호출하기
# def print_number(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# print_number(10, 20, 30)

# print()
# # 언패킹 사용하기
# x = [10, 20, 30]
# print_number(*x)
# print_number(*[10, 20, 30])
# print_number(*[10, 20])


# # 가변 인수 함수 만들기
# def print_numbers(*args):
#     for arg in args:
#         print(arg)
    
# print_numbers(10)
# print_numbers(10, 20, 30, 40)

# print()

# x = [10]
# print_numbers(*x)
# y = [10, 20, 30, 40]
# print_numbers(*y)


# # 고정 인수와 가변 인수를 함께 사용하기
# def print_numbers(a, *args):
#     print(a)
#     print(args)
#     print()

# print_numbers(1)
# print_numbers(1, 10, 20)
# print_numbers(*[10, 20, 30])


# # 키워드 인수 사용하기
# def personal_info(name, age, address):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)

# personal_info('홍길동', 30, '서울시 용산구 이촌동')
# personal_info(30, '서울시 용산구 이촌동', '홍길동')

# personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

# print(10, 20, 30, sep=':', end='')

# # 키워드 인수와 딕셔너리 언패킹 사용하기
# def personal_info(name, age, address):
    # print('이름: ', name)
    # print('나이: ', age)
    # print('주소: ', address)

# x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# personal_info(**x)
# x = {'age': 30, 'address': '서울시 용산구 이촌동', 'name': '홍길동'}
# personal_info(**x)
# personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# personal_info(**{'name': '홍길동', 'old': 30, 'address': '서울시 용산구 이촌동'})
# personal_info(**{'name': '홍길동', 'age': 30})


# # 키워드 인수를 사용하면 가변 인수 함수 만들기
# def personal_info(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ': ', arg, sep='')

# personal_info(name='홍길동')
# personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

# x = {'name': '홍길동'}
# personal_info(**x)
# y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# personal_info(**y)


# def personal_info(**kwargs):
#     if 'name' in kwargs:
#         print('이름: ', kwargs['name'])
#     if 'age' in kwargs:
#         print('나이: ', kwargs['age'])
#     if 'address' in kwargs:
#         print('주소: ', kwargs['address'])


# # 위치 인수와 키워드 인수를 함께 사용하기
# def custom_print(*args, **kwargs):
#     print(*args, **kwargs)

# custom_print(1, 2, 3, sep=':', end='')


# 매개변수에 초깃값 지정하기
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)
personal_info('홍길동', 30, '서울시 용산구 이촌동')

# 초깃값이 지정된 매개변수 위치
def personal_info(name, address='비공개', age):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

def personal_info(name, age, address='비공개'):
def personal_info(name, age=0, address='비공개'):
def personal_info(name='비공개', age=0, address='비공개'):






# # 함수를 변수 또는 리스트에 넣어서 호출할 수 있나요?
# def hello():
#     print('Hello, world!')

# x = hello
# x()

# y = [hello, hello]
# y[0]()
# y[1]()


# 순수 함수와 비순수 함수는 무엇인가요?
# 순수함수
def add(a, b):
    return a + b

print(add(1, 2))

# 비순수 함수
number_list = [1, 2, 3]

def append_number(n):
    number_list.append(n)

append_number(4)
print(number_list)