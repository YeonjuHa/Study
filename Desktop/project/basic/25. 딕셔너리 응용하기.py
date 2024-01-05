# 딕셔너리 복습
d1 = dict(name='cat', age=3)
d1

d2 = dict(zip(['name', 'age'], ['cat', 3]))
d2

d3 = dict([('name', 'cat'), ('age', 3)])
d3

d4 = dict({'name':'cat', 'age':3})
d4


# 딕셔너리에 키와 기본값 저장하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
x

x.setdefault('f', 100)
x

# 딕셔너리에서 키의 값 수정하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
x

x.update(e=50)
x

x.update(a=900, f=60)
x

y = {1: 'one', 2: 'two'}
y.update({1: 'one', 3: 'THREE'})
y

y.update([[2, 'TWO'], [4, 'FOUR']])
y

y.update(zip([1, 2], ['one', 'two']))
y

# 딕셔너리에서 키-값 쌍 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a')
x

x.pop('z', 0)
x

x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['a']
x

# 중복되는 것 모두 삭제
x = {'a':10, 'a':10.0, 'b':20, 'c':30, 'd':40}
x.pop('a')
x

# 딕셔너리에서 임의의 키-값 쌍 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.popitem()
x

# 딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.clear()
x

# 딕셔너리에서 키의 값을 가져오기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.get('a')

x.get('z', 100)

# 딕셔너리에서 키-값 쌍을 모두 가져오기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.items()
x.keys()
x.values()

# 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
x

y = dict.fromkeys(keys, 100)
y


# 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
# 키만 출력됨
x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i, end=' ')

# 모든 키와 값 출력
x = {'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    print(key, value)

x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x.items():
    k, y = i
    print(k, y)

# 딕셔너리의 키만 출력하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
for key in x.keys():
    print(key, end=' ')

# 딕셔너리의 값만 출력하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
for value in x.values():
    print(value, end=' ')    

# 딕셔너리 표현식 사용하기
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
x

# 키만 가져옴
{key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
# 값을 키로 사용
{value: 0 for value in {'a':10, 'b':20, 'c':30, 'd':40}.values()}
# 키-값 자리를 바꿈
{value: key for key, value in {'a':10, 'b':20, 'c':30, 'd':40}.items()}


# 딕셔너리 표현식에서 if 조건문 사용하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    if value == 20:
        del x[key]

# 표현식으로 작성
x = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key: value for key, value in x.items() if value != 20}
x


# 딕셔너리 안에서 딕셔너리 사용하기
terrestrial_planet = {
    'Mercury' : {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus' : {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069
    },
    'Earth' : {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641
    },
    'Mars' : {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600
    }
}

print(terrestrial_planet['Venus']['mean_radius'])


# 딕셔너리의 할당과 복사
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
x is y
y['a'] = 99
x
y

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
x is y
x == y
y['a'] = 99
x
y

# 중첩 딕셔너리의 할당과 복사 알아보기
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'
x
y

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
x
y