# 1. for과 raneg 사용하기
#for i in range(100):
#    print('Hello, world!')


#range(100)
#print(range(100))
#print( list( range(100)))


for i in [0, 1, 2, 3, 4]:
    print('Hello, Python!')

print()    # 공백

for i in (0, 1, 2, 3, 4):
    print('Hello, world!')

print()    # 공백

for i in 'hello':
    print(i)
    print('Hello, Python!')

print()    # 공백

for i in range(5):
    print(i, 'Hello, world', sep='')

print()    # 공백

for i in range(5):
    print(i, end='')
    print('Hello, world')


# 시작하는 숫자와 끝나는 숫자 지정하기
print()    # 공백

for i in range(5, 12):
    print('Hello, world!', i)


# 증가폭 사용하기
print()    # 공백

for i in range(0, 10, 2):
    print('Hello, wolrd!', i)


# 숫자를 감소시키기
print()    # 공백

for i in range(10, 0, -1):
    print('Hello, world!', i)


print()    # 공백

for i in range(10, 0, -3):
    print('Hello, world!', i)

# reversed 사용
print()

for i in reversed(range(10)):
    print('Hello, world!', i)


# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)


# 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

print()

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

print()

for letter in 'Python':
    print(letter, end=' ')

print()

for letter in reversed('Python'):
    print(letter, end=' ')

print()

name = 'Python'
print(len(name))    # 문자열의 크기(길이) 출력

for letter in range(len(name)):
    print( 'name' + '[' + str(letter) + ']')