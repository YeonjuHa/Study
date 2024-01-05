# # 클래스와 메서드 만들기
# class Person:
#     def greeting(self):
#         print('Hello')

# james = Person()    # Person 클래스로 james 인스턴스 만들기

# # 메서드 호출하기
# james.greeting()   # 인스턴스를 통해 클래스의 메서드에 접근

# maria = Person()
# maria.greeting()


# # 파이썬에서 흔히 볼 수 있는 클래스
# a = int(10)
# a

# b = list(range(10))
# b

# c = dict(x=10, y=20)
# c

# b = list(range(10))
# b.append(20)
# b

# a = 10
# type(a)

# b = [0, 1, 2]
# type(b)

# c = {'x': 10, 'y': 20}
# type(c)

# james = Person()
# type(james)


# # 인스턴스와 객체의 차이점?
# a = list(range(10))
# a
# b = list(range(20))
# b

# # 빈 클래스 만들기
# class Person:
#     pass

# # 메서드 안에서 메서드 호출하기
# class Person:
#     def greeting(self):
#         print('Hello')
    
#     def hello(self):
#         self.greeting()

# james = Person()
# james.hello()


# # 특정 클래스의 인스턴스인지 확인하기
# class Person:
#     pass

# james = Person()
# isinstance(james, Person)
# isinstance(maria, Person)

# # 숫자가 정수일 때만 계산하도록
# def factorial(n):
#     if not isinstance(n, int) or n < 0:
#         return None
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# factorial(5)
# factorial(-5)    # 결과 안나옴
# factorial(5.0)   # 결과 안나옴


# # 속성 사용하기
# class Person:
#     def __init__(self):
#         self.hello = '안녕하세요.'
    
#     def greeting(self):
#         print(self.hello)
    
# james = Person()
# james.greeting()


# # 인스턴스를 만들 때 값 받기
# class Person:
#     def __init__(self, name, age, address):
#         self.hello = '안녕하세요.'
#         self.name = name
#         self.age = age
#         self.address = address

#     def greeting(self):
#         print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

# maria = Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()

# print('이름: ', maria.name)
# print('나이: ', maria.age)
# print('주소: ', maria.address)


# # 클래스의 위치 인수, 키워드 인수
# class Person:
#     def __init__(self, *args):
#         self.name = args[0]
#         self.age = args[1]
#         self.address = args[2]
    
#     def greeting(self):
#         print(self.name, self.age, self.address)

# maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
# maria.greeting()


# class Person:
#     def __init__(self, **kwargs):
#         self.name = kwargs['name']
#         self.age = kwargs['age']
#         self.address = kwargs['address']
    
#     def greeting(self):
#         print(self.name, self.age, self.address)

# maria1 = Person(name= '마리아', age= 20, address= '서울시 서초구 반포동')
# maria1.greeting()

# maria2 = Person(**{'name': '마리아', 'age': 22, 'address': '수원시 영통구 영통동'})
# maria2.greeting()



# # 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
# class Person:
#     pass

# maria = Person()
# maria.name = '마리아'
# print(maria.name)

# james = Person()
# print(james.name)


# class Person:
#     def greeting(self):
#         self.hello = '안녕하세요.'

# maria = Person()
# # maria.hello
# maria.greeting()
# print(maria.hello)


# class Person:
#     __slots__ = ['name', 'age']

# maria = Person()
# maria.name = '마리아'
# maria.age = 20
# maria.address = '서울시 서초구 반포동'  # 허용되지 않은 속성, 에러 발생


# # 비공개 속성 사용하기
# class Person:
#     def __init__(self, name, age, address, wallet):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet  # 비공개 속성

# maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet -= 10000


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개 속성

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개 속성

    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네...')
            return None
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(13000)


# 비공개 매서드 사용하기
class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()

james = Person()
james.hello()
james.__greeting()