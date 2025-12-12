#importing modules
import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import datetime
# creat engine for text to speech
engine =pyttsx3.init()
# speak function
def speak(text):
    print("Assistant:",text)
    engine.say(text)
    engine.runAndWait()
# take command function
def take_command():
    listener=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listining......")
        audio=listener.listen(source)
        try:
            command=listener.recognize_google(audio)
            command=command.lower()
            print("You said :",command)
            return command
        except:
            return ""
# run assistant
def run_assistnt():
    command=take_command()
    # if command contais time
    if 'time' in command:
        time=datetime.datetime.now()
        speak(time)
        print("Current time is:",time)
    # if command contains open notepad
    elif 'open notepad' in command:
        speak("opening notepad")
        print("Opening notepad")
        os.system("notepad")
    #if command contains open youtube
    elif "open youtube" in command:
        speak("opening youtube")
        print("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    # if command contains hey chini
    elif "hey chini" in command:
        query=command.replace("hey chini","")
        if query:
            url=f"https://www.bing.com/search?q={query}"
            speak("searching for query")
            print("searching for query")
            webbrowser.open(url)
    #if command contains
    elif 'stop' in command:
        speak("okay, bye bye  we will catch up later")
        exit()
    else:
        print("i am here to assist you ask like current time ,open youtube ,search  for some thing....")
#main function
if __name__=="__main__":
    name=input("Enter your name  : ",)
    speak(f"hey hi{name},i am here to assist you ask like current time ,open youtube ,search  for some thing....")
    while True:
        run_assistnt()



