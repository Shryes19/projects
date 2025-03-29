import turtle

import pandas
import time

screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
states = []
i = 0
s = 0

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
dic = data.to_dict()
d = dic['state']
x = dic["x"]
y = dic["y"]

ans_state = screen.textinput(title="0/50 Guess the name", prompt="What's the other state's name")
ans = [ans_state.lower()]
while i < 50:
    if d[i].lower() == ans_state.lower():
        ans.append(d[i].lower())
        tim.goto(x[i], y[i])
        tim.write(d[i])
        time.sleep(1)
        s += 1
        if s == 50:
            break
        ans_state = screen.textinput(title=f"{s}/50 States correct", prompt="What's the other state's name")
        if ans_state.lower() not in ans:
            i = 0
            continue
        else:
            ans_state = screen.textinput(title=f"{s}/50 States correct", prompt="What's the other state's name")
            i = 0

    elif i == 49 and d[i].lower() != ans_state.lower():
        ans_state = screen.textinput(title=f"{s}/50 States correct", prompt="What's the other state's name")
        if ans_state.lower() not in ans:
            i = 0
            continue
        else:
            ans_state = screen.textinput(title=f"{s}/50 States correct", prompt="What's the other state's name")
            i = 0



    else:
        i += 1



tim.goto(0,0)
tim.write("YOU WIN",align="center",font=("Courier", 26, "normal"))

screen.exitonclick()




