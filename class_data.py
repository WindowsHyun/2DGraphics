__author__ = 'Administrator'

from pico2d import *

import main

class cBackGround:
    def __init__(self):
        self.image = load_image('BackgroundImage\\SBT.png')
        #print("Import Backgroung Data")
    def draw(self):
        self.image.draw_to_origin(0, main.gY, main.gCanvasWidth, main.gCanvasHeight)
        # draw_to_origin을 사용하면 원본이미지를 그대로 사용 가능하면서 사이즈 크기를 자신이 원하는만큼 조절이 가능하다.
    def drawTwo(self):
        self.image.draw_to_origin(0, main.gY2, main.gCanvasWidth, main.gCanvasHeight)
        #drawTwo를 만든이유는 이미지가 내려오는데 중간에 끊겨보이면 안되니깐 자연스럽게 이어지게 만들기 위하여.
    def dAimage(self):
        self.image = load_image('BackgroundImage\\DBT.png')
    def dBimage(self):
        self.image = load_image('BackgroundImage\\BSBT.png')
    pass

class cDrawPlanet:
    def __init__(self):
        self.image = load_image('GeneralImage\\planet.png')
        self.image.draw(414, 723)
    pass

class cAutoBackGround:
    def __init__(self):
        global gY, gY2
        main.gY -= 3
        main.gY2 -= 3

        if main.gY2 <= 0:
            main.gY = 0
            main.gY2 = 800
    pass