a = [0, 0, 0, 0, 0]
b = a
print( a is b )     # 객체 a와 객체 b가 같은지 비교

b[2] = 99    # 객체 b의 2번 인덱스 값을 99로 재할당
print( a )
print( b )