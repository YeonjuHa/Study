# # class 선언(복습)
# class Person:
#     def __init__(self, **kwarg):
#         self.hello = '안녕하세요'
#         self.name = kwarg['name']
#         self.age = kwarg['age']
#         # self.address = arg[2]

#     def greeting(self):
#         print( '{0} 저는 {1}입니다.'.format(self.hello, self.name) )
    
# maria = Person(**{'name':'마리아', 'age':20, 'power':21})
# maria.greeting()

# print('이름:', maria.name)
# print('나이:', maria.age)
# # print('주소:', maria.addess)


# # 사람 클래스로 학생 클래스 만들기
# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def study(slef):
#         print('공부하기')

# james = Student()
# james.greeting()
# james.study()

# maria = Person()
# maria.greeting()
# maria.study()


# # 상속 관계 확인하기
# class Person:
#     pass
# class Student(Person):
#     pass

# print(issubclass(Student, Person))


# # 기반 클래스의 속성 사용하기
# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         self.school = '파이썬 코딩 도장'

# james = Student()
# print(james.school)
# print(james.hello)


# # super()로 기반 클래스 초기화하기
# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         print('Student __init__')
#         self.school = '파이썬 코딩 도장'

# james = Student()
# print(james.school)
# print(james.hello)


# # 기반 클래스를 초기화하지 않아도 되는 경우
# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     pass

# james = Student()
# print(james.hello)


# # 메서드 오버라이딩 사용하기
# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# james = Student()
# james.greeting()


# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         super().greeting()
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# james = Student()
# james.greeting()


# # 다중 상속 사용하기
# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class University:
#     def manage_credit(self):
#         print('학점 관리')

# class Undergraduate(Person, University):
#     def study(self):
#         print('공부하기')

# james = Undergraduate()
# james.greeting()
# james.manage_credit()
# james.study()


# # 다이아몬드 상속
# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')

# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')

# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')

# class D(B, C):
#     pass

# x = D()
# x.greeting()

# print(D.mro())


# # 추상 클래스 사용하기
# from abc import*

# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass

#     @abstractmethod
#     def go_to_school(self):
#         pass

# class Student(StudentBase):
#     def study(self):
#         print('공부하기')

# james = Student()
# james.study()


# from abc import*

# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass

#     @abstractmethod
#     def go_to_school(self):
#         pass
    
# class Student(StudentBase):
#     def study(self):
#         print('공부하기')
#     def go_to_school(self):
#         print('학교가기')

# james = Student()
# james.study()
# james.go_to_school()


# 추상 메서드를 빈 메서드로 만드는 이유
maria = StudentBase()