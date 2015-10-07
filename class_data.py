__author__ = 'Administrator'

from main import *

class BackGround:
    def __init__(self):
        self.image = load_image('BackgroundImage\\SBT.png')
        print("BackGround = ",self.image)
    def draw(self, gWhatDraw):
        if gWhatDraw == 0:
            self.image.draw_to_origin(0, gY, gCanvasWidth, gCanvasHeight)
            # draw_to_origin을 사용하면 원본이미지를 그대로 사용 가능하면서 사이즈 크기를 자신이 원하는만큼 조절이 가능하다.
        else:
            self.image.draw_to_origin(0, gY2, gCanvasWidth, gCanvasHeight)
            #drawTwo를 만든이유는 이미지가 내려오는데 중간에 끊겨보이면 안되니깐 자연스럽게 이어지게 만들기 위하여.
    """
    def dChangeBackground(self, gNum):
        if gNum == 0:
            self.image = load_image('BackgroundImage\\SBT.png')
        if gNum == 1:
            self.image = load_image('BackgroundImage\\BSBT.png')
        if gNum == 2:
            self.image = load_image('BackgroundImage\\DBT.png')
    """
    pass

class DrawPlanet:
    def __init__(self):
        self.image = load_image('GeneralImage\\planet.png')
        print("Planet = ",self.image)
    def dDraw(self):
        self.image.draw(415, 723)
    pass

class DrawMenu:
    def dLoad(self, WHatMenu):
        if WHatMenu == "Title":
            self.image = load_image('GeneralImage\\Mtitle.png')
            print("Title = ",self.image)
        if WHatMenu == "Start":
            self.image = load_image('GeneralImage\\Mplay.png')
            print("Start = ",self.image)
        if WHatMenu == "Score":
            self.image = load_image('GeneralImage\\Mscore.png')
            print("Score = ",self.image)
        if WHatMenu == "Exits":
            self.image = load_image('GeneralImage\\Mexits.png')
            print("Exits = ",self.image)
        if WHatMenu == "Easy":
            self.image = load_image('GeneralImage\\Measy.png')
            print("Easy = ",self.image)
        if WHatMenu == "Middle":
            self.image = load_image('GeneralImage\\Mmedium.png')
            print("Middle = ",self.image)
        if WHatMenu == "Hard":
            self.image = load_image('GeneralImage\\Mhard.png')
            print("Hard = ",self.image)
        if WHatMenu == "Back":
            self.image = load_image('GeneralImage\\Mback.png')
            print("Back = ",self.image)
            pass
    def dDraw(self, x, y):
        self.image.draw(x, y)
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

class DrawFootrest:
    def __init__(self):
        self.image = load_image('GeneralImage\\newscaffolding.png')
        print("Footrst = ", self.image)
    def dDraw(self,WhatNum, x, y):
        self.image.clip_draw(WhatNum * 120, 0, 120, 65, x, y)
    pass
"""

def dAutoSlideBG():
    global gY, gY2
    gY -= 3
    gY2 -= 3

    if gY2 <= 0:
        gY = 0
        gY2 = 800
    pass

def dMenuClick(WHatMenu, x, y):
    global gWhatScenes, gRunning
    if x >= 131 and x <= 349 and y >= 363 and y <= 437 and WHatMenu == "GameSelect":
            print("Easy")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "GameSelect":
            print("Middle")
    if x >= 131 and x <= 349 and y >= 63 and y <= 137 and WHatMenu == "GameSelect":
            print("Hard")

    if x >= 131 and x <= 349 and y >= 363 and y <= 437 and WHatMenu == "Main":
            WHatMenu = "GameSelect"
            print("Start")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "Main":
            WHatMenu = "Score"
            print("Score")
    if x >= 131 and x <= 349 and y >= 63 and y <= 137 and WHatMenu == "Main":
            WHatMenu = False
            print("Exits")

    if x >= 4 and x <= 42 and y >= 4 and y <= 42:
        if WHatMenu == "GameSelect" or WHatMenu == "Score":
            WHatMenu = "Main"
        print("Back")
    return WHatMenu
    pass