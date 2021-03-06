import turtle
from turtle import *
from random import randint
import time


window1 = turtle.Screen()
window1.bgcolor("black")
time.sleep(4)
turtle.color("white")
turtle.write("WELCOME TO TURTLE RACE", font=("Bauhaus 93", 35, "bold"))
turtle.penup()
time.sleep(4)
turtle.clearscreen()

window2 = turtle.Screen()
window2.bgcolor("yellow")
turtle.penup()
goto(0,50)
turtle.write("MAIN MENU",font = ("Bauhaus 90",20,"bold"))
turtle.penup()
time.sleep(2)
goto(-3,2)
turtle.write("1. new game",font = ("Bauhaus 70",15,"bold"))
turtle.penup()
time.sleep(2)
goto(-3,-30)
turtle.write("2. about",font = ("Bauhaus 70",15,"bold"))
turtle.penup()
time.sleep(3)
goto(-3,-62)
turtle.write("3. exit",font = ("Bauhaus 70",15,"bold"))
turtle.penup()
time.sleep(3)
turtle.clearscreen()

window3 = turtle.Screen()
window3.bgcolor("pink")
screen = turtle.getscreen()
choice = screen.textinput("enter your choice(menu,about or exit):","enter your choice(new game,about or exit):")
if choice == ("new game"):
        window4 = turtle.Screen()
        window4.bgcolor("orange")
        turtle.write("NEW GAME",font = ("Bauhaus 80",15,"bold"))
        time.sleep(3)
        screen2 = turtle.getscreen()
        choice2 = screen2.textinput("enter your turtle color(menu,about or exit):","enter your turtle color(red,blue,white,yellow or pink):")
        turtle.clearscreen()

        window = turtle.Screen()
        window.bgcolor("forest green")
        turtle.speed(0)
        turtle.penup()
        turtle.setpos(-300,200)
        window.title("Turtle Race")
        turtle.write("TURTLE RACE", font=("Bauhaus 93", 20, "bold"))
        turtle.penup()

        border_pen=turtle.Turtle()
        border_pen.speed(2)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-100,-300)
        border_pen.pendown()
        border_pen.pensize(4)
        for side in range(5):
            border_pen.fd(600)
            border_pen.lt(90)
                
        goto(-50,250)
        for steps in range(16):
            write(steps)
            right(90)
            forward(15)
            pendown()
            forward(200)
            penup()
            backward(215)
            left(90)
            forward(30)
        time.sleep(2)
        goto(-50,70)    
        for steps in range(16):
                    right(90)
                    forward(15)
                    pendown()
                    forward(200)
                    penup()
                    backward(215)
                    left(90)
                    forward(30)

        time.sleep(2) 
        goto(-50,3)    
        for steps in range(16):
                    right(90)
                    forward(15)
                    pendown()
                    forward(200)
                    penup()
                    backward(215)
                    left(90)
                    forward(30)

                


        ada = turtle.Turtle()
        ada.color('red')
        ada.shape('turtle')
        ada.penup()
        ada.speed(0)
        ada.goto(-80,200)
        ada.pendown()
        adaspeed=10


        bob = turtle.Turtle()
        bob.color('blue')
        bob.shape('turtle')
        bob.penup()
        bob.goto(-80,100)
        bob.pendown()


        cob = turtle.Turtle()
        cob.color('white')
        cob.shape('turtle')
        cob.penup()
        cob.goto(-80,0)
        cob.pendown()

        sob = turtle.Turtle()
        sob.color('yellow')
        sob.shape('turtle')
        sob.penup()
        sob.goto(-80,-100)
        sob.pendown()


        fob =turtle.Turtle()
        fob.color('pink')
        fob.shape('turtle')
        fob.penup()
        fob.goto(-80,-200)
        fob.pendown()
                
        time.sleep(3)
        for turn in range(100):
                    ada.forward(randint(1,11))
                    bob.forward(randint(1,9))
                    cob.forward(randint(1,9))
                    sob.forward(randint(1,8))
                    fob.forward(randint(1,8))

        if choice2 == ("red"):
                    turtle.penup()
                    goto(-15,25)
                    time.sleep(3)
                    turtle.write("YOU WON THE GAME", font=("Bauhaus 80", 20, "bold"))
                    turtle.penup()
                    time.sleep(3)
                    turtle.clearscreen()
                    turtle.setpos(0,0)
                    time.sleep(2)
                    turtle.write("GAME OVER!!!", font=("Bauhaus 93", 40, "bold"))
                    turtle.penup()
                    time.sleep(3)
                    window.exitonclick()

        else:
                    turtle.penup()
                    goto(-15,25)
                    time.sleep(3)
                    turtle.write("YOU LOST THE GAME", font=("Bauhaus 80", 20, "bold"))
                    turtle.penup()
                    time.sleep(3)
                    turtle.clearscreen()
                    turtle.setpos(0,0)
                    time.sleep(2)
                    turtle.write("GAME OVER!!!", font=("Bauhaus 93", 40, "bold"))
                    turtle.penup()
                    time.sleep(3)
                    window.exitonclick()

elif choice == ("about"):
                turtle.penup()
                goto(-25,180)
                turtle.write("ABOUT",font = ("Bauhaus 80",25,"bold"))
                turtle.penup()
                time.sleep(3)
                goto(-650,-30)
                turtle.write("This game introduce loops through a fun turtle race game.Loops are used to draw the race track and to make the turtle move a random \n number of steps each turn\n",font = ("Bauhaus 70",15,"bold"))
                time.sleep(2)
                goto(-650,-50)
                turtle.write("If you have a group of people to play the game ,each person pick a turtle and the one that gets the furthest is the winner.",font = ("Bauhaus 70",15,"bold"))
                time.sleep(7)
                turtle.clearscreen()
                window3.exitonclick()
                
elif choice == ("exit"):
                turtle.write("EXIT",font = ("Bauhaus 80",15,"bold"))
                time.sleep(3)
                turtle.clearscreen()
                time.sleep(3)
                window3.exitonclick()

else:
                turtle.write("INCORRECT CHOICE",font = ("Bauhaus 80",15,"bold"))
                time.sleep(3)
                turtle.clearscreen()
                time.sleep(3)
                window3.exitonclick()
