# from cProfile import label
from assistantUi import Ui_assistantUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import os
import webbrowser
import main
import sys



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    
    def run(self):
        pass
        # main.wishMe()
        # main.takeCommand()
        

startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_assistantUI()
        self.gui.setupUi(self) 

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        self.gui.pushButton_google.clicked.connect(self.google_app)
        self.gui.pushButton_youtube.clicked.connect(self.youtube_app)
        self.gui.pushButton_facebook.clicked.connect(self.facebook_app)
        self.gui.pushButton_instagram.clicked.connect(self.instagram_app)
        self.gui.pushButton_whatsapp.clicked.connect(self.whatsapp_app)
        # self.gui.pushButton_VS_Code.clicked.connect(self.vs_code_app)
    

    def google_app(self):
        main.speak("Opening Chrome...")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def youtube_app(self):
        main.speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")
    
    def facebook_app(self):
        main.speak("Opening facebook...")
        webbrowser.open("https://www.facebook.com/")

    def instagram_app(self):
        main.speak("Opening Instagram...")
        webbrowser.open("https://www.instagram.com/")

    def whatsapp_app(self):
        main.speak("Opening Whatsapp...")
        webbrowser.open("https://web.whatsapp.com/")


    def startTask(self):

        self.gui.level1 = QtGui.QMovie("material//B.G//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.level1)
        self.gui.level1.start()

        self.gui.level2 = QtGui.QMovie("material//ExtraGui//live.gif")
        self.gui.Gif_2.setMovie(self.gui.level2)
        self.gui.level2.start()

        self.gui.level3 = QtGui.QMovie("material//VoiceReg//__1.gif")
        self.gui.Gif_3.setMovie(self.gui.level3)
        self.gui.level3.start()

        self.gui.level4 = QtGui.QMovie("material//ExtraGui//Earth.gif")
        self.gui.Gif_4.setMovie(self.gui.level4)
        self.gui.level4.start()

        self.gui.level5 = QtGui.QMovie("material//ExtraGui//Code_Template.gif")
        self.gui.Gif_5.setMovie(self.gui.level5)
        self.gui.level5.start()

        self.gui.level6 = QtGui.QMovie("material//ExtraGui//initial.gif")
        self.gui.Gif_6.setMovie(self.gui.level6)
        self.gui.level6.start()

        self.gui.level7 = QtGui.QMovie("material//ExtraGui//B.G_Template_1.gif")
        self.gui.Gif_7.setMovie(self.gui.level7)
        self.gui.level7.start()

        timer =QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :" + time
        label_date = "Date :" +date

        self.gui.text_time_1.setText(label_time)
        self.gui.text_date_1.setText(label_date)

        startExe.start()

    
GuiApp = QApplication(sys.argv)
assistant_Gui = Gui_Start()
assistant_Gui.show()
main.speak("Starting your Assistant.....")
exit(GuiApp.exec_())
# main.speak("Good Bye...")

