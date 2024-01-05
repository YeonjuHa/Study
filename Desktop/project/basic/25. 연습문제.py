# 25.7 연습문제: 평균 점수 구하기
# 다음 소스 코드를 완성하여 평균 점수가 출력되게 만드세요.
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)


# 25.8 심사문제: 딕셔너리에서 특정 값 삭제하기
# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고 첫 번째 줄은 키,
# 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다.
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))
x = {key: value for key, value in x.items() if key !='delta' and value != 30}
print(x)