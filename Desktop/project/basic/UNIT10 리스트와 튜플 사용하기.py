# 리스트 만들기
a = 38; b = 21; c = 53; d = 62; e = 19
print(a, b, c, d, e)

x = [38, 21, 53, 62, 19]
print(x)


# 리스트에 여러 가지 자료형 저장하기
person = ['james', 17, 175.3, True]
person


# 빈 리스트 만들기
a = []
a

b = [    ]
b

c = list()
c


# range를 사용하여 리스트 만들기
# 0~9까지 "연속적인" 정수를 생성
range(10)

a = list( range(10) )
a
print(a)


b = list( range(5, 12) )
b
print(b)

c = list( range(-4, 10, 2) )
c
print(c)

d = list( range(10, 0, -1) )
d
print(d)


print( list( range(10, 15+1) ) )

print( list( range('a', 'z' ) ) )
print( list( range(1.0, 2.5) ) )


# 튜플 사용하기
a = (38, 21, 53, 62, 19)
a
print(a)

a = 38, 21, 53, 62, 19
a
print(a)

person = ('james', 17, 175.3, True)
person
print(person)


# 요소가 한 개 들어있는 튜플 만들기
a = (38)
a
print(a)

b = (38, )
b
print(b)

c = 38,
c
print(c)


# 리스트 만들기
# 10, 20, 30, 40, 50
a = [10, 20, 30, 40, 50]
a
print(a)

b = list( [10, 20, 30, 40, 50] )    # list( (10, 20, 30, 40, 50) )도 가능
b
print(b)

c = list( range(10, 50+1, 10) )
c
print(c)

# 튜플 만들기
#10, 20, 30, 40, 50
d = (10, 20, 30, 40, 50)
d
print(d)


e = 10, 20, 30, 40, 50
e
print(e)

f = tuple( (10, 20, 30, 40, 50) )    # tuple( [10, 20, 30, 40, 50] )도 가능
f
print(f)


# 리스트 + range()
x = list( range(10) )
x
print(x)

# 튜플 + ranege()
y = tuple( range(10) )
y
print(y)


# 나중에 배울 내용
a = [10, 20, 30]
print(a)
a[0] = 100
print(a)

# 튜플에서는 변경 불가 
#b = (10, 20, 30)
#print(b)
#b[0] = 100
#print(b)

# 리스트를 튜플로 변환
a = [10, 20, 30, 40, 50]
b = tuple( [10, 20, 30, 40, 50] )
print(b)

c = tuple(a)
print(c)



# list와 tuple 안에 문자열을 넣으면?
print( list('Hello') )
print( tuple('Python') )



# 리스트와 튜플로 변수 만들기
a, b, c = [1, 2, 3]
print(a, b, c)
d, e, f = (4, 5, 6)
print(d, e, f)

# 언패킹
x = [1, 2, 3]
a, b, c = x
print(a, b, c)
y = (4, 5, 6)
d, e, f = y
print(d, e, f)


input().split()
x = input().split()
a, b = x
print(x)
print(a, b)













