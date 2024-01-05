# # 21.5 연습문제: 오각별 그리기
# import turtle as t

# n = 5
# t.shape('turtle')
# t.color('#fac13c')
# for i in range(n):
#     t.forward(100)
#     t.right( (360 / n) * 2)
#     t.forward(100)
#     t.left(360 / n)


# 21.6 심사문제: 별 그리기
import turtle as t

n, line = map(int, input().split())

t.shape('turtle')
t.color('#fac13c')
for i in range(n):
    t.forward(line)
    t.right( (360 / n) * 2)
    t.forward(line)
    t.left(360 / n)




t.exitonclick()