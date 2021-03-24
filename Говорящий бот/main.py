import eel
import pyttsx3
@eel.expose
def say(say_user):
    say_user_example = pyttsx3.init()
    say_user_example.say(say_user)
    say_user_example.runAndWait()
    if say_user == "TEST":
        say("Успешно")
eel.init("web")
eel.start("index.html", size=(500, 500))

#import os
