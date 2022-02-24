import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('ui/calculator.ui')[0] #ui 불러오기

class CalculratorApp(QMainWindow, form_class):
    def __init__(self): #초기화자
        super().__init__()
        self.setupUi(self) #만들어놓은 signal.ui 연결
        self.setWindowTitle('계산기') # 윈도우 제목 설정
        # self.setWindowIcon(QIcon('img/google_logo.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Calculrator Application Ver 1.0') # 윈도우 상태표시줄 입력
        self.num0button.clicked.connect(self.num0button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num1button.clicked.connect(self.num1button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num2button.clicked.connect(self.num2button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num3button.clicked.connect(self.num3button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num4button.clicked.connect(self.num4button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num5button.clicked.connect(self.num5button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num6button.clicked.connect(self.num6button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num7button.clicked.connect(self.num7button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num8button.clicked.connect(self.num8button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.num9button.clicked.connect(self.num9button_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.addbutton.clicked.connect(self.addbutton_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.subbutton.clicked.connect(self.subbutton_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.mulbutton.clicked.connect(self.mulbutton_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.divbutton.clicked.connect(self.divbutton_clicked)  # 버튼 클릭시 연결될 함수 설정
        self.operbutton.clicked.connect(self.operbutton_clicked)  # 버튼 클릭시 연결될 함수 설정

        self.clearbutton.clicked.connect(self.clear_text)



    def num0button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '0'
        self.mainlabel.setText(ret)

    def num1button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '1'
        self.mainlabel.setText(ret)

    def num2button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '2'
        self.mainlabel.setText(ret)

    def num3button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '3'
        self.mainlabel.setText(ret)

    def num4button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '4'
        self.mainlabel.setText(ret)

    def num5button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '5'
        self.mainlabel.setText(ret)
    def num6button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '6'
        self.mainlabel.setText(ret)
    def num7button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '7'
        self.mainlabel.setText(ret)
    def num8button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '8'
        self.mainlabel.setText(ret)
    def num9button_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '9'
        self.mainlabel.setText(ret)
    def addbutton_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '+'
        self.mainlabel.setText(ret)
    def subbutton_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '-'
        self.mainlabel.setText(ret)
    def mulbutton_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '*'
        self.mainlabel.setText(ret)
    def divbutton_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area + '/'
        self.mainlabel.setText(ret)
    def operbutton_clicked(self):
        input_area = self.mainlabel.text()
        ret = input_area
        result = eval(ret)
        self.mainlabel.setText(str(result))





    def clear_text(self):
        self.mainlabel.clear()



app = QApplication(sys.argv)
window = CalculratorApp()
window.show()
app.exec_()