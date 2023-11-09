import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (500)
t.color('#4689BC')



def triangulo(tamaño):
    t.pendown()
    for _ in range(3):
        t.forward(tamaño)
        t.left(120)

def ir_a(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    pass

ir_a(-200, 100)
triangulo(100)

ir_a(50, 100)
triangulo(50)

ir_a(0, -100)
triangulo(150)

ir_a(-120, -20)
triangulo(200)

t.hideturtle()
turtle.exitonclick()
