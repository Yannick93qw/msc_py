import turtle

turtle.reset()
turtle.speed("fastest")

# Aufgabe a)
turtle.pensize(5)
turtle.color("red")

# Gelbes Dreieck
turtle.fillcolor("yellow")

turtle.begin_fill()
turtle.left(45)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(135)
turtle.forward((60**2 + 60**2)**0.5)
turtle.end_fill()

# Turtle zur Startposition des grünen Dreiecks bewegen
turtle.left(135)
turtle.forward(60)

# Grünes Dreieck
turtle.fillcolor("lime")

turtle.begin_fill()
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(135)
turtle.forward((60**2 + 60**2)**0.5)
turtle.end_fill()

# Turtle zur Startposition des cyan Dreiecks bewegen
turtle.penup()
turtle.forward((60**2 + 60**2)**0.5)
turtle.left(90)
turtle.pendown()

# Cyan Dreieck
turtle.fillcolor("cyan")

turtle.begin_fill()
turtle.left(45)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(135)
turtle.forward((60**2 + 60**2)**0.5)
turtle.end_fill()

# Turtle nach Rechts bewegen um die Quadrat Blume zu zeichnen
turtle.penup()
turtle.home()
turtle.forward(350)
turtle.pendown()

# Aufgabe b)
# Da sich die Quadrate überlappen und das Quadrat welches zuerst gezeichnet wird hinter den anderen ist (Last wins)
# müssen die Quadrate in folgender Reihenfolge gezeichnet werden
# Cyan, Gelb, Magenta, Blau, Lime

turtle.right(25)

# Cyan Quadrat
turtle.fillcolor("cyan")
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.end_fill()

# Zur Startposition für das gelbe Quadrat gehen
turtle.penup()
turtle.left(10)
turtle.forward(50)
turtle.pendown()



# Zur Startposition des grünen Quadrates gehen und schräger Winkel einstellen




turtle.exitonclick()