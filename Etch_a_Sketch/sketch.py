import turtle as t

my_turtle = t.Turtle()
my_turtle.pencolor("black")
my_turtle.pensize(3)
def move_forward():
    my_turtle.forward(20)
def move_backward():
    my_turtle.backward(20)
def move_left():
   new_heading = my_turtle.heading() + 20
   my_turtle.setheading(new_heading)

def move_right():
    new_heading = my_turtle.heading() - 20
    my_turtle.setheading(new_heading)

def clr_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen = t.Screen()
screen.listen()
screen.bgcolor("grey")
screen.onkeypress(move_forward, key="w")
screen.onkeypress(move_backward, key="s")
screen.onkeypress(move_left, key="a")
screen.onkeypress(move_right, key="d")
screen.onkey(clr_screen, key="c")

screen.exitonclick()