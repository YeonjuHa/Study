# 값을 여러 개 출력하기
print(1, 2, 3)
print('Hello', 'Python')


# sep로 값 사이에 문자 넣기
print(1, 2, 3, sep=', ')    # 콤마와 공백을 지정
print(4, 5, 6, sep=',')    # 콤마만 지정
print('Hello', 'Python', sep='')    # 빈 문자열을 지정
print('Hello' + 'Python')
print(1920, 1080, sep='x')    # x를 지정


# 줄바꿈 활용하기
print(1, 2, 3)
print(1, 2, 3, sep='\n')
print('1\n2\n3')
print('1 \n 2 \n 3')

print(1, 2, 3, sep='\t')
print(1, 2, 3, sep='\\')
print('1\t2\t3')
print('1 \\ 2 \\ 3')


# end 사용하기
print(1)
print(2)
print(3)


print(1, end='')
print(2, end='')
print(3)


print(1, end=' ')
print(2, end=' ')
print(3)

