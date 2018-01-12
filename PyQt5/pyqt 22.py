import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import QWebView, QWebPage

app = QApplication(sys.argv)

browser = QWebView()
browser.load(QUrl("https://www.google.com"))
browser.show()

app.exec_()