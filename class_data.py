__author__ = 'Administrator'

from pico2d import *

import main

class cBackGround:
    def __init__(self):
        self.image = load_image('BackgroundImage\\SBT.png')
        #print("Import Backgroung Data")
    def draw(self, gWhatDraw):
        if gWhatDraw == 0:
            self.image.draw_to_origin(0, main.gY, main.gCanvasWidth, main.gCanvasHeight)
            # draw_to_origin을 사용하면 원본이미지를 그대로 사용 가능하면서 사이즈 크기를 자신이 원하는만큼 조절이 가능하다.
        else:
            self.image.draw_to_origin(0, main.gY2, main.gCanvasWidth, main.gCanvasHeight)
            #drawTwo를 만든이유는 이미지가 내려오는데 중간에 끊겨보이면 안되니깐 자연스럽게 이어지게 만들기 위하여.
    def dChangeBackground(self, gNum):
        if gNum == 0:
            self.image = load_image('BackgroundImage\\SBT.png')
        if gNum == 1:
            self.image = load_image('BackgroundImage\\BSBT.png')
        if gNum == 2:
            self.image = load_image('BackgroundImage\\DBT.png')
    pass

class cDrawPlanet:
    def __init__(self):
        self.image = load_image('GeneralImage\\planet.png')
        self.image.draw(415, 723)
    pass

class cDrawMenu:
    def dDraw(self, WHatMenu, x, y):
        if WHatMenu == "Title":
            self.image = load_image('GeneralImage\\Mtitle.png')
            self.image.draw(x, y)
        if WHatMenu == "Start":
            self.image = load_image('GeneralImage\\Mplay.png')
            self.image.draw(x, y)
        if WHatMenu == "Score":
            self.image = load_image('GeneralImage\\Mscore.png')
            self.image.draw(x, y)
        if WHatMenu == "Exits":
            self.image = load_image('GeneralImage\\Mexits.png')
            self.image.draw(x, y)
        if WHatMenu == "Easy":
            self.image = load_image('GeneralImage\\Measy.png')
            self.image.draw(x, y)
        if WHatMenu == "Middle":
            self.image = load_image('GeneralImage\\Mmedium.png')
            self.image.draw(x, y)
        if WHatMenu == "Hard":
            self.image = load_image('GeneralImage\\Mhard.png')
            self.image.draw(x, y)
        if WHatMenu == "Back":
            self.image = load_image('GeneralImage\\Mback.png')
            self.image.draw(x, y)
            pass

    pass

"""
class cDrawRabbit:
    def dDraw(self, frame, LR):
        if LR == True:
            self.image = load_image('CharacterImage\\Rabbit-Left.png')
        elif LR == False:
            self.image = load_image('CharacterImage\\Rabbit-Right.png')

        self.image.clip_draw(frame * 85, 0, 85, 113, 100, 100)
    pass

class cDrawRabbitJet:
    def dDraw(self, frame, LR):
        if LR == True:
            self.image = load_image('CharacterImage\\Rabbit-Up.png')
        elif LR == False:
            self.image = load_image('CharacterImage\\Rabbit-UpHand.png')

        self.image.clip_draw(frame * 56, 0, 56, 113, 100, 100)
    pass
"""

class cAutoBackGround:
    def __init__(self):
        global gY, gY2
        main.gY -= 3
        main.gY2 -= 3

        if main.gY2 <= 0:
            main.gY = 0
            main.gY2 = 800
    pass