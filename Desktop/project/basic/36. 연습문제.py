# 36.8 연습문제: 리스트에 기능 추가하기
# 다음 소스 코드에서 리스트(list)에 replace 메서드를 추가한 AdvancedList 클래스를 작성하세요.
# AdvancedList는 list를 상속받아서 만들고, replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾸도록 만드세요.

class AdvancedList(list):
    def repalce(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.repalce(1, 100)
print(x)



# 36.9 심사문제: 다중 상속 사용하기
# 다음 소스 코드에서 동물 클래스 Animal과 날개 클래스 Wing을 상속받아 새 클래스 Bird를 작성하여
# '먹다', '파닥거리다', '날다', True, True가 각 줄에 출력되게 만드세요.

class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))