# 동물 이름을 입력 받아 텍스트 파일로 저장하시오.
# 파일 이름은 animals.txt
# 숫자 0000을 입력하면 중단

while True:
    name = input('동물 이름 입력: ')
    if name != '0000':
        with open('animals.txt', 'a') as file:
            file.write(name + '\n')
    else:
        break