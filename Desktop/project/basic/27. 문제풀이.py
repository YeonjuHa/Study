# # 27.5 연습문제: 파일에서 10자 이하인 단어 개수 세기
# # 단어가 줄 단위로 저장된 words.txt. 파일이 주어집니다.
# # 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.
with open('27.5 words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)


print()


# 27.6 심사문제: 특정 문자가 들어있는 단어 찾기
# 문자열이 저장된 words.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다).
# word.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.
with open('27.6 words.txt', 'r') as file:
    words = file.readline().split()
    for word in words:
        if 'c' in word:
            print(word.strip(',.'))