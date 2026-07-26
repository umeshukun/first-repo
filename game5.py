import turtle
import colorsys

# 画面の準備
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Art")

t = turtle.Turtle()
t.speed(0) # 最速で描画
turtle.tracer(2) # 描画スピードをさらに加速

# 色鮮やかな幾何学模様を描く
n = 36
for i in range(360):
    color = colorsys.hsv_to_rgb(i / 360, 1.0, 1.0)
    t.pencolor(color)
    t.width(i / 100 + 1)
    t.forward(i * 3 / n + i)
    t.left(59)

turtle.done()