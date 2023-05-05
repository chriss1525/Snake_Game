# simple snake game

import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0

# set up screen
box = turtle.Screen()
box.title("Snake game")
box.bgcolor("green")
box.setup(width=600, height=600)
box.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# apple

apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(0, 100)


segments = []

# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center",
          font=("Courier", 24, "normal"))


# Functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"

def stop():
    head.direction = "stop"


# keyboard bindings
box.listen()
box.onkeypress(go_up, "Up")
box.onkeypress(go_down, "Down")
box.onkeypress(go_left, "Left")
box.onkeypress(go_right, "Right")
box.onkeypress(stop, "space")

# More Functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# main game loop
while True:
    box.update()

    # check for collision with borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # reset score
        score = 0

        # clear the segments list
        segments.clear()

    # check for a collision with food
    if head.distance(apple) < 20:
        # move food to different random spot
        x = random.randint(- 290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)

        # add segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # move end segments first
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments list
            segments.clear()
            score = 0

    time.sleep(delay)

box.mainloop()
