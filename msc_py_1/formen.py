import turtle

turtle.reset()

turtle.speed("fastest")

# Aufgabe a) -> Quadrat zeichnen
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

# Turtle nach rechts bewegen um die nächste Aufgabe zu beginnen
# Hierzu heben wir zudem den Stift an, da sonst eine Linie gezeichnet werden würde
turtle.penup()
turtle.forward(60)
turtle.pendown()

# Aufgabe b) -> Rechteck zeichnen
turtle.forward(50) # Seitenlänge
turtle.left(90)
turtle.forward(25) # Höhe
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)

turtle.penup()
turtle.forward(60)
turtle.pendown()

# Aufgabe c)
turtle.pensize(5)
turtle.color("blue")
turtle.left(45)
turtle.forward(50)

turtle.right(90)
turtle.color("red")
turtle.forward(50)

turtle.color("cyan")
turtle.left(90)
turtle.forward(50)

turtle.right(90)
turtle.color("black")
turtle.forward(50)

# Strichdicke und Rotation zurücksetzen
turtle.pensize(1)
turtle.left(45)

turtle.penup()
turtle.forward(10)
turtle.pendown()

# Aufgabe d)

turtle.pensize(5)
turtle.color("red")
# Grundfläche des Dreiecks anhand der Seitenlängen (50) mit Satz des Pythagoras berechnen
turtle.forward((50**2 + 50**2)**0.5)
turtle.left(135)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Strichdicke und Rotation zurücksetzen
turtle.pensize(1)
turtle.left(135)

turtle.penup()
turtle.forward(((50**2 + 50**2)**0.5) + 10)
turtle.pendown()

# Aufgabe e)

turtle.pensize(5)

# Blaues Dreieck
turtle.color("blue")

turtle.forward((50**2 + 50**2)**0.5)
turtle.left(135)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.left(135)

turtle.penup()
turtle.forward((50**2 + 50**2)**0.5)
turtle.pendown()

# Rotes Dreieck
turtle.color("red")

turtle.forward((50**2 + 50**2)**0.5)
turtle.left(135)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Rotation hier nicht zurücksetzen und gleich grünes Dreieck zeichnen

turtle.color("green")

turtle.forward(50)
turtle.left(135)
turtle.forward((50**2 + 50**2)**0.5)
turtle.left(135)
turtle.forward(50)

turtle.exitonclick()