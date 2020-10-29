import pyshorteners
import os
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QLabel


# os.system("pip3 install pyshorteners")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.root()

    def root(self):
        self.yazi = QLabel("coded by root@ebby:~#\n\nURL Shortener\n\n")
        
        self.url_text = QLabel("Paste the url here  ==>>")
        self.url = QLineEdit("")
        
       
        self.short_text = QLabel("Shortened url here ==>>")
        self.shortened_url = QLineEdit("")

        self.button = QPushButton("Shorten URL")

        
        hbox_url = QHBoxLayout()
        hbox_shortened = QHBoxLayout()
        
        vbox = QVBoxLayout()

        hbox_url.addWidget(self.url_text)
        hbox_url.addWidget(self.url)
        
        hbox_shortened.addWidget(self.short_text)
        hbox_shortened.addWidget(self.shortened_url)

        vbox.addStretch()
        vbox.addWidget(self.yazi)
        vbox.addLayout(hbox_url)
        vbox.addLayout(hbox_shortened)
        vbox.addWidget(self.button)
        vbox.addStretch()



        self.setLayout(vbox)
        self.setFixedHeight(170)
        self.setFixedWidth(600)
        self.button.clicked.connect(self.wave)
        self.setWindowTitle("URL Shortener")
        self.show()


    def wave(self):
        url = self.url.text()
        shorted = pyshorteners.Shortener().tinyurl.short(url)
        self.shortened_url.setText(shorted)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())








"""
url = input("URL (type exit to exit) :  ")
if url == "exit":
    print("Goodbye ! ")
    break

else:
    s = pyshorteners.Shortener().tinyurl.short(url)
    print("Shortened : ", s)
"""		
