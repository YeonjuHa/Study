# 10 진수와 2진수 변환하기
bin(13)
0b1101

int('1101', 2)

# 비트 논리 연산자 사용하기
bin(0b1101 & 0b1001)
13 & 9
bin(0b1101 | 0b1001)
13 | 9
bin(0b1101 ^ 0b1001)
13 ^ 9
bin(~0b1101)
~13

# bytes
bytes(10)
bytes([10, 20, 30, 40, 50])
bytes(b'hello')

# bytearray
x = bytearray(b'hello')
x[0] = ord('a')
x

# 바이트 자료형과 인코딩
'hello'.encode()
'안녕'.encode('euc-kr')
'안녕'.encode('utf-8')

b'hello'.decode()
b'\xbe\xc8\xb3\xe7'.decode('euc-kr')

# 날짜/시간 모듈 활용하기
import time
time.time()

time.localtime(time.time())

time.strftime('%Y-%m-%d', time.localtime(time.time()))
time.strftime('%c', time.localtime(time.time()))


import datetime
datetime.datetime.today()

pip install pytz
datetime.datetime.now(pytz.timezone('UTC'))


# 특정 날짜와 시간으로 객체 만들기
d = datetime.datetime(2023, 11, 1)
d

d = datetime.datetime.strptime('2023-11-01', '%Y-%m-%d')
d

d.strftime('%Y-%m-%d')
d.strftime('%c')

today = datetime.datetime.today()
today.year, today.month, today.day, today.hour, today.minute, today.second, today.microsecond

d = datetime(2023, 11, 1)
from datetime import timedelta
d - timedelta(days=20)
d + timedelta(days=20)


# 내장 함수
all([1, 2, 3, 'cat'])
all([1, 2, 3, 'cat', False])
all([1, 2, 3, 'cat', 0])

chr(65)
chr(97)


# 이스케이프 시퀀스
str1 = "오늘의 메뉴는 '자장면'"
str1
str2 = '오늘의 메뉴는 \'자장면\''
str2


# 실숫값의 오차
0.1 + 0.2

0.1 + 0.2 == 0.3

import math, sys
x = 0.1 + 0.2
math.fabs(x - 0.3) <= sys.float_info.epsilon

import math
math.isclose(0.1 + 0.2, 0.3)


# Decimal으로 정확한 자릿수 표현하기
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')


# Fraction으로 분수 표현하기
from fractions import Fraction
Fraction('10/3')


# 프로퍼티 사용하기
class Person:
    def __init__(self):
        self.__age = 0
    
    def get_age(self):           # getter
        return self.__age
    
    def set_age(self, value):    # setter
        self.__age = value

james = Person()
james.set_age(20)
print(james.get_age())



class Person:
    def __init__(self):
        self.__age = 0
    
    @property
    def age(self):           # getter
        return self.__age
    
    @age.setter
    def age(self, value):    # setter
        self.__age = value

james = Person()
james.age = 20
print(james.age)
