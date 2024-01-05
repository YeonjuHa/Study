# 39.6 연습문제: 배수 이터레이터 만들기
# 다음 소스 코드에서 특정 수의 배수를 만드는 이터레이터를 작성하세요.
# 배수는 0부터 지정된 숫자보다 작을 때까지 만들어야 합니다.

class MultipleIterator:
    def __init__(self, stop, multiple):
        self.current = 0
        self.stop = stop
        self.multiple = multiple
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop:
            return self.current * self.multiple
        else:
            raise StopIteration
    
for i in MultipleIterator(20, 3):
    print(i, end=' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')