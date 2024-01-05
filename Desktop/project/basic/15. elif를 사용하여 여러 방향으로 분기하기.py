# 1. elif 사용하기
x = 20
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')



# 1) if, elif, else를 모두 사용하기
x = 30

if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

# elif 앞에 else가 오면 잘못된 문법
if x == 10:
   print('10입니다.')
else:
   print('10도 20도 아닙니다.')
elif x == 20:
   print('20입니다.')


# 2) 음료수 자판기 만들기
button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')


# None과 False는 같은가?
print( None == False )
print( None is False )


# if 조건문만 사용할 때 elif를 사용할 때 차이점
# if만
a, b, c = 10, 20, 30

if a == 10:
    print('10')
if b == 20:
    print('20')
if c == 30:
    print('30')

# if, elif
if a == 10:
    print('10')
elif b == 20:
    print('20')
elif c == 30:
    print('30')


a, b, c = 5, 20, 30
if a == 10:
    print('10')
elif b == 20:
    print('20')
elif c == 30:
    print('30')