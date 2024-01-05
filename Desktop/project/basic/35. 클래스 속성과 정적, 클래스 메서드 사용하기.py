# # 클래스 속성과 인스턴스 속성 알아보기
# # 클래스 속성 사용하기
# class Person:
#     bag = []    # 객체 관계 없이 공통 사용

#     def put_bag(self, stuff):
#         self.bag.append(stuff)

# james = Person()    # james 객체 생성
# maria = Person()    # maria 객체 생성
# james.put_bag('책')
# maria.put_bag('열쇠')

# print(james.bag)
# print(maria.bag)



# class Person:
#     bag = []    # 객체 관계 없이 공통 사용

#     def put_bag(self, stuff):
#         Person.bag.append(stuff)

# james = Person()    # james 객체 생성
# maria = Person()    # maria 객체 생성
# james.put_bag('책')
# maria.put_bag('열쇠')

# print(Person.bag)


# print(james.__dict__)
# print(Person.__dict__)


# # 인스턴스 속성 사용하기
# class Person:
#     def __init__(self):
#         self.bag = []    # 객체 관계 없이 공통 사용

#     def put_bag(self, stuff):
#         self.bag.append(stuff)

# james = Person()    # james 객체 생성
# maria = Person()    # maria 객체 생성
# james.put_bag('책')
# maria.put_bag('열쇠')

# print(james.bag)
# print(maria.bag)


# # 비공개 클래스 속성 사용하기
# class Knight:
#     __item_limit = 10   # 비공개 클래스 속성

#     def print_item_limit(self):
#         print(Knight.__item_limit)

# x = Knight()
# x.print_item_limit()    # 10 출력

# print(Knight.__item_limit)  # 에러


# # 클래스와 메서드의 독스트링 사용하기
# class Person:
#     '''사람 클래스입니다.'''

#     def greeting(self):
#         '''인사 메서드입니다.'''
#         print('Hello')

# print(Person.__doc__)
# print(Person.greeting.__doc__)

# maria = Person()
# print(maria.greeting.__doc__)


# # 정적 메서드 사용하기
# class Calc:
#     @staticmethod
#     def add(a, b):
#         print(a + b)
    
#     @staticmethod
#     def mul(a, b):
#         print(a * b)

# Calc.add(10, 20)
# Calc.mul(10, 20)




# 클래스 메서드 사용하기
class Person:
    count = 0

    def __init__(self):
        Person.count += 1
    
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()