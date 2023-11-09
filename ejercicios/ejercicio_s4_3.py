import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (500)
t.color('#4689BC')

t.penup()
t.goto(-400, 100)
t.pendown()


# Rows of lines
largo_rayas = 30
distancia_lineas = 50

def dibujar_linea():
    for _ in range(5):
        t.forward(largo_rayas)
        t.penup()
        t.forward(largo_rayas)
        t.pendown()

def bajar():
    t.penup()
    t.right(90)
    t.forward(distancia_lineas)

def volver_al_principio():
    t.left(90)
    t.backward(largo_rayas*2*5)
    t.pendown()

for _ in range(4):
    dibujar_linea()
    bajar()
    volver_al_principio()


t.penup()
t.goto(150, 100)
t.pendown()

# Squares in squares
cuadrado_pequeño = 100
cuadrado_grande = 200

def cuadrado():
    for _ in range(4):
        t.left(90)
        t.forward(cuadrado_pequeño)

for _ in range(4):
    t.forward(cuadrado_grande)
    cuadrado()
    t.right(90)


t.hideturtle()
turtle.exitonclick()
