# 17. whlie 반복문으로 Hello, world! 100번 출력하기
# while 반복문
i = 0       # 초기식(= 변수의 초기화)
while i < 5:
    print('Hello, world!', i)
    i += 1      # i = i + 1(i 값을 1 증가)

print()
# for 반복문
for i in range(5):
    print('Hello, Python!', i)

# 무한 반복(ctrl+c 중지)
# 참인 값은 무한 반복(문자열, 숫자, True)
#i = 0       
#while True:
#    print('Hello, world!', i)
#    i += 1

# 거짓인 값은 실행 X
i = 0
while False:
    print('Hello, Python!')
    i += 1


print()
# 초깃값을 1부터 시작하기
i = 1
while i <= 5:
    print('Hello, world!', i)
    i += 1 

print()
# 초깃값을 감소시키기
i = 5
while i >= 1:
    print('Hello, world!', i)
    i -= 1      # i = i - 1

print()
# 입력한 횟수대로 반복하기
x = int(input('반복할 횟수를 입력하세요: '))
i = 0

while i < x:
   print('Hello, world!', i)
   i += 1


print()
# 반복 횟수가 정해지지 않은 경우
# random 모듈 임포트
import random

# 난수 만들기
print( random.random() )
print( random.random() )

print()
# 정수인 난수
print(random.randint(1, 6))
print(random.randint(1, 6))


print()
import random

i = 0
while i != 3:      # 3이 아닐 때까지 계속 반복(즉, 3이 나오면 stop)
    i = random.randint(1, 6)
    print(i)

print()
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
print(random.choice(dice))

# 로또 번호
import random

for j in range(5):      # 5번 반복
    print()     # 한 줄 띄우기

    for i in range(6):      # 번호 6개
        r = random.randint(1, 45)
        print(r, end=' ')


# 여러 값 중에 하나 선택 choice
import random

dice = ['cat', 'dog', '짜장면', '짬뽕', '탕수육']

print(random.choice(dice))