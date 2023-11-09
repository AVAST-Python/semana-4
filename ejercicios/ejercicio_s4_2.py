import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (500)
t.color('#4689BC')

largo_rayas = 30
distancia_lineas = 50

t.penup()
t.goto(-400, 100)
t.pendown()

# Changing colors from a number

for num in range(5):
    if num >= 3:
        t.color('red')
    else:
        t.color('blue')
    t.forward(largo_rayas)
    t.penup()
    t.forward(largo_rayas)
    t.pendown()


t.penup()
t.goto(0, 100)
t.pendown()


# Alternating colors
for num in range(5):
    if num % 2 == 0:
        t.color('red')
    else:
        t.color('blue')
    t.forward(largo_rayas)
    t.penup()
    t.forward(largo_rayas)
    t.pendown()




t.penup()
t.goto(-200, -100)
t.pendown()

# Alternating colors through a counter
contador = 0

for _ in range(4):

    for _ in range(5):
        if contador % 2 == 0:
            t.color('red')
        else:
            t.color('blue')
        contador = contador +1

        t.forward(largo_rayas)
        t.penup()
        t.forward(largo_rayas)
        t.pendown()

    t.penup()
    t.right(90)
    t.forward(distancia_lineas)
    t.left(90)
    t.backward(largo_rayas*2*5)
    t.pendown()


t.hideturtle()
turtle.exitonclick()
