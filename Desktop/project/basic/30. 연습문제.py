# 30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
# 다음 소스 코드를 완성하여 가장 높은 점수가 출력되게 만드세요.

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_socre(*args):
    return max(args)

max_socre = get_max_socre(korean, english, mathematics, science)
print('높은 점수:', max_socre)

max_socre = get_max_socre(english, science)
print('높은 점수:', max_socre)


# 30.7 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요.
# 평균 점수는 실수로 출력되어야 합니다.

korean, english, mathematics, science = map(int, input().split())

def get_min_max_socre(*args):
    min_sco = min(args)
    max_sco = max(args)
    return min_sco, max_sco

def get_average(*args):
    return sum(args) / len(args)

min_socre, max_socre = get_min_max_socre(korean, english, mathematics, science)
average_socre = get_average(korean, english, mathematics, science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_socre, max_socre, average_socre))

min_socre, max_socre = get_min_max_socre(english, science)
average_socre = get_average(english, science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_socre, max_socre, average_socre))