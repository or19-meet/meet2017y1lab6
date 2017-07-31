import turtle

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP

def up():
    global direction
    direction=UP
    print("you pressed UP!")

def left():
    global direction
    direction=LEFT
    print("you pressed LEFT!")

def down ():
    global direction
    direction=DOWN
    print("you pressed DOWN!")

def right():
    global direction
    direction=RIGHT
    print("you pressed RIGHT!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_MOVE)
turtle.listen()



    
