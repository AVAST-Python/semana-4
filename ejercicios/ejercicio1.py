import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (50)
t.color('#4689BC')

t.penup()
t.goto(-250, 0)
t.pendown()


# Polígono regular
lados = 5
largo_lado = 100

angulo_interno = 180 * (lados - 2) / lados
angulo_giro = 180 - angulo_interno

for vuelta in range(lados):
    t.forward(largo_lado)
    t.left(angulo_giro)


t.penup()
t.goto(100, 0)
t.setheading(0)
t.pendown()

# Extra: con el vértice abajo
lados = 5
largo_lado = 100

angulo_interno = 180 * (lados - 2) / lados
angulo_giro = 180 - angulo_interno
giro_inicial = 90 - angulo_interno / 2

t.left(giro_inicial)
for vuelta in range(lados):
    t.forward(largo_lado)
    t.left(angulo_giro)


t.hideturtle()
turtle.exitonclick()
