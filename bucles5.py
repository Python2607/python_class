import turtle


screen = turtle.Screen()
screen.title("Dibujar un corazón morado con Turtle")
screen.bgcolor("white")


t = turtle.Turtle()
t.color("purple")
t.speed(2)


t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()


t.hideturtle()


screen.mainloop()