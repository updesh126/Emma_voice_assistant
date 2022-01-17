import speech_recognition as sr
import pyttsx3 #text to speech
import pywhatkit # for whatsapp ,play on youtube ,search on google
import datetime
import wikipedia
import pyjokes
import webbrowser  # run web application
import os #run os application
import sys # for system exit
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from emma import Ui_MainWindow    #importing ui  



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()


#speech recognation take place
def take_command():

    with sr.Microphone() as source:

        print('listening....')
        voice = listener.listen(source, timeout=1,phrase_time_limit= 5)

    try:
        print('Recognizing...')
        command = listener.recognize_google(voice)
        print(command)

    except Exception as e:
        talk('say that again')
        command=take_command()

    return command


#use for wish good morning ,evening e.t.c
def wish():
    # it use for current time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        talk("good morning")

    elif hour>12 and hour<=18:
        talk("good afternoon")

    else:
        talk("good evening")
    talk('I am emma. How can i help you')


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        wish()

        #this is a main function for this assistant
        while True:
            command = take_command().lower()


            #main task start here for assistant
            if "open notepad" in command:
                os.startfile('C:\\WINDOWS\\system32\\notepad.exe')
                talk("opening notepad")

            elif "open cmd" in command:
                os.startfile('cmd')
                talk("opening cmd")
            #"C:\Users\updes\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            
                
            elif "open control panel" in command:
                os.startfile("control")
                talk("opening control panel")
            
            elif "open code" in command:
                os.startfile("code")
                talk("opening VS code")
            
            elif "open this pc" in command:
                os.startfile("explorer")
                talk("opening this pc")
        
            elif "open python" in command:
                os.startfile("python")
                talk("opening python")



            elif "wikipedia" in command:
                talk("Searching wikipedia")
                command = command.replace('wikipedia','')
                result = wikipedia.summary(command, sentences = 3)
                talk("according to wikipedia ")
                print(result)
                talk(result)

            elif"open youtube" in command:
                webbrowser.open("www.youtube.com")
                talk('opening youtube')


            elif 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)

            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is' + time)

            elif 'joke' in command:
                talk(pyjokes.get_joke())

            elif 'i love you' in command:
                talk('I am sorry')

            elif 'what is' in command:
                talk('searching' + command)
                pywhatkit.search(command)



            elif 'repeat after me' in command:
                say = command.replace('repeat after me', 'you say that')
                talk(say)
                print(say)



            elif 'open google' in command:
                talk("what should i search on google for you")
                cm = take_command().lower()
                pywhatkit.search(cm)

            elif 'open hotstar' in command:
                webbrowser.open('www.hotstar.com')
                talk('opening hotstar')

            elif 'open netflix' in command:
                webbrowser.open('www.netflix.com')
                talk('opening Netflix')

            elif 'open prime video' in command:
                webbrowser.open('www.primevideo.com')
                talk('opening prime video')

            elif 'open facebook' in command:
                webbrowser.open('www.facebook.com')
                talk('opening facebook')

            elif 'open instagram' in command:
                webbrowser.open('www.instagram.com')
                talk('opening instagram')

            elif 'open linkedin' in command:
                webbrowser.open('www.linkedin.com')
                talk('opening linkedin')

            elif 'open whatsapp' in command:
                webbrowser.open('web.whatsapp.com')
                talk('opening whatsapp')
            elif 'Download python' in command:
                webbrowser.open('www.python.org')
                talk('opening Python.org')

            elif 'open coursera' in command:
                webbrowser.open('www.coursera.org')
                talk('opening coursera')

            elif 'open udemy' in command:
                webbrowser.open('www.udemy.com')
                talk('opening udemy')

            elif 'news' in command:
                webbrowser.open('https://timesofindia.indiatimes.com')
                talk('opening NEWS')

            elif "no" in command or "nothing" in command or "exit" in command or "Good Bye" in command or "bye" in command :
                talk("thank you,and have a nice day")
                sys.exit()
            talk("do you want something else")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())