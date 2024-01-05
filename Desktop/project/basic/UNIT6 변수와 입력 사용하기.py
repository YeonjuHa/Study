# 변수 이름 만들기(규칙)
# 1. 영문 문자와 숫자를 사용할 수 있다.
name = 'cat'
name
print(name)

name1 = 'cat'
name2 = 'dog'
name1, name2
print(name1, name2)


# 2. 대소문자를 구분한다.
age = 3
Age = 5
age, Age
print(age, Age)


# 3. 문자부터 시작해야 하고, 숫자부터 시작하면 X
name1 = 'cat'
2name = 'dog'


# 4. _(밑줄)로 시작할 수 있다.
_age = 3
a_ge = 5
ag_e = 6
print(_age, a_ge, ag_e)


# 5. 특수문자(+, -, /, *, &, %) 사용 X
age& = 3


# 6. 파이썬의 키워드(if, for, while, and, or)는 사용 X
if = 'cat'


# 한글은 가능할까?
한글이름 = '야옹이'
한글이름
print(한글이름)


age = 3
AGE = '3'
type(age)
type(AGE)
print( age + 1 )
#print( AGE + 1 )
print( int(AGE) + 1 )


AGE1 = '3'
AGE2 = int(AGE1)
print( type(AGE2) )




# 6.1.2 변수 여러 개를 한 번에 만들기
x , y, z = 10, 20, 'cat'
print(x, y, z)

#x, y, z = 10, 20
#print(x, y, z)

x = y = z = 10
print(x, y, z)
x = x + 1
print(x)

# 두 변수의 값을 바꾸고 싶을 때
x , y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

x , y = 10, 20
x = y
y = x
print(x, y)


# 변수 삭제하기
x = 10
print(x)
del x
print(x)


# 빈 변수 만들기
x = None
print(x)
x


# 변수로 계산하기
a = 10
b = 20
c = 10 + 20
print(c)
d = a + b
print(d)
#a = 10, b =20

a= 10
print( a + 20 )
print(a)


a = 10
print(a)
a = a + 20
print(a)


a = 10
a += 20    # a = a + 20
print(a)

x = -10
x
+x
-x


# 복합 연산자(두 개의 연산자가 같이 묶여서 사용)
a = 10
a += 20    # a = a + 20
print(a)
a -= 5    # a = a - 5
print(a)
a *= 2    # a = a * 2
print(a)



# 6.3 입력값을 변수에 저장하기
input()
Hello, world!

x = input()
Hello, world!
print(x)


# 6.3.3 두 숫자의 합 구하기
a = input('첫 번째 숫자를 입력하세요:')
b = input('두 번째 숫자를 입력하세요:')
print( a + b )


# 6.3.4 입력 값을 정수로 변환하기
a = int( input('첫 번째 숫자를 입력하세요:') )
b = int( input('두 번째 숫자를 입력하세요:') )
print( a + b )


a = input('첫 번째 숫자를 입력하세요:')
b = input('두 번째 숫자를 입력하세요:')
print( int(a) + int(b) )



# 입력 값을 변수 두개에 저장하기
a, b = input( ' 문자열 두 개를 입력하세요: ' ).split()
print(a)
print(b)

a, b = input().split()
a, b = input().split(',')
a, b = input( ' 문자열 두 개를 입력하세요: ' ).split()
a, b = input( ' 문자열 두 개를 입력하세요: ' ).split(',')

a, b, c = input( '휴대번호 입력: ' ).split('-')



# 입력 값을 정수로 변환시키기
a, b = input('숫자 두 개를 입력하세요: ').split()
a = int(a)
b = int(b)

print( a + b )



# map을 사용하여 정수로 변환하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)


# 입력받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(','))
print(a + b)



