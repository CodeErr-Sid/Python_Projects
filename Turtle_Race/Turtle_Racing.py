import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.bgcolor("black")

user_bet = screen.textinput(title="Make Your Bet!.", prompt="Which Turtle Wins ?, Guess A Colour: ")

color = ["blue", "orange", "red", "green", "pink", "yellow"]
y_position = [-70, -40, -10, 20, 50, 80]

all_turtles =  []

for index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    screen.setup(width=500, height=400)
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="Result!", prompt=f"You've Won :), The {winning_color} Turtle is The Winner!!\n Type Anything to End")

            else:
                screen.textinput(title="Result!", prompt=f"You've Lost :(, The {winning_color} Turtle is The Winner!!\n Type Anything to End")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


