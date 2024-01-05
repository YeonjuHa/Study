# square2.py
base = 2
def square(n):
    return base ** n

# square2_main.py
import square2

print(square2.base)
print(square2.square(10))

# 변수, 함수 가져오기
from square2 import base, square
print(base)
square(10)


# 모듈에 클래스 작성하기
# person.py
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))
    
# person_main.py
import person
maria = person.Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

# hello.py
print('hello 모듈 시작')
print('hello.py __name__:', __name__)
print('hello 모듈 끝')

import hello

print('hello.py __name__:', __name__)

# 45.3.3
from calcpkg.opertation import add, mul
add(10, 20)
mul(10, 20)