import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Gie Gie in the chat.")

answer = pg.prompt("Enter your favorite color.")

if answer == "orange":
    speak.Speak("My favorite color is orange too! We must be twins.")

elif answer == "blue":
    speak.Speak("I don't like blue as much as IO like orange.")

else:
    speak.Speak("You liker the color " + answer)



speak.Speak("What kind of video should we watch?")

video = pg.prompt("Enter video below.")

speak.Speak("Ok, let's look for" + video + "on youtube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
