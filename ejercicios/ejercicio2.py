import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (500)
t.color('#4689BC')

t.penup()
t.goto(-450, 100)
t.pendown()


# Escalera reducing
for vuelta in range(4):
    t.left(90)
    t.forward(100-25*vuelta)
    t.right(90)
    t.forward(100-25*vuelta)


t.penup()
t.goto(-250, 100)
t.pendown()

# Pinchos increasing
for vuelta in range(7):
    t.left(90)
    t.forward(30*vuelta)
    t.left(180)
    t.forward(30*vuelta)
    t.left(90)
    t.forward(30*vuelta)


t.penup()
t.goto(-150, -250)
t.pendown()

# Extra: Flor
lado = 10
vueltas = 30
for num_vuelta in range(vueltas):

    t.forward(num_vuelta * lado)
    t.left(90+10)

t.hideturtle()
turtle.exitonclick()
