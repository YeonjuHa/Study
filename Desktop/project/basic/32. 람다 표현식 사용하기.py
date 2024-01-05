# 람다 표현식 사용하기
# 람다 표현식으로 함수 만들기
# 함수식
def plus_ten(x):
     return x + 10

plus_ten(1)


# 람다 표현식
lambda x: x + 10

plus_ten = lambda x: x + 10
plus_ten(1)

# 람다 표현식 자체를 호출하기
(lambda x: x + 10)(1)

# 람다 표현식 안에서는 변수를 만들 수 없다
(lambda x: y = 10; x + y)(1)

y = 10
(lambda x: x + y)(1)
(lambda x, y: x + y)(1, 2)


# 람다 표현식을 인수로 사용하기
# 함수식
def plus_ten(x):
     return x + 10

list(map(plus_ten, [1, 2, 3]))

# 람다 표현식
list(map(lambda x: x + 10, [1, 2, 3]))


# 람다 표현식으로 매개변수가 없는 함수 만들기
(lambda : 1)()

x = 10
(lambda : x)()

# 함수식
def hello():
     return 1

x = hello()
print(x)

# 람다 표현식에서 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list( map(lambda x: str(x) if x % 3 == 0 else x, a) )


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_a = []
for i in a:
    if (i % 3) == 0:
        list_a.append(str(i))
    else:
        list_a.append(i)

print(list_a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list( map( lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a ) )


# 반복문
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_a = []
for i in a:
    if i == 1:
        list_a.append(str(i))
    elif i == 2:
        list_a.append(float(i))
    else:
        list_a.append( i + 10 )

print(list_a)

# 함수식
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( list(map(f, a)) )

# map에 객체 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8]
list( map(lambda x, y: x * y, a, b) )

# filter 사용하기
def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))

# 람다 표현식
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list( filter(lambda x: x > 5 and x < 10, a) )


# reduce 사용하기
def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a)

# 람다 표현식
a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(lambda x, y: x + y, a)


# map, filter, reduce와 리스트 표현식
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
[i for i in a if i > 5 and i < 10]

a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a)-1):
    x = x + a[i + 1]

x