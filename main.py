from math import modf
import turtle
import random
import time

wn = turtle.Screen()
wn.setup(800, 500)
wn.title("Cube Timer")
wn.bgcolor("#ffdda6")


class Pen(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)

    def line(self, start_x, start_y):
        self.up()
        self.setpos(start_x, start_y)
        self.color("black")
        self.pensize(2)
        self.down()
        self.fd(233)

    def rectangle(self, start_x, start_y):
        self.up()
        self.setpos(start_x, start_y)
        self.color("black")
        self.fillcolor("white")
        self.pensize(2)
        self.down()
        self.begin_fill()
        for _ in range(2):
            self.fd(233)
            self.left(90)
            self.fd(200)
            self.left(90)
        self.end_fill()

    def text(self, x, y, text, align, size, style):
        self.up()
        self.goto(x, y)
        self.write(text, align=align, font=("Arial", size, style))


def nothing():
    pass


def start_page():
    ui()
    timer_pen.text(0, 100, "0.00", "center", 80, "normal")
    scramble()

    wn.onkeypress(start_key_press, "Return")
    wn.listen()


def ui():
    ui_pen.rectangle(-375, -225)
    ui_pen.rectangle(-117, -225)
    ui_pen.rectangle(141, -225)
    ui_pen.line(-375, -185)
    ui_pen.line(-375, -145)
    ui_pen.line(-375, -105)
    ui_pen.line(-375, -65)
    ui_pen.line(141, -185)
    ui_pen.line(141, -145)
    ui_pen.line(141, -105)
    ui_pen.line(141, -65)
    ui_pen.text(-.5, -60, "Welcome to", "center", 16, "bold")
    ui_pen.text(-.5, -90, "Cube Timer!", "center", 16, "bold")
    ui_pen.text(-.5, -135, "Press ENTER to start", "center", 16, "bold")
    ui_pen.text(-.5, -185, "Press SPACE to finish", "center", 16, "bold")
    ui_pen.text(-341, -60, "1.", "center", 16, "normal")
    ui_pen.text(-341, -100, "2.", "center", 16, "normal")
    ui_pen.text(-341, -140, "3.", "center", 16, "normal")
    ui_pen.text(-341, -180, "4.", "center", 16, "normal")
    ui_pen.text(-341, -220, "5.", "center", 16, "normal")
    ui_pen.text(-258.5, -20, "Top 5", "center", 18, "bold")
    ui_pen.text(257.5, -20, "Solves", "center", 18, "bold")


def scramble():
    moves = ("L", "L2", "L'",
             "R", "R2", "R'",
             "F", "F2", "F'",
             "B", "B2", "B'",
             "U", "U2", "U'",
             "D", "D2", "D'")
    output = []
    prev = 'ZZ'
    count = 0
    while count < 20:
        pos = random.randrange(18)
        if moves[pos][0] != prev[0]:
            output.append(moves[pos])
            prev = moves[pos]
            count += 1
    timer_pen.text(0, 50, ' '.join(output), "center", 15, "normal")


def solve_one():
    index = int(solve_number)
    first_solve = solve_times[index]
    ui_pen.text(175, -60, str(solve_number + 1) + ".", "center", 16, "normal")
    ui_pen.text(257.5, -60, first_solve, "center", 16, "normal")


def solve_two():
    index = int(solve_number + 1)
    second_solve = solve_times[index]
    ui_pen.text(175, -100, str(solve_number + 2) + ".", "center", 16, "normal")
    ui_pen.text(257.5, -100, second_solve, "center", 16, "normal")


def solve_three():
    index = int(solve_number + 2)
    third_solve = solve_times[index]
    ui_pen.text(175, -140, str(solve_number + 3) + ".", "center", 16, "normal")
    ui_pen.text(257.5, -140, third_solve, "center", 16, "normal")


def solve_four():
    index = int(solve_number + 3)
    fourth_solve = solve_times[index]
    ui_pen.text(175, -180, str(solve_number + 4) + ".", "center", 16, "normal")
    ui_pen.text(257.5, -180, fourth_solve, "center", 16, "normal")


def solve_five():
    index = int(solve_number + 4)
    fifth_solve = solve_times[index]
    ui_pen.text(175, -220, str(solve_number + 5) + ".", "center", 16, "normal")
    ui_pen.text(257.5, -220, fifth_solve, "center", 16, "normal")


def start_key_press():
    wn.listen()
    wn.onkeypress(nothing, "Return")
    wn.onkeyrelease(start_key_release, "Return")
    wn.bgcolor("red")
    timer_pen.clear()
    ui_pen.clear()


def start_key_release():
    global t1
    wn.listen()
    wn.onkeyrelease(nothing, "Return")
    wn.onkeypress(stop_key_press, "space")
    wn.bgcolor("green")
    t1 = time.time()


def stop_key_press():
    global solve_number
    wn.listen()
    wn.onkeypress(nothing, "space")
    wn.onkeypress(start_key_press, "Return")
    wn.bgcolor("#ffdda6")
    t2 = time.time()
    m = int(t2 - t1) // 60
    s = round(float(t2 - t1) % 60, 2)
    whole = round(float(t2 - t1) % 60, 1)
    if len(str(m)) == 1:
        mm = '0' + str(m)
    else:
        mm = str(m)
    if len(str(s)) == 3:
        ss = '0' + str(s) + '0'
    elif len(str(s)) == 4 and len(str(whole)) == 3:
        ss = '0' + str(s)
    elif len(str(s)) == 4 and len(str(whole)) == 4:
        ss = str(s) + '0'
    else:
        ss = str(s)
    timer_pen.text(0, 100, str(mm + ":" + ss), "center", 80, "normal")
    solve_times.append(str(mm + ":" + ss))
    top_solves.append(str(mm + ":" + ss))
    top_solves.sort()
    ui()
    scramble()
    if len(solve_times) == 1:
        solve_one()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
    if len(solve_times) == 2:
        solve_one()
        solve_two()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
        ui_pen.text(-258.5, -100, str(top_solves[1]), "center", 16, "normal")
    if len(solve_times) == 3:
        solve_one()
        solve_two()
        solve_three()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
        ui_pen.text(-258.5, -100, str(top_solves[1]), "center", 16, "normal")
        ui_pen.text(-258.5, -140, str(top_solves[2]), "center", 16, "normal")
    if len(solve_times) == 4:
        solve_one()
        solve_two()
        solve_three()
        solve_four()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
        ui_pen.text(-258.5, -100, str(top_solves[1]), "center", 16, "normal")
        ui_pen.text(-258.5, -140, str(top_solves[2]), "center", 16, "normal")
        ui_pen.text(-258.5, -180, str(top_solves[3]), "center", 16, "normal")
    if len(solve_times) == 5:
        solve_one()
        solve_two()
        solve_three()
        solve_four()
        solve_five()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
        ui_pen.text(-258.5, -100, str(top_solves[1]), "center", 16, "normal")
        ui_pen.text(-258.5, -140, str(top_solves[2]), "center", 16, "normal")
        ui_pen.text(-258.5, -180, str(top_solves[3]), "center", 16, "normal")
        ui_pen.text(-258.5, -220, str(top_solves[4]), "center", 16, "normal")
    if len(solve_times) > 5:
        solve_number = solve_number + 1
        solve_one()
        solve_two()
        solve_three()
        solve_four()
        solve_five()
        ui_pen.text(-258.5, -60, str(top_solves[0]), "center", 16, "normal")
        ui_pen.text(-258.5, -100, str(top_solves[1]), "center", 16, "normal")
        ui_pen.text(-258.5, -140, str(top_solves[2]), "center", 16, "normal")
        ui_pen.text(-258.5, -180, str(top_solves[3]), "center", 16, "normal")
        ui_pen.text(-258.5, -220, str(top_solves[4]), "center", 16, "normal")


timer_pen = Pen()
ui_pen = Pen()

solve_times = []
top_solves = []
solve_number = 0

start_page()

turtle.done()
