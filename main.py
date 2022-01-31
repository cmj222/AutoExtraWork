

# 기본 베이스 임포트
import os
import os.path
import sys
import winsound as sd


# 이미지 인식 기능 임포트
import time

import pyautogui
import pytesseract
from PIL import Image

# ui 관련 임포트
from PyQt5 import QtCore
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import *
from easydict import EasyDict
from win32api import GetSystemMetrics
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


# 옆의 main.ui의 카피 패스로 경로를 따온다.
# 폼클래스를 정의한다. uic에서 ui타입을 로딩한다. 대상은 경로와 같다.
# form_class = uic.loadUiType("./main.ui")[0] 작동했던 원본. 하지만 exe로 전환시 문제됨.
# FileNotFoundError: [Errno 2] No such file or directory: './main.ui'
#uic.loadUi(r'F:\POA_program\main.ui', self)
form_class = uic.loadUiType("F:\\python\\PycharmProjects\\AutoExtraWork\\main.ui")[0]


class WindowClass(QMainWindow, form_class):
    # 윈도우클래스는 q메인윈도우를 상속받아서 폼클래스로 전달할 것이다.

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ##################
        ### 변수선언구간 ###
        ##################

        ####################
        ### 자동실행 함수들 ###
        ####################

        # 첫화면 #
        #self.FileSystem(self.PoaMemo)  # basePath를 받아서 파일탐색기를 띄워라

        ###########################
        ### 버튼 트리거, 반응 구간 ###
        ###########################

        # 테스트 버튼을 누르면 3초 뒤에 화면에서 찾는 이미지를 검색한다.
        self.btnTestStart.clicked.connect(self.TestStart)

        # 자동추가 버튼을 누르면 자동추가모드라는 함수를 시행한다.
        #self.button_addFolder.clicked.connect(self.addMemoFolder)

        # 자동추가모드 화면에서 새로 추가를 누르면 새로추가함수를 시행한다
        #self.Button_addNewImageNText.clicked.connect(self.addNewTextImage)
        #self.Button_useImage_addText.clicked.connect(self.useImage_addText)
        # 보기모드 버튼을 누르면 보기모드라는 함수를 시행한다.
        #self.button_view.clicked.connect(self.viewPage)

    def TestStart(self):
        #time.sleep(5)
        sd.Beep(1000, 500)
        #pyautogui.click('btnLogin.png')
        #pyautogui.click('ERP_icon.png')
        #pyautogui.click('iconFolder.png')

        print("테스트스타트끝. 이제 인풋로그인 시행")
        self.InputLogin()

    def InputLogin(self):

        print("인풋로그인끝. 이제 즐겨찾기클릭 시행")
        self.ClickFavorite()

    def ClickFavorite(self):
        time.sleep(5)
        sd.Beep(1000, 500)
        pyautogui.click('iconFavorite.png')




app = QApplication(sys.argv)
# 앱을 만든다 = 어플리케이션을 실행할.
mainWindow = WindowClass()
# 메인윈도우 실행
mainWindow.show()
# 메인윈도우 보여줌.
app.exec_()
# 위에서 만들고 선언한 앱을 실행
# 이 위로 일종의 무한루프를 선언함. 무한루프 중 조건이 달성되면 시행하고 다시 루프하고...


def print_hi(name):
    print("테스트")


if __name__ == '__main__':
    print_hi('PyCharm')

# 상단의 이미지뷰의 이미지



# 이미지 인식의 베이직
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#A = Image.open('이미지.png')
#result = pytesseract.image_to_string(A, lang='kor')
#result = result.replace(" ","")
#print(result)
