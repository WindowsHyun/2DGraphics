__author__ = 'Administrator'

from main import *

import os
os.chdir('C:\\2DGraphics\\2DGraphics\\ResourceData')
#print("- Module OS And Dir Settings -")

from pico2d import *
#print("- import Pico2D -")

import ctypes  # An included library with Python install.
#print("- Module ctypes -")

class BackGround:
    def __init__(self):
        self.image = load_image('BackgroundImage\\SBT.png')
        #print("BackGround = ",self.image)
    def draw(self,gY, gY2, gCanvasWidth, gCanvasHeight, gWhatDraw):
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

class DrawMiscPictures:
    def __init__(self):
        self.planet = load_image('GeneralImage\\planet.png')
        self.title = load_image('GeneralImage\\Mtitle.png')
        self.back = load_image('GeneralImage\\Mback.png')
        self.easy = load_image('GeneralImage\\Measy.png')
        self.exit = load_image('GeneralImage\\Mexits.png')
        self.hard = load_image('GeneralImage\\Mhard.png')
        self.medium = load_image('GeneralImage\\Mmedium.png')
        self.start = load_image('GeneralImage\\Mstart.png')
        self.score = load_image('GeneralImage\\Mscore.png')
        """
        print("Planet = ",self.planet)
        print("Title = ",self.title)
        print("Back = ",self.back)
        print("Easy = ",self.easy)
        print("Exit = ",self.exit)
        print("Hard = ",self.hard)
        print("Medium = ",self.medium)
        print("Start = ",self.start)
        print("Score = ",self.score)
        """
    def dDraw(self, WhatDraw, x, y):
        if WhatDraw == "planet":
            self.planet.draw(x,y)
        if WhatDraw == "title":
            self.title.draw(x,y)
        if WhatDraw == "back":
            self.back.draw(x,y)
        if WhatDraw == "Easy":
            self.easy.draw(x,y)
        if WhatDraw == "Exit":
            self.exit.draw(x,y)
        if WhatDraw == "Hard":
            self.hard.draw(x,y)
        if WhatDraw == "Medium":
            self.medium.draw(x,y)
        if WhatDraw == "Start":
            self.start.draw(x,y)
        if WhatDraw == "Score":
            self.score.draw(x,y)
    pass


class cDrawRabbit:
    def __init__(self):
        self.leftimage = load_image('CharacterImage\\Rabbit-Left.png')
        self.rightimage = load_image('CharacterImage\\Rabbit-Right.png')

    def dDraw(self, frame, LR, x, y):
        if LR == True:
            self.leftimage.clip_draw(frame * 85, 0, 85, 113, x, y)
        elif LR == False:
            self.rightimage.clip_draw(frame * 85, 0, 85, 113, x, y)
    pass

class cDrawRabbitJet:
    def __init__(self):
        self.upimage = load_image('CharacterImage\\Rabbit-Up.png')
        self.uphandimage = load_image('CharacterImage\\Rabbit-UpHand.png')

    def dDraw(self, frame, LR):
        if LR == True:
            self.upimage.clip_draw(frame * 56, 0, 56, 113, 100, 100)
        elif LR == False:
            self.uphandimage.clip_draw(frame * 56, 0, 56, 113, 100, 100)
    pass

class DrawFootrest:
    def __init__(self):
        self.image = load_image('GeneralImage\\newscaffolding.png')
        #print("Footrst = ", self.image)
    def dDraw(self,WhatNum, x, y):
        self.image.clip_draw(WhatNum * 120, 0, 120, 65, x, y)
    pass


def dMenuClick(WHatMenu, x, y):
    global gWhatScenes, gRunning
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and WHatMenu == "GameSelect":
            WHatMenu = "Easy"
            print("Easy")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "GameSelect":
            WHatMenu = "Middle"
            print("Middle")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and WHatMenu == "GameSelect":
            WHatMenu = "Hard"
            print("Hard")
#400 - 350
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and WHatMenu == "Main":
            WHatMenu = "GameSelect"
            print("Start")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "Main":
            WHatMenu = "Score"
            print("Score")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and WHatMenu == "Main":
            WHatMenu = False
            print("Exits")

    if x >= 4 and x <= 42 and y >= 4 and y <= 42:
        if WHatMenu == "GameSelect" or WHatMenu == "Score":
            WHatMenu = "Main"
            print("Back")
    return WHatMenu
    pass

def dAutoSlideBG(gY, gY2):
    gY -= 3
    gY2 -= 3
    if gY2 <= 0:
        gY = 0
        gY2 = 800
    return gY, gY2
    pass

def dMsgBox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text.encode('euc-kr'), title.encode('euc-kr'), style)

def dFontDraw(x, y, text, r, g, b):
    font = Font("훈솜사탕R.ttf")
    font.draw(x, y, text, (r,g,b))

"""
Styles:
0 : OK
1 : OK | Cancel
2 : Abort | Retry | Ignore
3 : Yes | No | Cancel
4 : Yes | No
5 : Retry | No
6 : Cancel | Try Again | Continue
"""