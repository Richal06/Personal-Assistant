import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import datetime

engine = pyttsx3.init()

def speak(audio, voice='male'):
    engine.setProperty('voice', get_voice_id(voice))
    engine.say(audio)
    engine.runAndWait()

def get_voice_id(voice):
    voices = engine.getProperty('voices')
    if voice == 'female':
        return voices[1].id
    else:
        return voices[0].id

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    date = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak("Today's date is")
    speak(date)
    print("Today's date is ", date)

def wishme():
    print("Welcome back!")
    speak("Welcome back!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    elif 16 <= hour < 24:
        speak("Good Evening!")
        print("Good Evening!")
    else:
        speak("Good Night!")

    speak("I'm Your Buddy, your personal assistant. How may I assist you?")
    print("I'm Your Buddy, your personal assistant. How may I assist you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm Your Buddy, a virtual assistant created by Richa.")

        elif "how are you" in query:
            responses = ["I'm doing well, thank you for asking!", "I'm great, thanks for asking!",
                         "I'm feeling wonderful, thank you!", "I'm fantastic, how about you?"]
            speak(random.choice(responses))

        elif "fine" in query or "good" in query:
            responses = ["That's great to hear!", "Awesome!", "Glad to hear that!", "Good to know!"]
            speak(random.choice(responses))

        elif "wikipedia" in query:
            try:
                speak("Searching on Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(result)
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't find any relevant information on Wikipedia.")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            browser = wb.get('chrome')
            browser.open_new_tab("https://www.google.com")
            speak("What would you like to search for?")
            search_query = takecommand()
            browser.open_new_tab(f"https://www.google.com/search?q={search_query}")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "YOUR_MUSIC_DIRECTORY"
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("Sorry, I couldn't find any music in your directory.")

        elif "open chrome" in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif "search on chrome" in query:
            speak("What should I search?")
            search = takecommand()
            wb.open_new_tab(f"https://www.google.com/search?q={search}")

        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            with open("data.txt", "w") as f:
                f.write(data)
            speak("You asked me to remember: " + data)

        elif "do you remember anything" in query:
            try:
                with open("data.txt", "r") as f:
                    data = f.read()
                speak("You asked me to remember: " + data)
            except FileNotFoundError:
                speak("Sorry, I don't have anything to remember.")

        elif "screenshot" in query:
            img = pyautogui.screenshot()
            img_path = "screenshot.png"
            img.save(img_path)
            speak("Screenshot taken successfully!")

        elif "offline" in query:
            speak("Going offline. Goodbye!")
            break

        elif "play a song" in query:
            speak("Sure, playing a random song on YouTube.")
            wb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Rick Roll ;-)
