# 32.4 연습문제: 이미지 파일만 가져오기
# 다음 소스 코드를 완성하여 확장자가 .jpg, .png인 이미지 파일만 출력되게 만드세요.
# 여기서는 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다.
# 람다 표현식에서 확장자를 검사할 때는 문자열 메서드를 활용하세요.

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
a = list( filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files) )
print(a)



# 32.5 심사문제: 파일 이름을 한꺼번에 바꾸기
# 표준 입력으로 숫자.확장자 형식으로 된 파일 이름 여러 개가 입력됩니다.
# 다음 소스 코드를 완성하여 파일 이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로 출력되게 만드세요.
# 예를 들어 1.png는 001.png, 99.docx는 099.docx, 100.xlsx는 100.xlsx처럼 출력되어야 합니다.
# 그리고 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태하야 합니다.
# 람다 표현식에서 파일명을 처리할 때는 문자열 포매팅과 문자열 메서드를 활용하세요.

files = input().split()
b = list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1] ,files))
print(b)

# 문자열 포매팅 
c = list(map(lambda x: '{0:03d}'.format(int(x.split('.')[0])) + '.' + x.split('.')[1], files))
print(c)