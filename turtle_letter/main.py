import turtle

def Gruppe_1_N():
	def draw_rounded_rect(width, height, color):
		turtle.fillcolor(color)
		turtle.begin_fill()
		turtle.forward(width)
		turtle.circle(height, 180)
		turtle.forward(width)
		turtle.circle(height, 180)
		turtle.end_fill()


	def draw_rect(width, height, color):
		turtle.fillcolor(color)
		turtle.begin_fill()
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)
		turtle.end_fill()

	def draw_n(left_segment_color, middle_segment_color, right_segment_color):
		# Draw left most part of the N.
		draw_rounded_rect(360, 20, left_segment_color)

		# Move to the start location of the middle '|' of the N.
		turtle.penup()
		turtle.forward(355)
		turtle.left(90)
		turtle.forward(39)
		turtle.right(90)
		turtle.right(165)
		turtle.pendown()

		# Draw middle part of the N.
		draw_rounded_rect(373, 20, middle_segment_color)

		# Move to the start location of the right '|' of the N.
		turtle.penup()
		turtle.forward(388)
		turtle.left(75)
		turtle.forward(35)
		turtle.left(90)
		turtle.forward(20)
		turtle.pendown()

		# Draw right most part of the N.
		draw_rounded_rect(360, 20, right_segment_color)

	# Draw border
	turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90);turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90)

	# Draw black background
	draw_rect(300, 400, "black")

	# Move to start location of the N.
	turtle.penup()
	turtle.forward(125)
	turtle.left(90)
	turtle.forward(20)
	turtle.pendown()
	draw_n("#B00710", "#E50914", "#B00710")

	# Move to the bottom right corner with the cursor facing right
	turtle.penup()
	turtle.right(180)
	turtle.forward(20)
	turtle.left(90)
	turtle.forward(80)
	turtle.pendown()

turtle.reset()
turtle.speed("fastest")
Gruppe_1_N()
turtle.exitonclick()