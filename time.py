import turtle
import datetime
import time
def turtlelest():
    global h,m,s,t
    h=turtle.Turtle()
    m=turtle.Turtle()
    s=turtle.Turtle()
    h.hideturtle()
    h.speed(0)
    m.hideturtle()
    m.speed(0)
    s.hideturtle()
    s.speed(0)
    t=turtle.Turtle()
    t.speed(0)
def clock(radius):
    number=[3,2,1,12,11,10,9,8,7,6,5,4]
    t.hideturtle()
    t.dot()
    t.penup()
    t.setheading(270)
    t.fd(radius)
    t.setheading(0)
    t.pendown()
    t.setheading(0)
    t.circle(radius)
    for i in range(12):
        t.penup()
        t.home()
        t.setheading(0+i*30) #每个指针与第一个写出的标记差i(差几个)*30(360/12)
        t.forward(radius-10)
        t.pendown()
        t.write(number[i])
        t.forward(10)
def showtime(hour,minute,second,r):
    hms=[h,m,s]
    ha=hour*360/12+minute*360/12/60+second*360/12/60/60  #计算每个指针的角度
    ma=minute*360/60+second*360/60/60
    sa=second*360/60
    hmsa=[ha,ma,sa]
    for i in range(3):
        hms[i].pensize(5-2*i)
        hms[i].setheading(90)
        hms[i].setheading(90-hmsa[i]) #由于setheading是从右面开始的,所以+90已从钟表的顶端开始运行
        hms[i].forward(90-(3-i)*20)
def timeshow(r):
    turtlelest()
    clock(r)
    while True:
        now = datetime.datetime.now()
        print("Current date and time: ",now.hour,now.minute,now.second)
        showtime(now.hour,now.minute,now.second,100)
        turtle.tracer(1)#开始动画，把之前的瞬间显示出来
        turtle.tracer(0)#停止动画
        h.clear()
        m.clear()
        s.clear()
        h.home()
        s.home()
        m.home()
timeshow(100)
