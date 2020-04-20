import turtle
import time
import random
import math

def penInit(obj,x,y):
    #obj = turtle.Turtle()   # 初始化
    obj.hideturtle()        # 海龟隐藏
    obj.penup()             # 笔全程拿起（依赖 stamp）
    obj.setpos(x,y)         # 设置初始位置
    obj.speed(10)           # 移动速度：最快，因为不依赖移动来刷新
    obj.resizemode("user")  # 用户自定义，为了设置形状
    obj.shape("square")     # 设置形状
    obj.shapesize(1, 1, 1)  # 大小 20*20，有 1 像素的边界

def penMove(obj,dir):
    obj.right(obj.heading() - dir) # 转向
    obj.forward(20)                # 向前
    astamp = obj.stamp()           # 获取 stamp
    obj.left(0)                    # 规避 bug
    return astamp

direction = 0
vec = list()                # 存储 body stamp 的 list
gesture = 0                 # 存储 head 的上一个动作,初始为右
eating = 0                  # 记录是否在 eat，也作为计数器
eatwait = 0                 # eat 前的计数器
headStamp = 0

def snakeMove(head,body):
    global direction
    global vec
    global gesture
    global eating
    global eatwait
    global headStamp
    directionGet = direction
    if ((directionGet == 90) and (head.ycor() > 221)): return 0
    if ((directionGet == 270) and (head.ycor() < -221)): return 0
    if ((directionGet == 180) and (head.xcor() < -221)): return 0
    if ((directionGet == 0) and (head.xcor() > 221)): return 0
    tempstamp1 = penMove(head,directionGet)
    tempstamp2 = penMove(body,gesture)
    
    vec.append(tempstamp2)         # 将新的 stamp 加入list
    if (eating > 0):                    # 已经碰到了食物
        if (eatwait > 0):                    # 计数器：尾巴离食物还有多少格
            body.clearstamp(vec.pop(0))      # 擦除尾部的 stamp
            eatwait -= 1                
        else:
            eating -=1                  # eat 的计数器。由于没有删除 stamp，蛇的长度增加了
    else:
        body.clearstamp(vec.pop(0))     # 将最旧的 stamp 移除
     
    head.clearstamp(headStamp)     # 删除旧的 head stamp
    headStamp = tempstamp1         # 更新 head stamp
    gesture = directionGet

def setRight():
    global direction
    if (direction != 180):
        direction = 0

def setLeft():
    global direction
    if (direction != 0):   
        direction = 180

def setUp():
    global direction
    if (direction != 270):    
        direction = 90

def setDown():
    global direction
    if (direction != 90):    
        direction = 270

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
    penInit(words,-220,100)
    words.color("black")         # 字体颜色
    words.write("Welcome to Kinley's version of snake...\nYou are going to use the 4 arrow keys to move the snake\naround the screen, trying to consume all the food items \nbefore the monster catches you...\n\nClick anywhere on the screen to start the game,have fun!!",False,'left',font=('Arial',12,'bold'))#字体大小调下(font=(字体名称，大小，类型））

    head = turtle.Turtle()
    penInit(head,-20,0)
    head.setheading(0)
    head.color("red")       # head 全红色
    headStamp = penMove(head,0)
    
    pausePen = turtle.Turtle()
    penInit(pausePen,300,0)

    monster = turtle.Turtle()
    penInit(monster,-150,-150)
    monster.color("purple")             # 颜色紫色
    monsterStampStore = monster.stamp()   # 存储 stamp
    monster.left(0)
    monsterStampTemp = monsterStampStore
    
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
            penMove(pausePen,0)
            #print("waiting")
        else:
            break
    turtle.title("                                                 Snake")  # 窗口标题
    fakeHead = head.stamp()
    fakeMonster = monster.stamp()
    words.clear()                   # 删掉开场说明

    #snake = SnakeClass(0.0,0.0)          # 蛇 class
    
    body = turtle.Turtle()
    penInit(body,-100,0)
    
    body.setheading(0)
    
    body.color("black")     # body 黑色
    body.pencolor("blue")   # body 蓝色边框
    
    for i in range(4):
        astamp = penMove(body,0)          # 右移同时盖章
        vec.append(astamp)

    turtle.onkey(pauseChange, "space")
    turtle.onkey(setUp, "Up")        # 按键响应
    turtle.onkey(setDown, "Down")
    turtle.onkey(setLeft, "Left")
    turtle.onkey(setRight, "Right")
    turtle.onkeypress(setUp, "Up")
    turtle.onkeypress(setDown, "Down")
    turtle.onkeypress(setLeft, "Left")
    turtle.onkeypress(setRight, "Right")
    turtle.listen()
    
    foods = list()           # 存放所有 food turtle 的 list
    food1 = turtle.Turtle()  # 建立所有的 food turtle
    food2 = turtle.Turtle()
    food3 = turtle.Turtle()
    food4 = turtle.Turtle()
    food5 = turtle.Turtle()
    food6 = turtle.Turtle()
    food7 = turtle.Turtle()
    food8 = turtle.Turtle()
    food9 = turtle.Turtle()
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
        penInit(foods[i],foodx[i]+2,foody[i]-10)
        foods[i].write(i+1, False, align="center",font=("Arial", 12, "normal"))   # 标注食物编号
    
    # 各种时间戳
    timeBegin = time.time()  # 开始时间
    timePaused = 0.0         # 累计暂停时间
    pauseCut1 = 0.0          # 用于暂停时间计算
    pauseCut2 = 0.0
    timeNow = 0.0            # 现在的时间
    head.clearstamp(fakeHead)
    monster.clearstamp(fakeMonster)
    while (True):
        if (pausing):        # 绕开 bug 实现暂停
            penMove(pausePen,0)
            #print("waiting")
            if (pauseCut1 == 0.0):        # 计算暂停时间
                pauseCut1 = timeNow
            else:
                pauseCut1 = pauseCut2
            pauseCut2 = time.time()
            timePaused = pauseCut2 - pauseCut1 # 累加
        else:
            snakeTime += 1                  # 蛇的计数器  
            if (eating == 0):
                snakeLevel = 80             
            else:
                snakeLevel = 120            # 在吃，则加高 bound，拖慢蛇的速度
            if (snakeTime == snakeLevel):   # count 到 snake 该走了
                snakeTime = 0
                snakeMove(head,body)
                for i in foodExist: 
                    if ((foodx[i] - head.xcor() < 1)and(foodx[i] - head.xcor() > -1)and(foody[i] - head.ycor() < 1)and(foody[i] - head.ycor() > -1)):
                        foods[i].clear()          # check 一下有没有食物被吃掉
                        foodExist.remove(i)
                        if (eatwait == 0):
                            eatwait = len(vec)
                        eating += i+1
            monsterTime += 1                              # 怪的计数器
            if (monsterTime == monsterLevel):             # 怪该走了
                # monster 的 speed 是 2
                temp1 = 1/math.sqrt((monster.xcor() - head.xcor())*(monster.xcor() - head.xcor()) + (monster.ycor() - head.ycor())*(monster.ycor() - head.ycor()))
                temp2 = random.random() + 1
                if (monster.xcor() != head.xcor()):
                    monster.setx(monster.xcor() + (head.xcor() - monster.xcor())*temp1*temp2) # 新坐标
                if (monster.ycor() != head.ycor()):
                    monster.sety(monster.ycor() + (head.ycor() - monster.ycor())*temp1*temp2)
                monsterStampTemp = monster.stamp()                   # 新 stamp
                monster.left(0)
                monster.clearstamp(monsterStampStore)                # 擦除旧的 stamp
                monsterStampStore = monsterStampTemp
                monsterTime = 0                           # 怪的计数器清零
            if ((monster.xcor() - head.xcor() < 20.0)and(monster.xcor() - head.xcor() > -20.0)and(monster.ycor() - head.ycor() < 20.0)and(monster.ycor() - head.ycor() > -20)):
                caught = True                             # 检测有没有捉到 head
                break                                     # 游戏结束，输了
            if (len(foodExist) == 0): break  # 食物被吃光了，赢了
            time.sleep(0.001)                # loop delay
            timeNow = time.time()            
            pauseCut1 = 0.0                  # 为了让 pause 时间统计辨认是否需要累加
            turtle.title("                              Snake:   Contacted: %d   Time: %d"%((9-len(foodExist)),timeNow - timeBegin - timePaused))
    
    head.color("yellow")       # head 橙色
    if (caught):            # 判断输赢
        head.write("Lose", False,font=("Arial", 24, "bold"))
    else:
        head.write("Win", False,font=("Arial", 24, "bold"))

    turtle.exitonclick()    # 单击鼠标退出