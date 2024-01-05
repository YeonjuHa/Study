# 문자열 판단하기
import re
re.match('Hello', 'Hello, world!')
re.match('Python', 'Hello, world!')
re.match('Python', 'Python, Hello!')
re.match('Python', 'Hello, Python')

# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
re.search('^Hello', 'Hello, world!')
re.search('world$', 'Hello, world!')
re.search('world!$', 'Hello, world!')
re.search('Python', 'Hello, Python')
re.search('world', 'Hello, world!')

# 지정된 문자열이 하나라도 포함되는지 판단하기
re.match('hello|world', 'hello')
re.match('Hello|world', 'hello')


# 범위 판단하기
re.match('[0-9]*', '1234')
re.match('[0-9]+', '1234')
re.match('[0-9]+', 'abcd')

re.match('[0-9]+', 'abcd1')
re.match('[0-9]+', '1abcd')


re.match('a*b', 'b')
re.match('a+b', 'b')
re.match('a*b', 'aab')
re.match('a+b', 'aab')

re.match('a*b', 'baa')
re.match('a+b', 'baa')


# 문자가 한 개만 있는지 판단하기
re.match('abc?d', 'abd')
re.match('ab[0-9]?c', 'ab3c')
re.match('ab.d', 'abxd')

re.match('ab.d', 'abx1d')
re.match('ab..d', 'abx1d')


# 문자 개수 판단하기
re.match('h{3}', 'hhhello')
re.match('(hello){3}', 'hellohellohelloworld')

re.match('h{3}', 'hhello')
re.match('(hello){3}', 'hello hello hello world')


# 특정 범위의 문자숫자
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100')

re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010.1000.1000')
re.match('[0-9]{3}.[0-9]{4}.[0-9]{4}', '010.1000.1000')

re.match('[0-9]{3}.[0-9]{4}.[0-9]{4}', '010/1000/1000')


re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000')


# 숫자와 영문 문자를 조합해서 판단하기
re.match('[a-zA-Z0-9]+', 'Hello1234')
re.match('[A-Z0-9]+', 'hello')

# 한글
re.match('[가-힣]+', '홍길동')
re.match('[가-힣]+', '아헿헿')


# 특정 문자 범위에 포함되지 않는지 판단하기
re.match('[^A-Z]+', 'Hello')
re.match('[^A-Z]+', 'hello')

re.search('^[A-Z]+', 'Hello')

re.search('[0-9]+$', 'Hello1234')


# 특수 문자 판단하기
re.search('\*+', '1 ** 2')
re.match('[$()a-zA-Z0-9]+', '$(document)')


re.match('\d+', '1234')
re.match('\D+', 'Hello')
re.match('\w+', 'Hello_1234')
re.match('\W+', '(:)')


# 공백 처리하기
re.match('[a-zA-Z0-9 ]+', 'Hello 1234')
re.match('[a-zA-Z0-9\s]+', 'Hello 1234')


# 같은 정규표현식 패턴을 자주 사용할 때
p = re.compile('[0-9]+')
p.match('1234')
p.search('hello')


# 그룹 사용하기
m = re.match('([0-9]+) ([0-9]+)', '10 295')
m.group(1)
m.group(2)
m.group()
m.group(0)

m.groups()


m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')
m.group('arg')


# 패턴에 매칭되는 모든 문자열 가져오기
re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
re.findall('[a-z]+', '1 2 Fizz 4 Buzz Fizz 7 8')
re.findall('[A-Z]+', '1 2 Fizz 4 Buzz Fizz 7 8')
re.findall('[a-zA-Z]+', '1 2 Fizz 4 Buzz Fizz 7 8')
re.findall('[a-zA-Z0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')


# 문자열 바꾸기
re.sub('apple|orange', 'fruit', 'apple box orange tree')

re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')


def multiple10(m):
    n = int(m.group())
    return str(n * 10)

re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')

# 람다 표현식
re.sub('[0-9]+', lambda m : str(int(m.group()) * 10), '1 2 Fizz 4 Buzz Fizz 7 8')
