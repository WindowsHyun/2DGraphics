__author__ = 'Administrator'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import main
#print("- Module main -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0
Game_Running = True


######################################################
# 토끼 불러오는 함수
Rabbit_Direction = True
Rabbit_Y = 237
Rabbit_X = 417
Rabbit_UpDownDirection = 0
RabbitJump_LimitCount = 0
Rabbit_Jet = False
RabbitJet_Status = False
RabbitJet_Frame = 0
RabbitMaximum_Jump = 10
######################################################
GameMap_Col = 22
GameMap_Row = 30
Game_Map = [[0 for col in range(GameMap_Col)] for row in range(GameMap_Row)]
for i in range(GameMap_Row): #GameMap_Col==> GameMap_Row
    for j in range(GameMap_Col):  #GameMap_Row==> GameMap_Col
        Game_Map[i][j] = -1
Game_MapCheck = [0 for row in range(GameMap_Row)]
GameCreated_Line = 2
######################################################

print("gmae_help.py : Create Local -> Global function")

def handle_events():
    global Game_Running, Rabbit_Frame, Rabbit_Direction, GAME_Scenes
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, Canvas_Height - event.y
            print(x, "-", y)
            GAME_Scenes = dMenuClick(GAME_Scenes, x, y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            if GAME_Scenes == "Game_Main":
                dUpdateMenu(GAME_Scenes)
                game_framework.change_state(main)
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Rabbit_Direction = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Rabbit_Direction = False
    pass

def enter():
    global GameLoad_BackGround, GameLoad_Menu, GAME_Scenes, lRabbit, lFootrest, lRabbitJet, Game_Map
    GAME_Scenes = "Game_Help"
    print("Open : game_help.py Code")
    GameLoad_BackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    GameLoad_Menu = DrawMenuPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    lRabbit = cDrawRabbit()
    lRabbitJet = cDrawRabbitJet()
    lFootrest = DrawFootrest()

    Game_Map[24][4] = 0
    Game_Map[20][4] = 1
    Game_Map[16][4] = 4
    Game_Map[12][4] = 5
    Game_Map[8][4] = 12
    Game_Map[4][4] = 9

    #토끼, 발판 이미지 불러오기
    dUpdateMenu(GAME_Scenes)
    pass


def update():
    global Background_Y, BackgroundSub_Y, lRabbit, lRabbitJet
    global Rabbit_X, Rabbit_Direction, Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet, Game_Map, GameMap_Col, GameMap_Row, Rabbit_Frame, Rabbit_Y, RabbitMaximum_Jump
    Background_Y, BackgroundSub_Y = dAutoSlideBG(Background_Y, BackgroundSub_Y)                                                    # 이미지 내려주는 함수
    Rabbit_Frame, Rabbit_Y, RabbitJump_LimitCount = lRabbit.dUpdateRabbitUpDown(Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount)
    Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection = lRabbit.dLimitJump(Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection, RabbitMaximum_Jump)
    Rabbit_X, Rabbit_Direction = lRabbit.dRabbitPass(Rabbit_X, Rabbit_Direction, Canvas_Width)
    Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet, Game_Map = dFootrestCheck(GameMap_Col, GameMap_Row, Rabbit_X, Rabbit_Y, Rabbit_UpDownDirection, RabbitJump_LimitCount, Game_Map, Rabbit_Jet)
    delay(0.015)
    pass

def draw():
    global GameLoad_BackGround, GameLoad_Menu
    global Canvas_Width, Canvas_Height, Rabbit_Direction, Rabbit_X, Rabbit_Y, Rabbit_Frame
    clear_canvas()

    GameLoad_BackGround._mainDraw(Background_Y, Canvas_Width, Canvas_Height)
    GameLoad_BackGround._subDraw(BackgroundSub_Y, Canvas_Width, Canvas_Height)
    GameLoad_Menu._DrawPlanet(415, 723)
    GameLoad_Menu._DrawBack(22, 22)

    if ( Rabbit_Jet == False ):
        lRabbit.dDraw(Rabbit_Frame, Rabbit_Direction, Rabbit_X, Rabbit_Y)
    else:
        lRabbitJet.dDraw(2, 0, Rabbit_X, Rabbit_Y)
        #dRabbitJet()

    Game_Map[4][19] = 0

    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            lFootrest.dDraw(Game_Map[j][i],(GameMap_Col) * i, GameMap_Row * j)

    GameLoad_Menu._DrawHelp01(285, 720)
    GameLoad_Menu._DrawHelp02(285, 605)
    GameLoad_Menu._DrawHelp03(285, 483)
    GameLoad_Menu._DrawHelp04(285, 360)
    GameLoad_Menu._DrawHelp05(285, 245)
    #GameLoad_Menu.dDraw("Help01", 285, 125)

    dFontDraw(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global GameLoad_BackGround, GameLoad_Menu
    del(GameLoad_BackGround)
    del(GameLoad_Menu)
    print("Unload : game_help.py Code")
    pass