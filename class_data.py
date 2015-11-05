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

GAME_CurrentMenu = "Game_Main"
###########################################################################################################################################################################
# 발판 정보들
Nomal_Footrest, Hide_Footrest, Pink_Footrest, Red_Footrest, Move_Footrest, Broke_Footrest, Broke2_Footrest = 0, 1, 2, 3, 4, 5, 6
Broke3_Footrest, Broke4_Footrest, Black_Footrest, Black2_Footrest, Black3_Footrest, Jet_Footrest, Delete_Footrest = 7, 8, 9, 10, 11, 12, -1
Delete2_Footrest = 13
###########################################################################################################################################################################

class BackGround:
    def __init__(self):
        self.image = load_image('BackgroundImage\\SBT.png')

    def _mainDraw(self, Background_Y, Canvas_Width, Canvas_Height):
        self.image.draw_to_origin(0, Background_Y, Canvas_Width, Canvas_Height)

    def _subDraw(self, BackgroundSub_Y, Canvas_Width, Canvas_Height):
        self.image.draw_to_origin(0, BackgroundSub_Y, Canvas_Width, Canvas_Height)
    pass

class MenuPictures:
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
        self.help01 = load_image('GeneralImage\\MfootrestHelp01.png')
        self.help02 = load_image('GeneralImage\\MfootrestHelp02.png')
        self.help03 = load_image('GeneralImage\\MfootrestHelp03.png')
        self.help04 = load_image('GeneralImage\\MfootrestHelp04.png')
        self.help05 = load_image('GeneralImage\\MfootrestHelp05.png')

    def _DrawPlanet(self, x, y):
        self.planet.draw(x,y)

    def _DrawTitle(self, x, y):
        self.title.draw(x,y)

    def _DrawBack(self, x, y):
        self.back.draw(x,y)

    def _DrawEasy(self, x, y):
        self.easy.draw(x,y)

    def _DrawExit(self, x, y):
        self.exit.draw(x,y)

    def _DrawHard(self, x, y):
        self.hard.draw(x,y)

    def _DrawMedium(self, x, y):
        self.medium.draw(x,y)

    def _DrawStart(self, x, y):
        self.start.draw(x,y)

    def _DrawScore(self, x, y):
        self.score.draw(x,y)

    def _DrawHelp(self, x, y):
        self.help.draw(x,y)

    def _DrawHelp01(self, x, y):
        self.help01.draw(x,y)

    def _DrawHelp02(self, x, y):
        self.help02.draw(x,y)

    def _DrawHelp03(self, x, y):
        self.help03.draw(x,y)

    def _DrawHelp04(self, x, y):
        self.help04.draw(x,y)

    def _DrawHelp05(self, x, y):
        self.help05.draw(x,y)
    pass


class Rabbit:
    def __init__(self):
        self.leftimage = load_image('CharacterImage\\Rabbit-Left.png')
        self.rightimage = load_image('CharacterImage\\Rabbit-Right.png')

    def _DrawLeft(self, frame, x, y):
        self.leftimage.clip_draw(frame * 85, 0, 85, 113, x, y)

    def _DrawRight(self, frame, x, y):
        self.rightimage.clip_draw(frame * 85, 0, 85, 113, x, y)

    # Rabbit_UpDownDirection = 올라가거나 내려가거나를 체크하는 부분
    # Rabbit_Frame = 캐릭터의 이미지 동작
    # Rabbit_Y = 캐릭터가 맵화면에 올라가는 좌표
    # RabbitJump_LimitCount = 캐릭터 올라가는 횟수 ( 추후 충돌체크시 초기화를 하여 그 위치부터 다시 올라가게 해야한다. )
    def RabbitMove_UpDown(self, Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount):
        if Rabbit_UpDownDirection == "Up":
            Rabbit_Frame = 2
            Rabbit_Y += 12
            RabbitJump_LimitCount += 1
        elif Rabbit_UpDownDirection == "Down":
            Rabbit_Frame = 1
            Rabbit_Y -= 12
            RabbitJump_LimitCount -= 1
        elif Rabbit_UpDownDirection == "Jet":
            Rabbit_Frame = 2
            RabbitJump_LimitCount += 1
        return Rabbit_Frame, Rabbit_Y, RabbitJump_LimitCount

    # 실제 캐릭터가 올라간 횟수 최대 10번 올라가면 다시 내리게 하는 부분
    def RabbitMove_Jump(self, Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection, RabbitMaximum_Jump):
        if RabbitJump_LimitCount >= RabbitMaximum_Jump and Rabbit_UpDownDirection == "Up":
            Rabbit_Frame = 1
            Rabbit_UpDownDirection = "Down"
        elif RabbitJump_LimitCount <= 0 and Rabbit_UpDownDirection == "Down":
            Rabbit_Frame = 1
            #Rabbit_UpDownDirection = "Up"
            RabbitJump_LimitCount = 0
        return Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection

    # 실제 캐릭터가 왼쪽으로 가는지 오른쪽으로 가는지 판단해서 움직여 준다.
    def Rabbit_LeftRightDirection(self, Rabbit_Direction, Rabbit_X):
        if Rabbit_Direction == "Right":
            Rabbit_X += 7
        elif Rabbit_Direction == "Left":
            Rabbit_X -= 7
        return Rabbit_X

    # 실제 캐릭터가 벽을 넘어갔을 경우 반대편으로 다시 나오게 한다.
    def RabbitWall_Pass(self, Rabbit_X, Rabbit_Direction, Canvas_Width):
        if Rabbit_X >= Canvas_Width:
            Rabbit_Direction = "Right"
            Rabbit_X = 0
        elif Rabbit_X <= 0:
            Rabbit_Direction = "Left"
            Rabbit_X = Canvas_Width
        return Rabbit_X, Rabbit_Direction
    pass

class RabbitJet:
    def __init__(self):
        self.uphandimage = load_image('CharacterImage\\Rabbit-UpHand.png')

    def Draw(self, frame, x, y):
        self.uphandimage.clip_draw(frame * 56, 0, 56, 113, x, y)
    pass

class Footrest:
    def __init__(self):
        self.image = load_image('GeneralImage\\newscaffolding.png')
        #print("Footrst = ", self.image)
    def Draw(self,Footrest_Frame, x, y):
        self.image.clip_draw(Footrest_Frame * 120, 0, 120, 65, x, y)
    pass

def Create_Footrest(GameMap_Row, GameCreated_Line, Game_MapCheck, Game_Map, GAME_Scenes, RabbitMaximum_Jump):
    global GameLine_SomeMake, GameMap_ColLocation, GameMap_Footrest

    if ( GameMap_Row - 1 <= GameCreated_Line):
        pass
    else:
        GameLine_SomeMake = random.randint(1, 5)
        GameMap_ColLocation = random.randint(3, 19)
        GameMap_Footrest = random.randint(1, 12)
        if ( GameMap_Footrest == Pink_Footrest or GameMap_Footrest == Red_Footrest  or GameMap_Footrest == Broke2_Footrest or GameMap_Footrest == Broke3_Footrest
             or GameMap_Footrest == Broke4_Footrest or GameMap_Footrest == Black_Footrest or GameMap_Footrest == Black2_Footrest or GameMap_Footrest == Black3_Footrest ):
            GameMap_Footrest = Nomal_Footrest
        if ( GameMap_Footrest == Jet_Footrest and random.randint(1, 50) == 2):
            GameMap_Footrest = Jet_Footrest
        else:
            if ( GameMap_Footrest == Jet_Footrest ):
                GameMap_Footrest = Nomal_Footrest
        #print("라인 : ", GameCreated_Line, " 몇개 만들지 : ", GameLine_SomeMake, " 어디에 만들지 : ", GameMap_ColLocation)
        if ( Game_MapCheck[GameCreated_Line] == False):
            if (GameLine_SomeMake == 2):
                if( GameMap_ColLocation <= 19):
                    Game_Map[GameCreated_Line][GameMap_ColLocation] = GameMap_Footrest
                    Game_Map[GameCreated_Line][GameMap_ColLocation - 5] = GameMap_Footrest
                elif(GameMap_ColLocation >= 3):
                    Game_Map[GameCreated_Line][GameMap_ColLocation] = GameMap_Footrest
                    Game_Map[GameCreated_Line][GameMap_ColLocation + 5] = GameMap_Footrest
                Game_MapCheck[GameCreated_Line] = True
                #2개 였을경우
            else:
                Game_Map[GameCreated_Line][GameMap_ColLocation] = GameMap_Footrest
                Game_MapCheck[GameCreated_Line] = True
                #1개 였을경우
            pass
            if ( GAME_Scenes == "Game_Easy"):
                GameCreated_Line += 1
                RabbitMaximum_Jump = 10
            elif ( GAME_Scenes == "Game_Middle"):
                GameCreated_Line += 2
                RabbitMaximum_Jump = 13
            elif ( GAME_Scenes == "Game_Hard"):
                GameCreated_Line += 3
                RabbitMaximum_Jump = 15
    return GameCreated_Line, Game_MapCheck, Game_Map, RabbitMaximum_Jump
    pass

def CollisionCheck_Footrest(GameMap_Col, GameMap_Row, Rabbit_X, Rabbit_Y, Rabbit_UpDownDirection, RabbitJump_LimitCount, Game_Map, Rabbit_Jet ):
    for i in range(GameMap_Col):   # 가로
        for j in range(GameMap_Row):   # 세로
                if(Game_Map[j][i] != Delete_Footrest ):
                    if( Rabbit_X >= ((i - 3)*20) + 25 and Rabbit_X <= ((i - 2)*20) + 110):
                        if( Rabbit_Y >= ((j - 2)*30) + 46 +30 and Rabbit_Y <= ((j-1)*30) + 46 + 30 and Rabbit_UpDownDirection == "Down"):
                            #print("토끼 x 좌표 : ",Rabbit_X, "범위 : ", ((i - 3)*20) + 25, "~", ((i - 2)*20) + 110)
                            #print("토끼 y 좌표 : ",Rabbit_Y, "범위 : ", ((j -2)*30) + 46 + 30, "~", ((j-1)*30) + 46 + 30)
                            Game_Map = Footrest_Fade(i, j, Game_Map)
                            if(Game_Map[j][i] == Nomal_Footrest or Game_Map[j][i] == Pink_Footrest or Game_Map[j][i] == Move_Footrest
                               or Game_Map[j][i] == Hide_Footrest or Game_Map[j][i] == Jet_Footrest ):
                                Rabbit_UpDownDirection = "Up"
                                RabbitJump_LimitCount = 0
                            Game_Map = Footrest_Hide(i, j, Game_Map)
                            Rabbit_Jet = RabbitJet_Activate(i, j, Game_Map, Rabbit_Jet)
                            GameMap_Col, GameMap_Row, Game_Map = Footrest_Move(GameMap_Col, GameMap_Row, Game_Map)
    return Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet, Game_Map
    pass

def RabbitJet_Activate(i, j, Game_Map, Rabbit_Jet):
    if ( Game_Map[j][i] == Jet_Footrest ):
        Rabbit_Jet = True
    return Rabbit_Jet
    pass

def Footrest_Hide(i, j, Game_Map):
    if ( Game_Map[j][i] == Hide_Footrest ):
        Game_Map[j][i] = Delete_Footrest
    return Game_Map
    pass

def Footrest_Fade(i, j, Game_Map):
    if ( Game_Map[j][i] == Broke_Footrest ):
        Game_Map[j][i] = Broke2_Footrest
    return Game_Map
    pass

def Footrest_Move(GameMap_Col, GameMap_Row, Game_Map):
    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            if ( Game_Map[j][i] == Move_Footrest ):
                if( i >= 3):
                    Game_Map[j][i-1] = Game_Map[j][i]
                    Game_Map[j][i] = Delete_Footrest
                else:
                    Game_Map[j][i] = Delete2_Footrest
            if ( Game_Map[j][i] == Delete2_Footrest ):
                if( i <= 19):
                    Game_Map[j][i+1] = Game_Map[j][i]
                    Game_Map[j][i] = Delete_Footrest
                else:
                    Game_Map[j][i] = Move_Footrest
    return GameMap_Col, GameMap_Row, Game_Map
    pass

def GameMap_Reset(GameMap_Col, GameMap_Row, Game_Map, Game_MapCheck ):
    global GameCreated_Line
    for i in range(GameMap_Col):   # 가로
        for j in range(GameMap_Row):   # 세로
            Game_Map[j][i] = Delete_Footrest
            Game_MapCheck[j] = False
            GameCreated_Line = 2
    return Game_Map, Game_MapCheck, GameCreated_Line
    pass

def GameMenu_Click(GAME_Menu, x, y):
    global Game_Running
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and GAME_Menu == "Game_Select":
            GAME_Menu = "Game_Easy"
            print("Easy")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and GAME_Menu == "Game_Select":
            GAME_Menu = "Game_Middle"
            print("Middle")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and GAME_Menu == "Game_Select":
            GAME_Menu = "Game_Hard"
            print("Hard")
#400 - 350
    if x >= 131 and x <= 349 and y >= 313 and y <= 387 and GAME_Menu == "Game_Main":
            GAME_Menu = "GameSelect"
            print("Start")
    if x >= 131 and x <= 349 and y >= 213 and y <= 287 and GAME_Menu == "Game_Main":
            GAME_Menu = "Game_Score"
            print("Score")
    if x >= 131 and x <= 349 and y >= 113 and y <= 187 and GAME_Menu == "Game_Main":
            GAME_Menu = False
            print("Exits")
    if x >= 380 and x <= 480 and y >= 0 and y <= 36 and GAME_Menu == "Game_Main":
            GAME_Menu = "Game_Help"
            print("Help")

    if x >= 4 and x <= 42 and y >= 4 and y <= 42:
        if GAME_Menu == "Game_Select" or GAME_Menu == "Game_Score" or GAME_Menu == "Game_Help":
            GAME_Menu = "Game_Main"
            print("Back")
    return GAME_Menu
    pass

def GameMap_Slide(Background_Y, BackgroundSub_Y):
    Background_Y -= 3
    BackgroundSub_Y -= 3
    if BackgroundSub_Y <= 0:
        Background_Y = 0
        BackgroundSub_Y = 800
    return Background_Y, BackgroundSub_Y
    pass



def GameMap_Renewal(Game_Map, Game_MapCheck, GameMap_Col, GameMap_Row, GameCreated_Line):
    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            if( i <= GameMap_Col and j <= GameMap_Row-2):
                Game_Map[j][i] = Game_Map[j+1][i]
                Game_MapCheck[j] = Game_MapCheck[j +1]
            pass
    Game_MapCheck[GameMap_Row-1] = False
    GameCreated_Line -= 1
    return Game_Map, Game_MapCheck, GameCreated_Line
    pass

def Game_MsgBox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text.encode('euc-kr'), title.encode('euc-kr'), style)

def GameDraw_Font(x, y, text, r, g, b):
    font = Font("훈솜사탕R.ttf")
    if ( text != None):
        font.draw(x, y, text, (r,g,b))

def GameShow_Menu():
    global GAME_CurrentMenu
    return GAME_CurrentMenu

def GameUpdate_Menu(menu):
    global GAME_CurrentMenu
    GAME_CurrentMenu = menu

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