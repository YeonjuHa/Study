# 문자열 바꾸기
s1 = 'Hello, world!'
s1
s2 = s1.replace('world', 'Python')
s2

# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)

# 문자열 분리하기
'apple pear grape pineapple orange'.split()
'apple pear grape pineapple orange'.split(',')

# 구분자 문자열과 문자열 리스트 연결하기
fruit = ['apple', 'pear', 'grape', 'pineapple', 'orange']
' '.join(fruit)
'-'.join(fruit)
'@'.join(fruit)

# 휴대폰 번호
phone = '010-1234-5678'
# 번호 분리
phone2 = phone.split('-')
phone2
# 분리된 휴대폰 번호를 하나로 합치기
phone3 = '-'.join(phone2)
phone3

# 휴대폰 번호
phone = '010-1234-5678'
# 번호 분리
phone2 = phone.split('-')
phone2
# 연결
phone3 = phone2[0] + phone2[1] + phone2[2]
phone3

# 소문자를 대문자로 바꾸기
'python'.upper()
'Python'.upper()
# 대문자를 소문자로 바꾸기
'PYTHON'.lower()
'Python'.lower()

# 왼쪽 공백 삭제하기
'   Python    '.lstrip()
# 오른쪽 공백 삭제하기
'   Python    '.rstrip()
# 양쪽 공백 삭제하기
'   Python    '.strip()

# 왼쪽의 특정 문자 삭제하기
', python.'.lstrip(' ,.')
# 오른쪽의 특정 문자 삭제하기
', python.'.rstrip(' ,.')
# 양쪽의 특정 문자 삭제하기
', python.'.strip(' ,.')

# 구두점을 간단하게 삭제하기
import string

', python.'.strip(string.punctuation)
string.punctuation
# 공백 삭제 추가
', python.'.strip(string.punctuation + ' ')
', python.'.strip(string.punctuation).strip()

# 문자열을 왼쪽 정렬하기
'python'.ljust(10)
# 문자열을 오른쪽 정렬하기
'python'.rjust(10)
# 문자열을 가운데 정렬하기
'python'.center(10)

# 메서드 체이닝
'python'.rjust(10).upper()

# 문자열 왼쪽에 0 채우기
'35'.zfill(4)
'3.5'.zfill(6)
'hello'.zfill(10)

# 왼쪽에서부터 문자열 위치 찾기
'apple pineapple'.find('pl')
'apple pineapple'.find('xy')
# 오른쪽에서부터 문자열 위치 찾기
'apple pineapple'.rfind('pl')
'apple pineapple'.rfind('xy')

# 왼쪽에서부터 문자열 위치 찾기
'apple pineapple'.index('pl')
'apple pineapple'.index('xy')
# 오른쪽에서부터 문자열 위치 찾기
'apple pineapple'.rindex('pl')
'apple pineapple'.rindex('xy')

# 문자열 개수 세기
'apple pineapple'.count('pl')



# 문자열 서식 지정자와 포매팅 사용하기
# 서식 지정자로 문자열 넣기
'I am %s.' % 'james'

name = 'maria'
'I am %s.' % name

# 서식 지정자로 문자열 넣기
'I am %d years old.' % 20
'I am %s years old.' % 20
'I am %s years old.' % '20'

# 서식 지정자로 소수점 표현하기
'%f' % 2.3

'%.2f' % 2.3
'%.3f' % 2.3


# 서식 지정자로 문자열 정렬하기 - 오른쪽
'%10s' % 'python'
# 서식 지정자로 문자열 정렬하기 - 왼쪽
'%-10s' % 'python'

# 자릿수가 다른 숫자 출력하기
'%10d' % 150
'%10d' % 15000

'%10.2f' % 2.3
'%10.2f' % 2000.3

# 서식 지정자로 문자열 안에 값 여러 개 넣기
'Today is %d %s.' % (10, 'October')
'Today is %d%s.' % (10, 'October')
'Today is %s %s.' % (10, 'October')


# format 메서드 사용하기
'Hello, {0}'.format('world!')
'Hello, {0}'.format(100)

# format 매서드로 값을 여러 개 넣기
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.11)

# format 메서드로 같은 값을 여러 개 넣기
'{0} {0} {1} {1}'.format('Python', "Script")

# format 메서드에서 인덱스 생략하기
'Hello, {} {} {}'.format('Python', 'Script', 3.11)

# format 메서드에서 인덱스 대신 이름 지정하기
'Hello, {language} {version}'.format(language = 'Python', version = 3.11)

# 문자열 포매팅에 변수를 그대로 사용하기(f-문자열 포매팅)
language = 'Python'
version = 3.11
f'Hello, {language} {version}'

# 중괄호 출력하기
'{{ {0} }}'.format('Python')

# format 메서드로 문자열 정렬하기
'{0:<10}'.format('python')
'{0:>10}'.format('python')
'{:>10}'.format('python')

# 숫자 개수 맞추기
'%03d' % 1
'{0:03d}'.format(35)

'%08.2f' % 3.6
'{0:08.2f}'.format(150.37)

# 채우기와 정렬을 조합해서 사용하기
'{0:0<10}'.format(15)
'{0:0>10}'.format(15)

'{0:0>10.2f}'.format(15)
'{0: >10}'.format(15)
'{0:>10}'.format(15)
'{0:x>10}'.format(15)

# 금액에서 천단위로 콤마 넣기
# format 내장 함수
format(1493500, ',')
# 서식 지정자와 함께 사용
'%20s' % format(1493500, ',')
# 포매팅
'{0:,}'.format(1493500)
# 정렬
'{0:>20,}'.format(1493500)
'{0:0>20,}'.format(1493500)