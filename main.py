import time
import turtle

import pandas as pd

ALIGNMENT = 'center'
FONT = ("Arial",30,'normal')

screen = turtle.Screen()
screen.title("Can You Name All The States?")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

correct = 0

# read the csv
df = pd.read_csv("50_states.csv")
states = df["state"].to_list()

guessed = set()

while correct < 50:
    answer_state = screen.textinput(title=f"{correct}/50 States Guessed",prompt="What's another state?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in states and answer_state not in guessed:
        guessed.add(answer_state)
        correct += 1

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x,y = int(df[df['state']==answer_state]['x']),int(df[df['state']==answer_state]['y'])
        t.goto(x,y)
        t.write(answer_state)

missed = [state for state in states if state not in guessed]

if correct < 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(f"You have guessed {correct} states.\nHere are the states that you missed", align=ALIGNMENT, font=FONT)
    time.sleep(2)
    t.clear()

    for state in states:
        if state not in guessed:
            t = turtle.Turtle()
            t.color("red")
            t.hideturtle()
            t.penup()
            x, y = int(df[df['state'] == state]['x']), int(df[df['state'] == state]['y'])
            t.goto(x, y)
            t.write(state)

# write the missed states to a csv
    df = pd.DataFrame(missed)
    df.to_csv("states_to_learn.csv")


else:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(f"You have guessed {correct} states. Congratulations!", align=ALIGNMENT, font=FONT)
    time.sleep(2)
    t.clear()

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, 0)
t.write(f"Thanks for playing!", align=ALIGNMENT, font=FONT)


screen.exitonclick()