import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit  # ✅ Added for playing YouTube
import wikipedia

# 💡 Make sure to install these before running:
# pip install speechrecognition pyttsx3 pywhatkit wikipedia

def say(text):
    print(f"[Jarvis says]: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening for your command...")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("🔍 Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"✅ You said: {query}")
            return query
    except sr.RequestError:
        print("❌ Could not request results; check your internet connection.")
    except sr.UnknownValueError:
        print("❌ Sorry, I did not understand the audio.")
    except Exception as e:
        print(f"❌ An error occurred in speech recognition: {e}")
    return ""

def run_vivo(command):
    # Handles 'play' commands
    if 'play' in command:
        song = command.replace('play', '').strip()
        if song:
            say(f'Playing {song}')
            pywhatkit.playonyt(song)
        else:
            say("Please tell me which song to play.")
    else:
        say("Sorry, I can only play songs in Vivo mode right now.")

if __name__ == "__main__":
    print("🖥️ PyCharm Assistant")
    say("Hello, I am Jarvis AI")

    while True:
        query = takeCommand().lower()

        if query == "":
            print("🔄 Empty command received. Listening again...")
            continue

        if "quit" in query or "exit" in query or "stop" in query:
            say("Goodbye! Have a nice day.")
            break

        found = False

        # Play songs
        if query.startswith("play"):
            run_vivo(query)
            found = True

        # Open websites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["instagram", "https://www.instagram.com"],
            ["google", "https://www.google.com"],
            ["whatsapp", "https://www.whatsapp.com"],
            ["facebook", "https://www.facebook.com"],
            ["twitter", "https://www.twitter.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["amazon", "https://www.amazon.in"],
            ["netflix", "https://www.netflix.com"],
            ["github", "https://www.github.com"]
        ]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                print(f"🌐 Opening {site[1]}")
                webbrowser.open(site[1])
                found = True
                break

        # Open local music
        if "open music" in query:
            music_path = r"C:\Users\patel\Music"
            if os.path.exists(music_path):
                say("Opening Music folder")
                print(f"🎵 Opening {music_path}")
                os.startfile(music_path)
            else:
                say("Music folder not found.")
            found = True

        # Time
        if "what is time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strTime}")
            print(f"⏰ The time is {strTime}")
            found = True

        # Date
        if "what is today's date" in query or "today's date" in query or "date" in query:
            today_date = datetime.datetime.now().strftime("%B %d, %Y")
            say(f"Today is {today_date}")
            found = True

        # Wikipedia search
        if "who is" in query:
            person = query.replace("who is", "").strip()
            try:
                info = wikipedia.summary(person, sentences=2)
                say(info)
            except wikipedia.exceptions.DisambiguationError:
                say("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                say("I couldn't find information on that.")
            found = True

        # Open PyCharm
        if "open pycharm" in query:
            pycharm_path = r"C:\Users\Public\Desktop\PyCharm 2025.1.1.1.lnk"
            if os.path.exists(pycharm_path):
                say("Opening PyCharm")
                print(f"🖥️ Opening {pycharm_path}")
                os.startfile(pycharm_path)
            else:
                say("PyCharm not found.")
            found = True

        # Custom Q&A
        qna = {
            "what is your name": "I am Jarvis, your personal assistant.",
            "how are you": "I'm always operational and ready to help you!",
            "where are you from": "I live in your computer, but I was born in the cloud.",
            "who created you": "I was created by Khush using Python and AI technologies.",
            "what can you do": "I can assist you with various tasks like opening websites, playing music, and telling the time.",
            "what is your hobby": "My hobby is learning new things and helping people.",
            "tell me a joke": "Why did the computer show up late to work? Because it had a hard drive!",
            "what is the weather": "Sorry, I don't have weather integration yet. Maybe next update!",
            "who is your favorite superhero": "Iron Man, of course! After all, I'm named after his AI assistant.",
            "what is your passion": "My passion is assisting you and making your life easier!"
        }

        for question, answer in qna.items():
            if question in query:
                say(answer)
                found = True
                break

        # Default response
        if not found:
            say("Sorry, I don't know how to do that yet.")
            print("⚠️ Command not recognized. Try asking something else.")
