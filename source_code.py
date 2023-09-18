import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

'''
# Printing Both Voices Id To select
print(voices[0].id)
print(voices[1].id)
'''

# Selecting David Voice
engine.setProperty('voice',voices[1].id) 



# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if 0 <= hour < 4:
        speak("Good night! It's quite late, make sure to get some rest.")
    elif 4 <= hour < 12:
        speak("Good morning! Rise and shine!")
    elif 12 <= hour < 16:
        speak("Good afternoon! How's your day going?")
    elif 16 <= hour < 20:
        speak("Good evening! I hope you had a great day.")
    else:
        speak("Good night! It's getting late, time to wind down.")    

def takeCommand(): 
    # It take Microphone input frm user and string output.
    
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold =  1 # if there's a pause of at least 1 second in the speech, the recognizer will consider it the end of the input and process the captured audio.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com', 'your-password')
    server.sendmail('sender_email@gmail.com', to, content)
    server.close()

# creating Speak 
if __name__ == "__main__":
    wishMe()
    speak("Hello Sir, I am Jarvis. How may i help you?")

    while True:
        #query = takeCommand().lower()
        query = "wikipedia one piece"
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com/")

        elif 'open leetcode' in query:
            webbrowser.open("https://leetcode.com/")

        elif 'open hackerearth' in query:
            webbrowser.open("https://hackerearth.com/")

        elif 'open hackerrank' in query:
            webbrowser.open("https://hackerrank.com/")

        elif 'open geekofgeeks' in query:
            webbrowser.open("https://geekofgeeks.com/")

        elif 'open website' in query:
            speak('Sure, please specify the website URL.')
            website_url = input()  # You can use speech recognition to capture the URL as well
            webbrowser.open(website_url)

        elif 'search google for' in query:
            query = query.replace("search Google for", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")


        elif 'open notepad' in query:
            subprocess.Popen(["notepad.exe"])

        elif 'open file explorer' in query:
            subprocess.Popen(["explorer.exe"])

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\Desktop\\Gallery\\Application Setup\\VS code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'what time is it' in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, The current time is {current_time}")

        elif 'search for file' in query:
            speak('Sure, please specify the file name.')
            file_name = input()  # You can use speech recognition to capture the file name as well
            # Add code to search for the file in a specific directory
            # You can use the 'os' module for this task

        elif 'play music' in query:
            music_dir = 'C:\\Users\\DELL\\Music\\Anime_Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'email to aman' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "receiver_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir I am Not able to send the email at the Moment")

        elif 'jarvis quit' in query:
            wishMe()
            break

        break


