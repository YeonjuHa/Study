import turtle as t

# # 사각형
# t.shape('turtle')

# for i in range(4):      # 사각형이므로 4번 반복
#     t.forward(100)
#     t.right(90)


# # 오각형
# t.shape('turtle')

# for i in range(5):
#     t.forward(100)
#     t.right( 360 / 5 )


# # 다각형 그리기
# n = int(input('n각형: '))
# t.shape('turtle')

# for i in range(n):
#     t.forward(100)
#     t.right( 360 / n )


# # 다각형에 색 칠하기
# import turtle as t

# n = 6
# t.shape('turtle')
# t.color('#40dbc1')      # color picker 
# t.begin_fill()
# for i in range(n):
#     t.forward(100)
#     t.right(360 / n)
# t.end_fill()


# # 복잡한 도형 그리기
# import turtle as t
# t.shape('turtle')

# t.circle(120)


# # 원을 반복해서 그리기
# import turtle as t

# n = 60
# t.shape('turtle')
# t.color('#40dbc1')
# t.speed('fastest')
# for i in range(n):
#     t.circle(120)
#     t.right( 360 / n )


# 선으로 복잡한 무늬 그리기
import turtle as t

t.shape('turtle')
t.speed('fastest')
t.color('#40dbc1')
for i in range(300):
    t.forward(i)
    t.right(91)


t.exitonclick()