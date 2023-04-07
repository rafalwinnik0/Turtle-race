from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
#user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
players = ["Rafał", "Tomek", "Kuba", "Krzysiek", "Marcin"]
turtles = []

new_position = -100
n = 0
for player in players:
    player = Turtle(shape="turtle")
    player.color(colors[n])
    n += 1
    player.penup()
    new_position += 30
    player.goto(x=-230, y=-new_position)
    turtles.append(player)

is_on = True
while is_on:
    for turtle in turtles:
        turtle.forward(10)
        if turtle.xcor() == 230:
            is_on = False
            break


screen.exitonclick()
