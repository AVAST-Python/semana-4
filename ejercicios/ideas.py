import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (50)
t.color('#4689BC')


length = 150
sides = 3

# Polígono reduciéndose
for _ in range(5*sides):
    length = length - 10
    if length < 0:
        break
    t.forward(length)
    t.left(360/sides)



t.hideturtle()
turtle.exitonclick()
