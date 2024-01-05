# 불
True
False

# 비교 연산자(<, >, <=, >=, ==)
3 > 1
3 < 1
10 == 10 # 같은지 비교
10 != 5 # 다른지 비교

result = 3>1
result


# 객체 비교
1 == 1.0
1 is 1.0
1 is not 1.0

'cat' == 'cat'
'cat' is 'cat'


# 값 비교에 is 쓰지 않기
a = -5 # 변수 a에 정수 -5를 할당
a is -5 # 변수 a와 정수 -5의 객체를 비교(같은지)
id(a) 
id(-5)

a = -6 # 변수 a의 값을 정수 -6으로 재할당
a is -6
id(a)
id(-6)


a = 5
id(a), id(5)

a = 6
id(a), id(6)

a = -5
id(a), id(-5)

a = -6   # 많이 사용하는 숫자의 경우 미리 메모리에 저장해두기 때문에 위 3숫자는 id가 같아 보임
id(a), id(-6)



# 논리연사자 사용하기
# and
True and True
True and False
False and True
False and False

True & False

# or
True or True
True or False
False or True
False or False

True | False
False | False

# not
not True
not False

not True and False or not False # not, and, or 순으로 해석
( (not True) and False) or (not False)

# 논리 연산자와 비교 연산자를 함께 사용하기
10 == 10 and 10 != 5
10 > 5 or 10 < 3
not (10 > 5)
not (1 is 1.0)

# 정수, 실수, 문자열을 불로 만들기
# 값이 있으면 True, 없으면 False
bool(1) #T
bool(0) #F
bool(1.5) #T
bool('False') #T
bool('') #F
bool(' ') #T 공백도 값이 있는 것


# 0 -> False, 1 -> True
bool(0), bool(1)

# 값이 있으면 True, 없으면 False
bool(10), bool('A'), bool('cat'), bool('     ')
bool(''), bool(""), bool("""""")

# bool 값이 True면 True, False면 False
bool(True), bool(False)

bool(true)
bool('False')


# 단락평가
print(False and True) #F
print(False and False) #F

print(True or True) #T
print(True or False) #





# id 함수
# 객체를 입력 받아 그 객체의 고유값(레퍼런스->참조 주소)을 반환한다
#id
# 파이썬이 객체를 구별하기 위해 부여하는 일련번로(숫자로서 의미는 없음)
# -> 이것을 이용 동일한 객체인지 판별
# 객체 수명 동안 유일하고 바뀌지 않음

a =10    # 변수 a에 정수 10을 할당
b = 20    # 변수 b에 정수 20을 할당
a == b    # 객체 a와 객체 b를 비교(객체 비교)
a is b


b = a    # 변수 a의 값을 변수 b에 할당(변수 b에 값을 재할당)
a == b #T
a is b #T



a = 1
b = 2
id(a), id(1)
id(b), id(2)

c = 2
id(c), id(2)

d = -5
id(d), id(-5)

e = -6
id(e), id(-6)

f = -6
id(f), id(-6)



