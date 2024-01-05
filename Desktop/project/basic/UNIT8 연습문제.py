# 8.4 연습문제: 합격 여부 출력하기
korean = 92
english = 47
mathematics = 86
science = 81

print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)


# 8.5 심사문제: 합격 여부 출력하기
국, 영, 수, 과 = map(int, input().split())
print(국 >= 90 and 영 > 80 and 수 > 85 and 과 >= 80)

