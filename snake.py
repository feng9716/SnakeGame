from turtle import Turtle, Screen

STARTING_POSITION = [(20,0), (0, 0), (-20, 0)]
STEP = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_segment(STARTING_POSITION[i])

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(STEP)

    def head_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def head_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def head_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def head_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.speed("fastest")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
