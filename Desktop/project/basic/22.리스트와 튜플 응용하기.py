# 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(500)
a.append('cat')
print(a)
print(len(a))

print()

a = []    # 빈 리스트
a.append(10)
print(a)

print()

a = []
for i in range(5):
    a.append(i)
    print(a)

print()

# 리스트 안에 리스트 추가하기
a = [10, 20, 30]
a.append([500, 600])
a.append(True)
print(a)
print(len(a))
print(a[3])
print(a[3][0])

print()

# 리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

print()

# 리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(0, 500)
print(a)

print()
a = [10, 20, 30]
a.insert(len(a), 500)
print(a)

print()

a = [10, 20, 30]
a.insert(1, [500, 600])
print(a)

print()

a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)


# 리스트에서 요소 삭제하기
# 리스트에서 특정 인덱스의 요소를 삭제하기
a = [10, 20, 30]
a.pop()
print(a)

print()

a = [10, 20, 30]
a.pop(1)
print(a)

print()

a = [10, 20, 30]
del a[1]
print(a)


# 리스트에서 특정 값을 찾아서 삭제하기
print()

a = [10, 20, 30]
a.remove(20)
print(a)

a = [10, 20, 30, 20]
a.remove(20)
print(a)

print()

# 리스트 a의 요소 20을 모두 제거
a = [10, 20, 30, 20]

print( list(range(len(a)-1)) )

for i in range(len(a) - 1):
    if a[i] == 20:
        a.pop(i)
        print(len(a), a)


# 리스트로 스택과 큐 만들기
from collections import deque
a = deque([10, 20, 30])
print(a)

print()
a.append(500)
print(a)

print()
a.popleft()
print(a)

# 리스트에서 특정 값의 인덱스 구하기
print()
a = [10, 20, 30, 15, 20, 40]
print (a.index(20), '번 인덱스', sep='')

# 특정 값의 개수 구하기
print()
a = [10, 20, 30, 15, 20, 40]
print(a.count(20), '개 있음', sep='')


# 리스트의 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)


# 리스트의 요소를 정렬하기
a = [10, 20, 30, 15, 20, 40]
a.sort()    # 오름차순
print(a)

print()
a = [10, 20, 30, 15, 20, 40]
a.sort(reverse=False)    # 오름차순
print(a)

print()
a = [10, 20, 30, 15, 20, 40]
a.sort(reverse=True)    # 내림차순
print(a)

# sort 메서드와 sorted 함수
a = [10, 20, 30, 15, 20, 40]
a.sort()    # 원본 변경
print(a)

b = [10, 20, 30, 15, 20, 40]
print( sorted(b) )    # 원본  변경 안됨
print(b)

print()
# reverse 메서드와 reversed 함수
a = [10, 20, 30, 15, 20, 40]
a.reverse()    # 원본 변경
print(a)

b = [10, 20, 30, 15, 20, 40]
print( reversed(b) )    # 원본  변경 안됨
print(b)


# 리스트의 모든 요소를 삭제하기
a = [10, 20, 30]
a.clear()
print(a)

b = [10, 20, 30]
del b[:]
print(b)

c = [10, 20, 30]
del c[0:len(c)]
print(c)


# 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

b = [10, 20, 30]
b.append(500)
print(b)

c = [10, 20, 30]
c.extend([500])
print(c)


print()
a = [10, 20, 30]
a[len(a):] = [400, 500, 600]
print(a)

b = [10, 20, 30]
b.extend([400, 500, 600])
print(b)


# 리스트가 비어 있는지 확인하기
seq = [10, 20, 30]
if len(seq):
    print('비어 있지 않음')
else:
    print('비어 있음')

print()
seq = []
if len(seq):
    print('비어 있지 않음')
else:
    print('비어 있음')

print()
seq = [10, 20, 30]
print( seq[0], seq[-3] )
print( seq[2], seq[-1], seq[len(seq)-1] )


# 리스트의 할당과 복사 알아보기
a = [0, 0, 0, 0, 0]
b = a
print( a is b )     # 객체 a와 객체 b가 같은지 비교

b[2] = 99    # 객체 b의 2번 인덱스 값을 99로 재할당
print( a )
print( b )


a = [0, 0, 0, 0, 0]
b = a.copy()    # 객체 a를 복사해서 객체 a에 할당

print( a is b )     # 객체 a와 객체 b가 같은지 비교
print( a == b )     # 객체 a의 값과 객체 b가 같은지 비교

b[2] = 99
print( a )
print( b )


# 반복문으로 리스트의 요소를 모두 출력하기
# 객체 a의 요소값을 하나씩 i에 전달
a = [38, 21, 53, 62, 19]
for i in a:
    print(i, end = ', ')    # 요소값을 출력

print()

for i in [38, 21, 53, 62, 19]:
    print(i, end=', ')    # 요소값을 출력



# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

print()

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print( str(index + 1) + '번', value)

print()

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a, start = 10):
    print(str(index) + '번', value)

# for 반복문에서 인덱스로 요소를 출력하기
a = [38, 21, 53, 62, 19]

# 인덱스 번호를 가져오기
for i in range(len(a)):
    print(i, end=' ')
print()

# 요소값 가져오기
for i in a:
    print(i, end=' ')

print()

# 인덱스와 요소값 동시에 가져오기
for i, v in enumerate(a):
    print(i, v)


# while 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1

print()

a = [38, 21, 53, 62, 19]
i = 0
while i <= len(a):
    print(a[i])
    i += 1


# 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]

smallest = a[0]
for i in a :
    if i < smallest:
        smallest = i

print('가장 작은 수 = ', smallest)


largest = a[0]
for j in a:
    if j > largest:
        largest = j

print('가장 큰 수 = ', largest)


a = [38, 21, 53, 62, 19]
a.sort()
print(a)
print( a[0] )    # 가장 작은 수
print( a[-1] )    # 가장 큰 수

a.sort(reverse=True)
print( a[0] )    # 가장 큰 수
print( a[-1] )    # 가장 작은 수

print(min(a))    # 가장 작은 수
print(max(a))    # 가장 큰 수


# 요소의 합계 구하기
a = [38, 21, 53, 62, 19]
x = 0    # 변수 초기화
for i in a:
    x += i

print(x)

a = [38, 21, 53, 62, 19]
print( sum(a) )


# 리스트 표현식 사용하기
a = [i for i in range(10)]
print(a)

x = []
for i in range(10):
    x.append(i)

print(x)

b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]
print(c)

d = list( i * 2 for i in range(10) )
print(d)


# 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]
print(a)

x = []
for i in range(10):
    if i % 2 == 0:
        x.append(i)
print(x)

b = [i + 5 for i in range(10) if i % 2 == 1]
print(b)


# for 반복문과 if 조건문을 여러 번 사용하기
a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a)


# 리스트에 map 사용하기
a = [1.2, 2.5, 3.7, 4.6]
# 실수를 정수로 바꾸기
print( a[0], '=>', int(a[0]) )

print()
# 모두 정수로 바꾸기
for i in range(len(a)):
    print( a[i], '=>', int(a[i]))

print()

a = list( map(int, a) )
print(a)


# input().split()과 map()
a = input('값 입력: ').split()
print(a)

a = map(int, input('값 입력: ').split())
print(a)
print( list(a) )


a, b = [10, 20]
print(a)
print(b)

a, b = map( int, input().split() )
print(a, b)

x = input().split()
m = map(int, x)
a, b = m



# 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
print( a.index(53) )

# 특정 값의 개수 구하기
a = (10, 20, 30, 12, 20, 40)
print( a.count(20) )

# for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19, 53)
for i in a:
    print(i, end=' ')


# 튜플 표현식 사용하기
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

print( (i for i in range(10) if i % 2 == 0) )    # 제너레이터 형식으로 나옴


# tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)


# 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19, 53)
print( min(a) )
print( max(a) )
print( sum(a) )