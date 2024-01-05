tup1 = (4, 5, 6)
tup1

tup2 = 4, 5, 6
tup2

tup3 = tuple([4, 0, 2])
tup3

tup4 = tuple('string')
tup4


# 튜플의 튜플을 생성
nested_tup = (4, 5, 6), (7, 8)
nested_tup
nested_tup[0]
nested_tup[1]
nested_tup[0][0]


tup = tuple(['foo', [1, 2], True])
tup
tup[2] = False

# 중요
tup[1].append(3)
tup
tup[1][2]
tup[1][2] = 30
tup

(4, None, 'foo') + (6, 0) + ('bar',)

t = 10
t
t = 20
t
t = (10,)
t
t[0]
t[0] = 20

('foo', 'bar') * 4


# 튜플에서 값 분리하기
tup1 = (4, 5, 6)
a, b, c = tup1
tup1
a, b, c

tup2 = 4, 5, (6, 7)
a, b, (c, d) = tup2
tup2
a, b, c, d

tup3 = 4, 5, (6, 7)
a, b, c = tup3
tup3
a, b, c


a, b = 1, 2
a
b

b, a = a, b
a
b

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')

values = 1, 2, 3, 4, 5
a, b, *rest = values
a
b
rest

a, b, *_ = values
a
b
_


# 튜플 메서드
