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
            if (snake.eatwait > 0):                    # 计数器：尾巴离食物还有多少格
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
        self.eating += num
    
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
    
    def result(self,ddd):
        self.head.pen.color("orange")       # head 橙色
        if (ddd):
            self.head.pen.write("Win", False,font=("Arial", 24, "bold"))
        else:
            self.head.pen.write("Lose", False,font=("Arial", 24, "bold"))


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
 
pausing = True                 # 是否暂停             
gameready = False              # 初始化是否完成

def pauseChange():             # 空格切换暂停/继续
    global pausing
    pausing = not pausing
    return 0

def gameBegin(x,y):            # onclick 绑定的函数
    global pausing
    global turtle
    global gameready
    if (gameready):
        pausing = False
        turtle.onclick(None)  

if __name__ == "__main__":
    
    turtle.setup(500, 500, 0, 0)
    turtle.title("                                        Snake by Kinley Lam")
    
    # 这里的设置是为了实现点击屏幕开始游戏
    turtle.penup()               # 笔拿起（依赖 stamp）
    #screenDetect.setpos(0,0)    # 设置初始位置
    turtle.resizemode("user")    # 用户自定义，为了设置形状
    turtle.shape("square")       # 设置形状
    turtle.shapesize(25, 25, 1)  # 大小 20*20，有 1 像素的边界
    turtle.color("white")        # 海龟颜色
    turtle.onclick(gameBegin)    # 绑定鼠标
    
    words = turtle.Turtle()      # 一堆说明
    words.hideturtle()           # 海龟隐藏
    words.penup()                # 笔拿起（依赖 stamp）
    words.setpos(-220,100)       # 设置初始位置
    words.resizemode("user")     # 用户自定义，为了设置形状
    words.shape("square")        # 设置形状
    words.shapesize(1, 1, 1)     # 大小 20*20，有 1 像素的边界
    words.color("black")         # 字体颜色
    words.write("Welcome to Kinley's version of snake...\nYou are going to use the 4 arrow keys to move the snake\naround the screen, trying to consume all the food items \nbefore the monster catches you...\n\nClick anywhere on the screen to start the game,have fun!!",False,'left',font=('Arial',12,'bold'))#字体大小调下(font=(字体名称，大小，类型））


    fakeHead = turtle.Turtle()    # 假的头（因为 snake 在一个 class 里面集中实现了，这里为了方便）
    fakeHead.hideturtle()         # 海龟隐藏
    fakeHead.penup()              # 笔拿起（依赖 stamp）
    fakeHead.setpos(0,0)          # 设置初始位置
    fakeHead.resizemode("user")   # 用户自定义，为了设置形状
    fakeHead.shape("square")      # 设置形状
    fakeHead.shapesize(1, 1, 1)   # 大小 20*20，有 1 像素的边界
    fakeHead.color("red")         # 海龟颜色
    fakeStamp = fakeHead.stamp()  # 盖章         
    fakeHead.left(0)              # 防 bug
    
    tempsnake = SnakeClass(-400.0,0.0)    # 边界外再搞条蛇，为了绕过 bug 实现暂停
    monster = MonsterClass(-150,-150,0)   # 怪
    eating = False                        # 是否在 eat
    caught = False                        # 是否被怪追上
    

    # 双 timer 异步进行对于 python 单线程来说是极端现实的，唯一可行的实现方式是，使用同一个 timer，
    # timer 给得细一些，然后让各个 object 在不同的时间动作
    
    snakeTime = 0                         # 用于 snake 的计数器
    snakeLevel = 80                       # 计数器的 bound
    monsterTime = 0                       # 用于 monster 的计数器
    monsterLevel = 20                     # 用于 monster 的 bound

    gameready = True  # 前面的基础准备完成

    while (True):           # 等待单击后游戏开始，这么写是为了绕过 bug 实现暂停功能
        if (pausing):
            tempsnake.up()  # 边界外的蛇疯狂游走
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
            break
    turtle.title("                                                 Snake")  # 窗口标题
    fakeHead.clearstamp(fakeStamp)  # 把假的头拿掉
    words.clear()                   # 删掉开场说明

    snake = SnakeClass(0.0,0.0)          # 蛇 class
    turtle.onkey(pauseChange, "space")
    turtle.onkey(snake.setUp, "Up")        # 按键响应
    turtle.onkey(snake.setDown, "Down")
    turtle.onkey(snake.setLeft, "Left")
    turtle.onkey(snake.setRight, "Right")
    turtle.onkeypress(snake.setUp, "Up")
    turtle.onkeypress(snake.setDown, "Down")
    turtle.onkeypress(snake.setLeft, "Left")
    turtle.onkeypress(snake.setRight, "Right")
    turtle.listen()
    
    foods = list()           # 存放所有 food turtle 的 list
    food1 = turtle.Turtle()  # 建立所有的 food turtle
    food1.hideturtle()
    food2 = turtle.Turtle()
    food2.hideturtle()
    food3 = turtle.Turtle()
    food3.hideturtle()
    food4 = turtle.Turtle()
    food4.hideturtle()
    food5 = turtle.Turtle()
    food5.hideturtle()
    food6 = turtle.Turtle()
    food6.hideturtle()
    food7 = turtle.Turtle()
    food7.hideturtle()
    food8 = turtle.Turtle()
    food8.hideturtle()
    food9 = turtle.Turtle()
    food9.hideturtle()
    foods.append(food1)      # 放入 food list
    foods.append(food2)
    foods.append(food3)
    foods.append(food4)
    foods.append(food5)
    foods.append(food6)
    foods.append(food7)
    foods.append(food8)
    foods.append(food9)
    
    foodx = [100,80,-60,-120,20,40,-80,-180,0]      # food 的 x，y 坐标
    foody = [140,-160,-200,20,160,-120,-140,0,100]
    foodExist = [0,1,2,3,4,5,6,7,8]      # 有哪些食物还被剩下，编号也可用于其他 list 的定位，一举两得
    
    for i in range(9):
        #foods[i].hideturtle()                      # 海龟隐藏
        foods[i].penup()                            # 笔全程拿起（依赖 stamp）
        foods[i].setpos(foodx[i]+2,foody[i]-10)     # 设置 turtle 位置，为了让打印对上食物定下的位置，加了偏移量
        foods[i].speed(10)                          # 移动速度：最快，因为不依赖移动来刷新
        foods[i].resizemode("user")                 # 用户自定义，为了设置形状
        foods[i].shape("square")                    # 设置形状
        foods[i].shapesize(1, 1, 1)                 # 大小 20*20，有 1 像素的边界
        #foods[i].color("white")                    # 海龟颜色
        foods[i].setheading(270)                    # 初始方向
        foods[i].write(i+1, False, align="center",font=("Arial", 12, "normal"))   # 标注食物编号
    
    # 各种时间戳
    timeBegin = time.time()  # 开始时间
    timePaused = 0.0         # 累计暂停时间
    pauseCut1 = 0.0          # 用于暂停时间计算
    pauseCut2 = 0.0
    timeNow = 0.0            # 现在的时间
    while (True):
        if (pausing):        # 绕开 bug 实现暂停
            tempsnake.up()   # 边界外的蛇疯狂游走
            tempsnake.up()
            tempsnake.left()
            tempsnake.left()
            tempsnake.down()
            tempsnake.down()
            tempsnake.left()
            tempsnake.left()
            print("waiting")
            if (pauseCut1 == 0.0):        # 计算暂停时间
                pauseCut1 = timeNow
            else:
                pauseCut1 = pauseCut2
            pauseCut2 = time.time()
            timePaused = pauseCut2 - pauseCut1 # 累加
        else:
            snakeTime += 1                  # 蛇的计数器  
            if (snake.eating == 0):
                snakeLevel = 80             
            else:
                snakeLevel = 120            # 在吃，则加高 bound，拖慢蛇的速度
            if (snakeTime == snakeLevel):   # count 到 snake 该走了
                if (snake.direction == 0):  # 走的方向
                    snake.right()
                elif (snake.direction == 90):
                    snake.up()
                elif (snake.direction == 180):
                    snake.left()
                else:
                    snake.down()
                snakeTime = 0   # 计数器清零
            for i in foodExist: 
                if ((foodx[i] - snake.headx < 1)and(foodx[i] - snake.headx > -1)and(foody[i] - snake.heady < 1)and(foody[i] - snake.heady > -1)):
                    foods[i].clear()          # check 一下有没有食物被吃掉
                    foodExist.remove(i)
                    snake.eat(i+1)
            monsterTime += 1                              # 怪的计数器
            if (monsterTime == monsterLevel):             # 怪该走了
                monster.move(snake.headx,snake.heady)
                monsterTime = 0                           # 怪的计数器清零
            if (monster.touch(snake.headx,snake.heady)):
                caught = True                             # 检测有没有捉到 head
                break                                     # 游戏结束，输了
            if (len(foodExist) == 0): break  # 食物被吃光了，赢了
            time.sleep(0.001)                # loop delay
            timeNow = time.time()            
            pauseCut1 = 0.0                  # 为了让 pause 时间统计辨认是否需要累加
            turtle.title("                              Snake:   Contacted: %d   Time: %d"%((9-len(foodExist)),timeNow - timeBegin - timePaused))
    
    if (caught):            # 判断输赢
        snake.result(False)
    else:
        snake.result(True)

    #time.sleep(10)
    turtle.exitonclick()    # 单击鼠标退出