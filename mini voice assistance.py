import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice",voices[2].id)

engine.setProperty("rate",170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def user_command_input():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening...")
            whatUsaid = listener.listen(source)
            print("got it")
            command = listener.recognize_google(whatUsaid)
            command = command.lower()
            print(command)
    except:
        ex = print('can not recognise what you said please talk again...')
        print(ex)
        talk(ex)
    return command
def run_tasks():
    user_input = user_command_input()
    user_input = user_input.lower()

    if "play" in user_input:
        play = user_input.replace("play", " ")
        print("playing " +play)
        talk("playing " +play)
        pywhatkit.playonyt(play)

    elif "youtube" in user_input:
        play = user_input.replace("youtube", " ")
        play = play.replace ("search"," ")
        print("searching " + play +" in youtube")
        talk("searching " + play + " in youtube")
        pywhatkit.playonyt(play)

    elif "time" in user_input:
        time = datetime.datetime.now().strftime("%I : %M %p")
        print(time)
        talk("current time is " + time)

    elif "wikipedia" in user_input:
        info = user_input.replace("wikipedia", " ")
        info = wikipedia.summary(info,2)
        print("here is the results from wikipedia :" + info)
        talk("here is the results from wikipedia :" + info)

    elif "who is" in user_input:
        info = user_input.replace("who is", " ")
        info = wikipedia.summary(info, 2)
        print("here is the results from wikipedia :" + info)
        talk("here is the results from wikipedia :" + "  " + info)

    elif "joke" in user_input:
        joke = pyjokes.get_joke("en","all")
        print(joke)
        talk(joke)

    else:
        exemption = "sorry i don't understand,please say again"
        print("sorry i don't understand,please say again")
        talk(exemption)
while True:
    run_tasks()
    if "bye" in user_command_input():
        break