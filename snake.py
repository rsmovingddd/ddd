import turtle
import time
import random
import math

class PenClass:

    def __init__(self,x,y,head):
        self.pen = turtle.Turtle()   # 初始化
        self.pen.hideturtle()        # 海龟隐藏
        self.pen.penup()             # 笔全程拿起（依赖 stamp）
        self.pen.setpos(x,y)         # 设置初始位置
        self.pen.speed(10)           # 移动速度：最快，因为不依赖移动来刷新
        self.pen.resizemode("user")  # 用户自定义，为了设置形状
        self.pen.shape("square")     # 设置形状
        self.pen.shapesize(1, 1, 1)  # 大小 20*20，有 1 像素的边界
        self.pen.setheading(head)    # 初始方向
        self.dir = head              # 记录方向的参数
    
    def up(self):
        self.pen.right(self.dir - 90)  # 转向，根据方向记录
        self.dir = 90
        self.pen.forward(20)       # 前进一格宽度
        astamp = self.pen.stamp()  # stamp 打印
        self.pen.left(0)           # 规避 stamp 的 bug
        return astamp              # 传回刚才印出的 stamp

    def down(self):
        self.pen.right(self.dir - 270)  # 转向，根据方向记录
        self.dir = 270
        self.pen.forward(20)
        astamp = self.pen.stamp()
        self.pen.left(0)
        return astamp
    
    def left(self):
        self.pen.right(self.dir - 180)  # 转向，根据方向记录
        self.dir = 180
        self.pen.forward(20)
        astamp = self.pen.stamp()
        self.pen.left(0)
        return astamp
    
    def right(self):
        self.pen.right(self.dir - 0)  # 转向，根据方向记录
        self.dir = 0
        self.pen.forward(20)
        astamp = self.pen.stamp()
        self.pen.left(0)
        return astamp
    
    def deleteStamp(self,getstamp):
        self.pen.clearstamp(getstamp)
   

class SnakeClass:
    
    def __init__(self,x,y):
        self.head = PenClass(x-20,y,0)    # head，初始位置会向右一格
        self.body = PenClass(x-100,y,0)   # body，紧跟着 head 的那一格，初始位置会向右一格
        self.head.pen.color("red")       # head 全红色
        self.body.pen.color("black")     # body 黑色
        self.body.pen.pencolor("blue")   # body 蓝色边框
        self.vec = list()                # 存储 body stamp 的 list
        self.headx = x                  # 存储 head 的坐标
        self.heady = y
        self.gesture = 0                 # 存储 head 的上一个动作,初始为右
        self.direction = 0               # 存储头部的方向
        self.eating = 0                  # 记录是否在 eat，也作为计数器
        self.eatwait = 0                 # eat 前的计数器

        for i in range(4):
            astamp = self.body.right()          # 右移同时盖章
            self.vec.append(astamp)
        self.headstamp = self.head.right()      # 存储头部的 stamp，注意盖章用右移实现
        self.tempstamp1 = self.headstamp        # 一个用于存储 stamp 的 temp 变量
        self.tempstamp2 = self.headstamp        # 一个用于存储 stamp 的 temp 变量
        self.head.pen.left(0)
    
    def moveBody(self):                          # 移动 body
        if (self.gesture == 0):                  # 加上新的 stamp        
            self.tempstamp2 = self.body.right()  # 方向为右
        elif (self.gesture == 90):
            self.tempstamp2 = self.body.up()     # 方向为上
        elif (self.gesture == 180):
            self.tempstamp2 = self.body.left()   # 方向为左
        else:
            self.tempstamp2 = self.body.down()   # 方向为下
        self.vec.append(self.tempstamp2)         # 将新的 stamp 加入list
        if (self.eating > 0):                    # 已经碰到了食物
            if (eatwait > 0):                    # 计数器：尾巴离食物还有多少格
                self.body.deleteStamp(self.vec.pop(0)) # 擦除尾部的 stamp
                self.eatwait -= 1                
            else:
                self.eating -=1                  # eat 的计数器。由于没有删除 stamp，蛇的长度增加了
        else:
            self.body.deleteStamp(self.vec.pop(0))   # 将最旧的 stamp 移除
    
    def up(self):                                    # 移动 整个 snake
        if (self.heady < 221):                       # head 撞墙检测，撞墙则整体不移动
            self.tempstamp1 = self.head.up()         # 移动 head
            self.heady += 20                         # 更新 head 坐标
            self.moveBody()                          # 移动 body
            self.gesture = 90                         # 记录 head 的行为（给接下来 body 用）
            self.head.deleteStamp(self.headstamp)    # 删除旧的 head stamp
            self.headstamp = self.tempstamp1         # 更新 head stamp
    
    def down(self):
        if (self.heady > -221): 
            self.tempstamp1 = self.head.down()
            self.heady -= 20
            self.moveBody()
            self.gesture = 270
            self.head.deleteStamp(self.headstamp)
            self.headstamp = self.tempstamp1
    
    def left(self):
        if (self.headx > -221): 
            self.tempstamp1 = self.head.left()
            self.headx -= 20
            self.moveBody()
            self.gesture = 180
            self.head.deleteStamp(self.headstamp)
            self.headstamp = self.tempstamp1
    
    def right(self):
        if (self.headx < 221): 
            self.tempstamp1 = self.head.right()
            self.headx += 20
            self.moveBody()
            self.gesture = 0
            self.head.deleteStamp(self.headstamp)
            self.headstamp = self.tempstamp1
    
    def eat(self,num):
        if (self.eatwait == 0):
            self.eatwait = len(self.vec)
        eating += num
    
    def setRight(self):
        if (self.direction != 180):
            self.direction = 0
    
    def setLeft(self):
        if (self.direction != 0):   
            self.direction = 180
    
    def setUp(self):
        if (self.direction != 270):    
            self.direction = 90
    
    def setDown(self):
        if (self.direction != 90):    
            self.direction = 270

class MonsterClass(PenClass):

    def __init__(self, x, y, head):
        super().__init__(x, y, head)
        self.pen.color("purple")             # 颜色紫色
        self.x = x                           # 存储坐标
        self.y = y                           
        self.stampStore = self.pen.stamp()   # 存储 stamp
        self.pen.left(0)
        self.stampTemp = self.stampStore     # stamp temp
        self.rate = 0.0                        # 存储得到的 random 变量
        self.temp1 = 0.0                       # int temp
        self.speed = 20                    # 控制速度的参数
    
    def setSpeed(self,n):
        self.speed = n

    def move(self,headx,heady):
        self.rate = random.random() + 1           # random 值，0.5 到 1.5
        self.temp1 = (self.x - headx)*(self.x - headx) + (self.y - heady)*(self.y - heady)
        self.temp1 = math.sqrt(self.temp1)
        self.temp1 = self.speed/(self.temp1*10)  # 计算比值，用于斜线移动
        if (self.x != headx):
            self.x += (headx - self.x)*self.temp1*self.rate # 新坐标
        if (self.y != heady):
            self.y += (heady - self.y)*self.temp1*self.rate
        self.pen.setpos(self.x,self.y)                      # 移动到新位置
        self.stampTemp = self.pen.stamp()                   # 新 stamp
        self.pen.left(0)
        self.pen.clearstamp(self.stampStore)                # 擦除旧的 stamp
        self.stampStore = self.stampTemp
    
    def touch(self,headx,heady):
        return ((self.x - headx < 20.0)and(self.x - headx > -20.0)and(self.y - heady < 20.0)and(self.y - heady > -20))


 
pausing = False                 # 是否暂停
pauseDetect = 0


def pauseChange():
    global pausing
    temppausing = not pausing
    pausing = temppausing
    return 0

if __name__ == "__main__":
    turtle.setup(500, 500, 0, 0)
    snake = SnakeClass(0.0,0.0)                 # 蛇
    tempsnake = SnakeClass(-400.0,0.0) 
    monster = MonsterClass(-150,-150,0)  # 怪
    gaming = True                        # 游戏是否在进行
    eating = False                       # 是否在 eat
    caught = False                       # 是否被怪追上
    snakeTime = 0                        # 用于 snake 的计数器
    snakeLevel = 80                      # 计数器的 bound
    monsterTime = 0
    monsterLevel = 30
    
    turtle.onkey(pauseChange, "space")
    #turtle.onkeypress(pauseChange, "space")
    turtle.onkey(snake.setUp, "Up")        # 按键响应
    turtle.onkey(snake.setDown, "Down")
    turtle.onkey(snake.setLeft, "Left")
    turtle.onkey(snake.setRight, "Right")
    turtle.onkeypress(snake.setUp, "Up")
    turtle.onkeypress(snake.setDown, "Down")
    turtle.onkeypress(snake.setLeft, "Left")
    turtle.onkeypress(snake.setRight, "Right")
    turtle.listen()
    
    i = 0
    while (True):
        if (pausing):
            tempsnake.up()
            tempsnake.up()
            tempsnake.left()
            tempsnake.left()
            tempsnake.down()
            tempsnake.down()
            tempsnake.left()
            tempsnake.left()
            print("waiting")
            #turtle.listen()
        else:
            snakeTime += 1                
            if (snakeTime == snakeLevel):
                if (snake.direction == 0):
                    snake.right()
                elif (snake.direction == 90):
                    snake.up()
                elif (snake.direction == 180):
                    snake.left()
                else:
                    snake.down()
                snakeTime = 0
            monsterTime += 1
            if (monsterTime == monsterLevel):
                monster.move(snake.headx,snake.heady)
                monsterTime = 0
            if (monster.touch(snake.headx,snake.heady)):
                caught = True
                break
            i += 1
            if (i == 10000):break
            time.sleep(0.002)
    
    if (caught):
        print("Lose")
    a = input()