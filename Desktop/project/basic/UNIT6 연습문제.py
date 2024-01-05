# 6.6 연습문제: 정수 세 개를 입력받고 합계 출력하기
a, b, c = map( int, input().split() )
print(a + b + c)



# 6.7 심사문제: 변수 만들기
a, b, c = 50, 100, None
print(a)
print(b)
print(c)


# 6.8 심사문제: 평균 점수 구하기
국, 영, 수, 과 = map(int, input().split())
print( (국 + 영 + 수 + 과) // 4 )
