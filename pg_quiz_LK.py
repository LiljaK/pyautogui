import pyautogui as pg
import time
import webbrowser
points = 0

#question
answer =pg.prompt(
"""
Which would you rather do?

a) slap battle with a friend
b) get a butterfly tatoo

"""
    )

# Give points
if answer == "a":
    points +=1
elif answer == "b":
    points += 2



    




# END OF SURVEY

pg.alert("You are.....")

#ted
if points == 2:
    pg.alert ("Ted")
    webrowser.open("https://uproxx.files.wordpress.com/2014/09/ted-mosby.jpg?quality=100&w=650")
#barney
elif points == 1:
    pg.alert ("Barney")
    webbrowser.open ("https://i.imgur.com/aDCdAyb.gif")
    
