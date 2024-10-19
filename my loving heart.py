import turtle
import random

# 设置屏幕
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Moving Hearts")
screen.setup(width=800, height=600)
screen.tracer(0, 0)  # 关闭动画效果

# 创建爱心形状
def draw_heart(t, size):
    t.penup()
    t.goto(t.xcor(), t.ycor() - size / 2)
    t.pendown()
    t.setheading(0)  # 重置方向
    t.begin_fill()
    t.left(140)
    t.forward(size)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.01)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.01)
    t.forward(size)
    t.end_fill()
    t.penup()
    t.goto(t.xcor(), t.ycor() + size / 2)
    t.pendown()

# 创建多个爱心
hearts = []
for _ in range(10):
    heart = turtle.Turtle()
    heart.hideturtle()  # 隐藏海龟图标
    heart.color("red")
    heart.penup()
    heart.speed(0)  # 设置速度为最快
    heart.goto(random.randint(-390, 390), random.randint(-290, 290))
    heart.direction = random.choice(["left", "right", "up", "down"])
    hearts.append(heart)

# 移动爱心
def move_hearts():
    for heart in hearts:
        x, y = heart.position()
        if heart.direction == "left":
            heart.setx(x - 10)
        elif heart.direction == "right":
            heart.setx(x + 10)
        elif heart.direction == "up":
            heart.sety(y + 10)
        elif heart.direction == "down":
            heart.sety(y - 10)

        # 碰撞检测
        if heart.xcor() < -390 or heart.xcor() > 390:
            heart.direction = "left" if heart.direction == "right" else "right"
        if heart.ycor() < -290 or heart.ycor() > 290:
            heart.direction = "up" if heart.direction == "down" else "down"

        for other_heart in hearts:
            if heart != other_heart and heart.distance(other_heart) < 20:
                heart.direction = random.choice(["left", "right", "up", "down"])

        heart.clear()
        heart.penup()
        draw_heart(heart, 20)

    screen.update()
    screen.ontimer(move_hearts, 1)

# 开始移动
move_hearts()

# 保持窗口打开
turtle.done()
