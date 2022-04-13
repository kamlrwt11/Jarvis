import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random


# for getting voices
# sapi5 for windows
# nsss for macos, its a driver
engine = pyttsx3.init('sapi5')

# gets the current value of an engine property
voices = engine.getProperty('voices')
# print(voices[0].id)

# voices[0].id for boy and voices[1].id for girl
#   setproperty is used for change in voices
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # it makes the speech audible in system.
    engine.runAndWait()


def wishme():
    # it is used fot getting current time and date
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Kamal Singh Rawat")

    elif hour >= 12 and hour <16:
        speak("Good Afternoon! Kamal Singh Rawat")

    else:
        speak("Good Evening! Kamal Singh Rawat")

    speak("Sir, i am jarvis how can i help you")


def takecommand():
    # it take microphone input from the user and return string output
    r = sr.Recognizer()
    # using audio input as source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # listen for the first phrase and extract it into audio data   
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kamalrawatstg153@gmail.com", 'password123456789')
    server.sendmail('kamalrawatstg153@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()

    #while True:
    if 1:
        query = takecommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'play music' in query:
            music_dir = "A:\Audio"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codepath = "C:\\Users\KAMAL RAWAT\Downloads\VSCodeUserSetup-x64-1.63.2.exe"
            os.startfile(codepath)

        elif "email to kamal" in query:
            try:
                speak("What should i say")
                content = takecommand()
                to = "kamalrawatstg153@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend kamal bhai, I am not able to send this email")
