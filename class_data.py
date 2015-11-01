__author__ = 'Administrator'

from main import *

import os
os.chdir('C:\\2DGraphics\\2DGraphics\\ResourceData')
#print("- Module OS And Dir Settings -")

from pico2d import *
#print("- import Pico2D -")

import ctypes  # An included library with Python install.
#print("- Module ctypes -")

import random
#print("- Module random -")

gNowMenu = "Game_Main"

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
        self.help = load_image('GeneralImage\\Mhelp.png')
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
        if WhatDraw == "Help":
            self.help.draw(x,y)
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

    # gRabbitYD = 올라가거나 내려가거나를 체크하는 부분
    # gFrame = 캐릭터의 이미지 동작
    # gRabbitY = 캐릭터가 맵화면에 올라가는 좌표
    # gRabbitR = 캐릭터 올라가는 횟수 ( 추후 충돌체크시 초기화를 하여 그 위치부터 다시 올라가게 해야한다. )
    def dUpdateRabbitUpDown(self, gFrame, gRabbitYD, gRabbitY, gRabbitR):
        if gRabbitYD == 0:
            gFrame = 2
            gRabbitY += 12
            gRabbitR += 1
        elif gRabbitYD == 1:
            gFrame = 1
            gRabbitY -= 12
            gRabbitR -= 1
        elif gRabbitYD == 2:
            gFrame = 2
            gRabbitR += 1
        return gFrame, gRabbitY, gRabbitR

    # 실제 캐릭터가 올라간 횟수 최대 10번 올라가면 다시 내리게 하는 부분
    def dLimitJump(self, gFrame, gRabbitR, gRabbitYD, gRabbitLimitJump):
        if gRabbitR >= gRabbitLimitJump and gRabbitYD == 0:
            gFrame = 1
            gRabbitYD = 1
        elif gRabbitR <= 0 and gRabbitYD == 1:
            gFrame = 1
            #gRabbitYD = 0
            gRabbitR = 0
        return gFrame, gRabbitR, gRabbitYD

    # 실제 캐릭터가 왼쪽으로 가는지 오른쪽으로 가는지 판단해서 움직여 준다.
    def dRabbitMove(self, gLeftTRightF, gRabbitX):
        if gLeftTRightF == False:
            gRabbitX += 7
        elif gLeftTRightF == True:
            gRabbitX -= 7
        return gRabbitX

    # 실제 캐릭터가 벽을 넘어갔을 경우 반대편으로 다시 나오게 한다.
    def dRabbitPass(self, gRabbitX, gLeftTRightF, gCanvasWidth):
        if gRabbitX >= gCanvasWidth:
            gLeftTRightF = False
            gRabbitX = 0
        elif gRabbitX <= 0:
            gLeftTRightF = True
            gRabbitX = gCanvasWidth
        return gRabbitX, gLeftTRightF
    pass

class cDrawRabbitJet:
    def __init__(self):
        self.upimage = load_image('CharacterImage\\Rabbit-Up.png')
        self.uphandimage = load_image('CharacterImage\\Rabbit-UpHand.png')

    def dDraw(self, frame, LR, x, y):
        if LR == True:
            self.upimage.clip_draw(frame * 56, 0, 56, 113, x, y)
        elif LR == False:
            self.uphandimage.clip_draw(frame * 56, 0, 56, 113, x, y)
    pass

class DrawFootrest:
    def __init__(self):
        self.image = load_image('GeneralImage\\newscaffolding.png')
        self.line = load_image('GeneralImage\\Mback.png')
        #print("Footrst = ", self.image)
    def dDraw(self,WhatNum, x, y):
        self.image.clip_draw(WhatNum * 120, 0, 120, 65, x, y)

    def dLine(self, x, y):
        self.line.draw(x, y)
    pass

def dCreateFootrest(gRow, gRandLine, gGameMapCheck, gGameMap, gWhatScenes, gRabbitLimitJump):
    global gLimitLine, gRandOne, gRandTwo, gWhatFootrest
    if ( gRow - 1 <= gRandLine):
        pass
    else:
        gLimitLine = random.randint(1, 5)
        gRandOne = random.randint(3, 19)
        gWhatFootrest = random.randint(1, 12)
        if ( gWhatFootrest == 2 or gWhatFootrest == 3  or gWhatFootrest == 6 or gWhatFootrest == 7 or gWhatFootrest == 8 or gWhatFootrest == 9 or gWhatFootrest == 10 or gWhatFootrest == 11 ):
            gWhatFootrest = 0
        if ( gWhatFootrest == 12 and random.randint(1, 50) == 2):
            gWhatFootrest = 12
        else:
            if ( gWhatFootrest == 12 ):
                gWhatFootrest = 0
        #print("라인 : ", gRandLine, " 몇개 만들지 : ", gLimitLine, " 어디에 만들지 : ", gRandOne)
        if ( gGameMapCheck[gRandLine] == False):
            if (gLimitLine == 2):
                if( gRandOne <= 19):
                    gGameMap[gRandLine][gRandOne] = gWhatFootrest
                    gGameMap[gRandLine][gRandOne - 5] = gWhatFootrest
                elif(gRandOne >= 3):
                    gGameMap[gRandLine][gRandOne] = gWhatFootrest
                    gGameMap[gRandLine][gRandOne + 5] = gWhatFootrest
                gGameMapCheck[gRandLine] = True
                #2개 였을경우
            else:
                gGameMap[gRandLine][gRandOne] = gWhatFootrest
                gGameMapCheck[gRandLine] = True
                #1개 였을경우
            pass
            if ( gWhatScenes == "Game_Easy"):
                gRandLine += 1
                gRabbitLimitJump = 10
            elif ( gWhatScenes == "Game_Middle"):
                gRandLine += 2
                gRabbitLimitJump = 13
            elif ( gWhatScenes == "Game_Hard"):
                gRandLine += 3
                gRabbitLimitJump = 15
    return gRandLine, gGameMapCheck, gGameMap, gRabbitLimitJump
    pass

def dFootrestCheck(gCol, gRow, gRabbitX, gRabbitY, gRabbitYD, gRabbitR, gGameMap, gRabbitJet ):
    for i in range(gCol):   # 가로
        for j in range(gRow):   # 세로
                if(gGameMap[j][i] != -1 ):
                    if( gRabbitX >= ((i - 3)*20) + 25 and gRabbitX <= ((i - 2)*20) + 110):
                        if( gRabbitY >= ((j - 2)*30) + 46 +30 and gRabbitY <= ((j-1)*30) + 46 + 30 and gRabbitYD == 1):
                            #print("토끼 x 좌표 : ",gRabbitX, "범위 : ", ((i - 3)*20) + 25, "~", ((i - 2)*20) + 110)
                            #print("토끼 y 좌표 : ",gRabbitY, "범위 : ", ((j -2)*30) + 46 + 30, "~", ((j-1)*30) + 46 + 30)
                            gGameMap = dFootRestFade(i, j, gGameMap)
                            if(gGameMap[j][i] == 0 or gGameMap[j][i] == 2 or gGameMap[j][i] == 4 or gGameMap[j][i] == 1 or gGameMap[j][i] == 12 ):
                                gRabbitYD = 0
                                gRabbitR = 0
                            gGameMap = dFootRestHide(i, j, gGameMap)
                            gRabbitJet = dSuperRabbit(i, j, gGameMap, gRabbitJet)
                            gCol, gRow, gGameMap = dFootRestMove(gCol, gRow, gGameMap)
    return gRabbitYD, gRabbitR, gRabbitJet, gGameMap
    pass

def dSuperRabbit(i, j, gGameMap, gRabbitJet):
    if ( gGameMap[j][i] == 12 ):
        gRabbitJet = True
    return gRabbitJet
    pass

def dFootRestHide(i, j, gGameMap):
    if ( gGameMap[j][i] == 1 ):
        gGameMap[j][i] = -1
    return gGameMap
    pass

def dFootRestFade(i, j, gGameMap):
    if ( gGameMap[j][i] == 5 ):
        gGameMap[j][i] = 6
    return gGameMap
    pass

def dFootRestMove(gCol, gRow, gGameMap):
    for i in range(gCol):
        for j in range(gRow):
            if ( gGameMap[j][i] == 4 ):
                if( i >= 3):
                    gGameMap[j][i-1] = gGameMap[j][i]
                    gGameMap[j][i] = -1
                else:
                    gGameMap[j][i] = 13
            if ( gGameMap[j][i] == 13 ):
                if( i <= 19):
                    gGameMap[j][i+1] = gGameMap[j][i]
                    gGameMap[j][i] = -1
                else:
                    gGameMap[j][i] = 4
    return gCol, gRow, gGameMap
    pass

def dResetMap(gCol, gRow, gGameMap, gGameMapCheck ):
    global gRandLine
    for i in range(gCol):   # 가로
        for j in range(gRow):   # 세로
            gGameMap[j][i] = -1
            gGameMapCheck[j] = False
            gRandLine = 2
    return gGameMap, gGameMapCheck, gRandLine
    pass

def dMenuClick(WHatMenu, x, y):
    global gRunning
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and WHatMenu == "Game_Select":
            WHatMenu = "Game_Easy"
            print("Easy")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "Game_Select":
            WHatMenu = "Game_Middle"
            print("Middle")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and WHatMenu == "Game_Select":
            WHatMenu = "Game_Hard"
            print("Hard")
#400 - 350
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and WHatMenu == "Game_Main":
            WHatMenu = "GameSelect"
            print("Start")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and WHatMenu == "Game_Main":
            WHatMenu = "Game_Score"
            print("Score")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and WHatMenu == "Game_Main":
            WHatMenu = False
            print("Exits")
    if x >= 380 and x <= 480 and y >= 0 and y <= 36 and WHatMenu == "Game_Main":
            WHatMenu = "Game_Help"
            print("Help")

    if x >= 4 and x <= 42 and y >= 4 and y <= 42:
        if WHatMenu == "Game_Select" or WHatMenu == "Game_Score" or WHatMenu == "Game_Help":
            WHatMenu = "Game_Main"
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



def dMapAllDown(gGameMap, gGameMapCheck, gCol, gRow, gRandLine):
    for i in range(gCol):
        for j in range(gRow):
            if( i <= gCol and j <= gRow-2):
                gGameMap[j][i] = gGameMap[j+1][i]
                gGameMapCheck[j] = gGameMapCheck[j +1]
            pass
    gGameMapCheck[gRow-1] = False
    gRandLine -= 1
    return gGameMap, gGameMapCheck, gRandLine
    pass

def dMsgBox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text.encode('euc-kr'), title.encode('euc-kr'), style)

def dFontDraw(x, y, text, r, g, b):
    font = Font("훈솜사탕R.ttf")
    if ( text != None):
        font.draw(x, y, text, (r,g,b))

def dShowMenu():
    global gNowMenu
    return gNowMenu

def dUpdateMenu(menu):
    global gNowMenu
    gNowMenu = menu

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