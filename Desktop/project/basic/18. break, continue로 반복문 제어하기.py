# # break로 반복문 끝내기
# # 1) while에서 break로 반복문 끝내기
# i = 0       # 변수 초기화
# while True:     # 참인 동안 반복(무한)
#     print(i)
#     i += 1
#     if i == 5:
#         print('중지 STOP!')
#         break

# print()
# # 2) for에서 break로 반복문 끝내기
# for i in range(10000):
#     print(i)
#     if i == 5:
#         print('중지 STOP!')
#         break


# # continue로 코드 실행 건너뛰기
# # 1) for에서 continue로 코드 실행 건너뛰기
# for i in range(5):
#     if i % 2 == 0:      # 짝수이면
#         print(i, '짝수>통과')
#         continue        # 그냥 지나감
#     print(i)            # i 값 출력(홀수만)

# print()
# # 2) while 반복문에서 continue로 코드 실행 건너뛰기
# i = 0
# while i < 5:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# print()
# 입력한 횟수대로 반복하기
# count = int(input('반복할 횟수를 입력하세요: '))

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == count:
#         break


# for j in range(0, count):
#     print(j)
#     j += 1
#     if j == count:
#         break


# print()
# # 1) 입력한 숫자까지 홀수 출력하기
# count = int(input('반복할 횟수를 입력하세요: '))

# for i in range(count):
#     if i % 2 == 0:
#         continue
#     print(i)


# 키보드로 정수 하나를 입력 받는다.
# 입력 받은 정수가 짝수이면 '짝수'
# 홀수이면 '홀수'라고 화면에 출력한다.
count = int(input('정수 하나를 입력하세요: '))


if count % 2 == 0:
    print(count, '짝수')
else:
    print(count, '홀수')

for i in range(count):
    if i % 2 == 0:
        print(i, '짝수')
    if i % 2 == 1:
        print(i, '홀수')
    if i == count:
        break


# # 1. 키보드로 정수 하나를 입력 받는다.
# # 2. 입력 받은 정수가 짝수이면 '짝수'
# # 3. 홀수이면 '홀수'라고 화면에 출력한다.
# # 1~3 과정을 반복한다.
# # 단, 입력한 숫자가 0이면 '중단' 메시지를 출력하고 종료한다.

# while True:     # 무한루프
#     x = int(input('정수 하나를 입력하세요: '))      # 입력 받은 숫자 출력

#     if x == 0:
#         print('중단')
#         break
#     elif x % 2 == 0:
#       print(x, '짝수')
#     else:
#         print(x, '홀수')
