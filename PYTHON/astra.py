import speech_recognition as sr#speech recognizer for chatbot
import datetime#for telling time
import pyjokes#for jokes
import pywhatkit#for searching web and playing youtube videos
import pyttsx3#for text to speech
import os #for opening files from os

engine = pyttsx3.init()#voice for chatbot
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[0].id)#male and female voice for chatbot
r = sr.Recognizer()#speech recognizer
def speak(audio):#reply from chatbot
    engine.say(audio)
    engine.runAndWait()

def wishme():#wishing according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:#wishing good morning
        speak("good morning")
    elif hour>=12 and hour<18:#wishing good afternoon
        speak("good afternoon")
    else:
       speak("good evening")#wishing good evening
    speak("I am astra how can i help you")#chatbot introducing itself

wishme()#calling wishme function
def takecmd():#taking command from user


    with sr.Microphone() as source:#using microphone as source
        print("Listening....")#indicating when to speak
        r.pause_threshold = 1# seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)#listening from microphone 

    try:# using try block because if voice will not recognized
        print('recognizing...')
        query = r.recognize_google(audio,language= 'en-US')
        print(f"You said:->{query}")
    except :#try block should have at least 1 except block 
        print("say that again please")
        return "None"
    return query

query = takecmd().lower() #converting command into lowercase 

if 'search' in query :#searching google
    query = query.replace("search","")
    search = pywhatkit.search(query)


elif 'play'in query:#playing youtube videos
    speak("playing")
    pywhatkit.playonyt(query)

elif 'tell me a joke' in query:#telling jokes
    jokes =(pyjokes.get_joke())#getting jokes online
    print(jokes)
    speak(jokes)

elif ' tell time' in query:#telling time
    strTime = datetime.datetime.now().strftime("%H:%M:%S")# string format of time    
    speak(f"the time is {strTime}")

elif 'open code' in query:#code for opening code
    vscode = "C:\\Users\\SIDHARTH MISHRA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(vscode)

elif 'open explorer' in query:#code for opening file explorer
    explorer = "C:\Windows\explorer.exe"
    os.startfile(explorer)


elif 'open word' in query:#code for opening word 
    wordpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
    os.startfile(wordpath)

    

else:#searching google if none of the conditions is executed
    pywhatkit.search(query)


while True:#running infinite loop so that it can take command again and again
    takecmd()