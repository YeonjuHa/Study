# 손님이 돈을 내고 주문을 하면 복권을 발행(복권 번호 출력) 해주고, 거스름돈을 내준다.
# 1회 게임 금액은 1,000원이다.
import random

x = int(input('금액입력: '))       # 손님이 준 돈
y = int(input('게임횟수: '))       # 손님이 희망한 게임 횟수
g = 1000                # 1 게임당 금액
z = x - ( g * y )    # 거스름돈


# 복권 발행
for i in range(y):
    print('복권 발행: ', end='')
    for j in range(6):
        lotto = random.randint(1, 45)     # 중복 없는 난수 생성
        print(lotto, end=' ')

    print()

print('받은금액: ', x)
print('거스름돈', z)
