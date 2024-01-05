# 중첩 루프 사용하기
# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep='', end=' ')
#     print('i:', i, sep='')


# for i in range(5):
#     for j in range(5):
#         print(j, end=' ')
#     print('index: ', i)


# # 사격형으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()     # 빈 행(줄바꿈)


# print()
# # 사각형 모양 바꾸기
# for i in range(3):
#     for j in range(7):
#         print('*', end='')
#     print()


# # 계단식으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print('*', end='')
#     print()


# 대각선으로 별 출력하기
# 일자로 먼저 출력해보기(왼쪽 위>아래)
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#     print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()