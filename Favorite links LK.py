import webbrowser
import pyautogui as pg

fails = ["https://www.youtube.com/watch?v=IqTk1je6iYs"]

vines = ["https://www.youtube.com/watch?v=x0uXVy4fzUA"]




answer = pg.prompt(
"""
Which would you like to do?
a) Watch fails
b) Watch best vines of 2017

"""
    )

if answer == "a":
    for i in videos:
        webrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
