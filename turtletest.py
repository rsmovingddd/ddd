import turtle
import time

def drawSnake(rad, angle, len, neckrad):
    b = 1

if __name__ == "__main__":
    turtle.setup(500,500,0,0)
    t = turtle.Turtle()
    t.speed(10)
    #t.pensize(10)  # 画笔尺寸
    t.color("red")
    t.pencolor("black")
    t.resizemode("user")
    t.shape("square")
    t.shapesize(1, 1, 1)
    t.ht()
    t.seth(270)    # 前进的方向
    
    #drawSnake(70, 80, 2, 15)
    t.stamp()
    t.penup()
    a = t.xcor()
    b = t.ycor()
    print(a," ",b)
    for i in range(11):
        t.stamp()
        t.fd(20)  # 直线前进
        t.stamp()
        t.left(0)
#       t.right(90)
        time.sleep(0.5)
        a = t.xcor()
        b = t.ycor()
        print("%.3f %.3f"%(a,b))
    #t.left(90)
    '''
    for i in range(5):
        t.fd(20)  # 直线前进
        t.stamp()
        time.sleep(0.1)
    '''

    a = input()
