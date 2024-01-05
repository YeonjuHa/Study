# 37.2 연습 문제: 사각형의 넓이 구하기
# 다음 소스 코드를 완성하여 사각형의 넓이가 출려되게 만드세요.
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)


# 37.3 심사문제: 두 점 사이의 거리 구하기
# 표준 입력으로 x, y 좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다.
# 여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다.
# 다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만드세요.
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map( int, input().split() )

for i in range(len(p) - 1):
    a = p[i+1].x - p[i].x
    b = p[i+1].y - p[i].y
    length += math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(length)