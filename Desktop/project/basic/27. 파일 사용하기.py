# #파일에 문자열 쓰기
# file = open('hello.txt', 'w')
# file.write('Hello, world!')
# file.close()

# # 파일에서 문자열 읽기
# file = open('hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()

# # 자동으로 파일 객체 닫기
# with open('hello.txt', 'r') as file:
#     s = file.read()
#     print(s)


# # 반복문으로 문자열 여러 줄을 파일에 쓰기
# with open('hello.txt', 'w') as file:
#     for i in range(3):
#         file.write('Hello, world! {0}\n'.format(i))


# # 리스트에 들어있는 문자열을 파일에 쓰기
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'w') as file:
#     file.writelines(lines)

# # 파일의 내용을 한 줄씩 리스트로 가져오기
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)


# # 파일의 내용을 한 줄씩 읽기
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'r') as file:
#     line = None
#     while line != '':
#         line = file.readline()
#         print(line.strip('\n'))

# # for 반복문으로 파일의 내용을 줄 단위로 읽기
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'r') as file:
#     for line in file:

#         print(line.strip('\n'))

    

# # 파일 객체는 이터레이터
# file = open('hello.txt', 'r')
# a, b, c = file
# a, b, c


# # 파이썬 객체를 파일에 저장하기, 가져오기
# # 파이썬 객체를 파일에 저장하기
# import pickle

# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

# with open('james.p', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)

# # 파일에서 파이썬 객체 읽기
# import pickle

# with open('james.p', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)


# 파일 끝에 추가
with open('hello.txt', 'a') as f:
    f.write('hello \n') 