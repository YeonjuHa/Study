# 2차원 리스트를 만들고 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print( a )

b = [[10, 20],
     [30, 40],
     [50, 60]]
print( b )


# 2차원 리스트의 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print(a)    # 전체 출력
print( a[0] )    # 행단위 출력
print( a[1] )    # 행단위 출력
print( a[2] )    # 행단위 출력

print( a[0][0] )
print( a[1][1] )
print( a[2][1] )

a[0][1] = 1000
print(a[0][1])
print(a)


# 톱니형 리스트
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
print(a)

b = []
b.append([])
b[0].append(10)
b[0].append(20)

b.append([])
b.append(500)
b.append(600)
b.append(700)
print(b)


# 사람이 알아보기 쉽게 출력하기
a = [[10, 20], [30, 40], [50, 60]]
print(a)

from pprint import pprint
pprint(a, indent=4, width=20)


# for 반복문을 한 번만 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in a:
    print(i)

for x, y in a:
    print(x, y)


# for 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print()


# for와 range 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for i in range(len(a)):           # 세로 크기
    for j in range(len(a[i])):    # 가로 크기
        print(a[i][j], end=' ')
    print()


# while 반복문을 한 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

print()
# while 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1


# 반복문으로 리스트 만들기
# for 반복문으로 1차원 리스트 만들기
a = []

for i in range(10):
    a.append(0)

print(a)

# for 반복문으로 2차원 리스트 만들기
a= []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)


# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)

b = [[0] * 2 for i in range(3)]
print(b)


# 톱니형 리스트 만들기
a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)

print()

a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(b)


# 2차원 리스트의 할당과 복사 알아보기
# 할당
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print('a리스트', a)
print('b리스트', b)

print()
# 복사
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print('a리스트', a)
print('b리스트', b)

print()
# deepcopy
a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print('a리스트', a)
print('b리스트', b)