# 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
fruits

fruits = {'orange', 'orange', 'cherry'}
fruits

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print( fruits[0] )

# 세트에 특정 값이 있는지 확인하기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
'orange' in fruits
'peach' in fruits

'prach' not in fruits
'orange' not in fruits

# set를 사용하여 세트 만들기
a = set('apple')
a
b = set(range(5))
b
c = set()
c

c1 = {}
type(c1)
c2 = set()
type(c2)

# 한글 문자열을 세트로 만들기
set('안녕하세요')

# 세트 안에 세트 넣기
a = {{1, 2}, {3, 4}}
b = {[1, 2], [3, 4]}

# 집합 연산 사용하기
# 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
set.union(a, b)

# 교집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a & b
set.intersection(a, b)

# 차집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a - b
b - a
set.difference(a, b)
set.difference(b, a)

# 대칭차집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a ^ b
set.symmetric_difference(a, b)


# 집합 연산 후 할당 연산자 사용하기
# 합집합
# 집합 연산을 한 후에 할당연산
a = {1, 2, 3, 4}
b = {5}
c = a | b
c

# 간단히 다시 쓰면
a = {1, 2, 3, 4}
a |= {5}             # 집합 a에 {5}를 |(합집합)연산 후 할당
a
a = {1, 2, 3, 4}
a.update({5})
a

# 교집합
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
a
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
a

# 차집합
a = {1, 2, 3, 4}
a -= {3}
a
a = {1, 2, 3, 4}
a.difference_update({3})
a

# 대칭차집합
a = {1, 2, 3, 4}
a ^ {3, 4, 5, 6}
a
a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
a

# 부분집합과 상위집합 확인하기
# 부분집합
a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}
a.issubset({1, 2, 3, 4, 5})

# 진부분집합
a = {1, 2, 3, 4}
a < {1, 2, 3, 4, 5}

# 상위집합
a = {1, 2, 3, 4}
a >= {1, 2, 3, 4}
a.issuperset({1, 2, 3, 4})

# 진상위집합
a = {1, 2, 3, 4}
a > {1, 2, 3}


# 세트가 같은지 다른지 확인하기
a = {1, 2, 3, 4}
a == {1, 2, 3, 4}
a == {4, 2, 1, 3}

# 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
a.isdisjoint({5, 6, 7, 8})
a.isdisjoint({3, 4, 5, 6})


# 세트 조작하기
# 세트에 요소를 추가하기
a = {1, 2, 3, 4}
a.add(5)
a

# 세트에서 특정 요소를 삭제하기
a.remove(3)
a

a.discard(2)
a
a.discard(3)
a
a.remove(3)

# 세트에서 임의의 요소를 삭제하기
a = {1, 2, 3, 4}
a.pop()
a

# 세트의 모든 요소를 삭제하기
a.clear()
a

# 세트의 요소 개수 구하기
a = {1, 2, 3, 4}
len(a)


# 세트의 할당과 복사
a = {1, 2, 3, 4}
b = a
a is b
b.add(5)
a
b

a = {1, 2, 3, 4}
b = a.copy()
a is b
a == b
b.add(5)
a
b


# 반복문으로 세트의 요소를 모두 출력하기
a = {1, 2, 3, 4}
for i in a:
    print(i)


for i in {1, 2, 3, 4}:
    print(i)


# for 반복문을 이용하여 세트 a를 리스트 형태로 변환해보자.
a = {1, 2, 3, 4}
l = []
for i in a:
    print(i)
    l.append(i)

l


# 세트 표현식 사용하기
a = {i for i in 'apple'}
a

# 세트 표현시에 if 조건문 사용하기
a = {i for i in 'pineapple' if i not in 'apl'}
a