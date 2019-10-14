import turtle as trtl

v = trtl.Turtle()

v.speed(0)
v.hideturtle()

#background
v.fillcolor("skyblue")
v.pensize(10)
v.penup()
v.begin_fill()
v.goto(-480,405)
v.pendown()
v.goto(470,405)
v.goto(470,-100)
v.goto(-480,-100)
v.goto(-480,405)
v.end_fill()
#sun
v.fillcolor("yellow")
v.penup()
v.goto(0,-150)
v.pendown()
v.begin_fill()
v.circle(150)
v.end_fill()
# ground
v.penup()
v.fillcolor("moccasin")
v.begin_fill()
v.goto(470,-100)
v.pendown()
v.goto(470,-395)
v.goto(-480,-395)
v.goto(-480,-100)
v.goto(470,-100)
v.end_fill()
#clouds
v.fillcolor("lightgrey")
counttwo=0
newx=-350
rot=90
count=0
v.penup()
v.goto(newx,350)
v.pendown()

for i in range(4):
    #makes cloud
    for i in range(10):
        v.begin_fill()
        v.setheading(rot)
        v.circle(25,180)
        rot=rot+45
        v.end_fill()
        count=count+1
        #gets new position
        if count == 10:
            v.fillcolor("lightgrey")
            v.pensize(2)
            v.pencolor("lightgrey")
            v.begin_fill()
            v. setheading(-112)
            v.circle(64)
            v.end_fill()
            v.pencolor("black")
            v.pensize(10)
            newx=newx+250
            v.penup()
            v.goto(newx,350)
            v.pendown()
            
            count=0
            rot=90

count=0
newx=-350
newy= -50
v.fillcolor("green")
v.penup()
v.goto(newx,newy)
v.pendown()
for b in range(4):
    #make cactus
    for b in range(1):
        v.pencolor("black")
        v.setheading(0)
        v.begin_fill()
        v.forward(100)
        v.right(90)
        v.forward(300)
        v.right(90)
        v.forward(100)
        v.right(90)
        v.forward(300)
        v.end_fill() 
        newx = newx + 200
        newy = newy + -10
        count =+ 1
        #change location
        if count == 1:
            v.penup()
            v.goto(newx,newy)
            v.pendown()

v.penup()
v.goto(0,0)
v.pendown()
v.setheading(-24)
#make sun rays
for s in range(24):
    v.penup()
    v.forward(180)
    v.pendown()
    v.forward(20) 
    v.penup()
    v.goto(0,0)
    v.right(-10)

#birds
v.pencolor("black")
v.penup()
v.goto(350,150)
v.pendown()
v.setheading(90)
v.circle(25,180)
v.setheading(90)
v.circle(25,180)




v.speed(.5)
while count < 100000:
    #v form
    v.pencolor("black")
    v.penup()
    v.goto(-395,150)
    v.pendown()
    v.setheading(45)
    v.forward(45)
    v.penup()
    v.goto(-395,150)
    v.pendown()
    v.setheading(135)
    v.forward(45)
    #delete v form
    v.pencolor("skyblue")
    v.penup()
    v.speed(1)
    v.goto(-395,150)
    v.speed(0)
    v.pendown()
    v.setheading(45)
    v.forward(45)
    v.penup()
    v.goto(-395,150)
    v.pendown()
    v.setheading(135)
    v.forward(45)
    #arc form
    v.pencolor("black")
    v.penup()
    v.goto(-350,150)
    v.pendown()
    v.setheading(90)
    v.circle(25,180)
    v.setheading(90)
    v.circle(25,180)
    #delete arc form
    v.pencolor("skyblue")
    v.penup()
    v.speed(1)
    v.goto(-350,150)
    v.speed(0)
    v.pendown()
    v.setheading(90)
    v.circle(25,180)
    v.setheading(90)
    v.circle(25,180)
    #line form
    v.pencolor("black")
    v.penup()
    v.goto(-350,150)
    v.pendown()
    v.setheading(0)
    v.forward(-90)
    #delete line form
    v.pencolor("skyblue")
    v.penup()
    v.speed(1)
    v.goto(-350,150)
    v.speed(0)
    v.pendown()
    v.setheading(0)
    v.forward(-90)
    #arc form
    v.pencolor("black")
    v.penup()
    v.goto(-350,150)
    v.pendown()
    v.setheading(90)
    v.circle(25,180)
    v.setheading(90)
    v.circle(25,180)
    #delete arc form
    v.pencolor("skyblue")
    v.penup()
    v.speed(1)
    v.goto(-350,150)
    v.speed(0)
    v.pendown()
    v.setheading(90)
    v.circle(25,180)
    v.setheading(90)
    v.circle(25,180)














v.hideturtle()

wn = trtl.Screen()
wn.mainloop()