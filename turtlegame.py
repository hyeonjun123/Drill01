import turtle

wn = turtle.Screen()

turtle.shape("turtle")


# 이동 함수
def move_up():
     turtle.setheading(90)
     turtle.forward(50)
     turtle.stamp()
     
def move_down():
     turtle.setheading(270)
     turtle.forward(50)
     turtle.stamp()

def move_left():
     turtle.setheading(180)
     turtle.forward(50)
     turtle.stamp()


def move_right():
     turtle.setheading(0)
     turtle.forward(50)
     turtle.stamp()

    

turtle.listen()
turtle.onkey(move_up, "W")
turtle.onkey(move_down, "S")
turtle.onkey(move_left, "A")
turtle.onkey(move_right, "D")


def restart_game():
    turtle.reset()
    

turtle.onkey(restart_game, "Escape")


wn.mainloop()
