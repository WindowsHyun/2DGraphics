__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
#print("- Module random -")
import game_select
#print("- Module main -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0

lRabbit = None
Game_Running = True
Rabbit_Direction = True
Rabbit_Y = 100
Rabbit_X = 100
Rabbit_UpDownDirection = 0
RabbitJump_LimitCount = 0
Rabbit_Jet = False
RabbitJet_Status = False
RabbitJet_Frame = 0
RabbitMaximum_Jump = 10

GameMap_Col = 22
GameMap_Row = 30
Game_Map = [[0 for col in range(GameMap_Col)] for row in range(GameMap_Row)]
for i in range(GameMap_Row): #GameMap_Col==> GameMap_Row
    for j in range(GameMap_Col):  #GameMap_Row==> GameMap_Col
        Game_Map[i][j] = -1
Game_MapCheck = [0 for row in range(GameMap_Row)]
GameCreated_Line = 2


print("gmae-ing.py : Create Local -> Global function")

def handle_events():
    global Game_Running, Rabbit_Frame, Rabbit_Direction, GAME_Scenes
    global Game_Map, Game_MapCheck, GameMap_Col, GameMap_Row, GameCreated_Line, Rabbit_Y, Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            dUpdateMenu("Game_Select")
            Rabbit_Y ,Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount = 100, 100, 0, 0
            Game_Map, Game_MapCheck, GameCreated_Line = dResetMap(GameMap_Col, GameMap_Row, Game_Map, Game_MapCheck)
            game_framework.change_state(game_select)
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, Canvas_Height - event.y
            #GAME_Scenes = dMenuClick(GAME_Scenes, x, y)
            print(x, "-", y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Rabbit_Direction = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Rabbit_Direction = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Rabbit_Jet = True
    pass

def enter():
    global lBackGround, lMiscPictures, GAME_Scenes, lRabbit, lFootrest, lRabbitJet
    GAME_Scenes = dShowMenu()
    print("Open : game_main.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    lRabbit = cDrawRabbit()
    lRabbitJet = cDrawRabbitJet()
    lFootrest = DrawFootrest()
    Game_Map[1][3] = 0
    Game_Map[1][8] = 0
    Game_Map[1][13] = 0
    Game_Map[1][18] = 0
    pass


def update():
    global lRabbit, lRabbitJet, Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount, Rabbit_X, Rabbit_Direction, Canvas_Width, RabbitMaximum_Jump, Rabbit_Jet
    global Game_MapCheck, Game_Map, GameMap_Row, GameCreated_Line, GAME_Scenes
    Rabbit_Frame, Rabbit_Y, RabbitJump_LimitCount = lRabbit.dUpdateRabbitUpDown(Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount)
    Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection = lRabbit.dLimitJump(Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection, RabbitMaximum_Jump)
    Rabbit_X = lRabbit.dRabbitMove(Rabbit_Direction, Rabbit_X)
    Rabbit_X, Rabbit_Direction = lRabbit.dRabbitPass(Rabbit_X, Rabbit_Direction, Canvas_Width)
    GameCreated_Line, Game_MapCheck, Game_Map, RabbitMaximum_Jump = dCreateFootrest(GameMap_Row, GameCreated_Line, Game_MapCheck, Game_Map, GAME_Scenes, RabbitMaximum_Jump)
    Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet, Game_Map = dFootrestCheck(GameMap_Col, GameMap_Row, Rabbit_X, Rabbit_Y, Rabbit_UpDownDirection, RabbitJump_LimitCount, Game_Map, Rabbit_Jet)
    dMapDown()
    dHideFootRest()


    delay(0.015)
    pass

def draw():
    global lBackGround, lMiscPictures, lRabbit, lFootrest, Rabbit_Jet, RabbitJet_Frame
    global Canvas_Width, Canvas_Height, Rabbit_Direction, Rabbit_Frame, Rabbit_X, Rabbit_Y, gtest, Rabbit_UpDownDirection
    global GameMap_Col, GameMap_Row, Game_Map
    clear_canvas()

    lBackGround.draw(Background_Y, BackgroundSub_Y, Canvas_Width, Canvas_Height, 0)                         # 배경 그려주는 함수
    lBackGround.draw(Background_Y, BackgroundSub_Y, Canvas_Width, Canvas_Height, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)

    if ( Rabbit_Jet == False ):
        lRabbit.dDraw(Rabbit_Frame, Rabbit_Direction, Rabbit_X, Rabbit_Y)
    else:
        lRabbitJet.dDraw(2, 0, Rabbit_X, Rabbit_Y)
        dRabbitJet()

    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            lFootrest.dDraw(Game_Map[j][i],(GameMap_Col) * i, GameMap_Row * j)

    dFontDraw(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def dMapDown():
    global Background_Y, BackgroundSub_Y, Rabbit_Y, Canvas_Height, Rabbit_UpDownDirection
    global Game_Map, Game_MapCheck, GameCreated_Line
    if( Rabbit_Y >= Canvas_Height-300):
        for i in range(10):
            Background_Y, BackgroundSub_Y = dAutoSlideBG(Background_Y, BackgroundSub_Y)
        Rabbit_UpDownDirection = 2
        Game_Map, Game_MapCheck, GameCreated_Line = dMapAllDown(Game_Map, Game_MapCheck, GameMap_Col, GameMap_Row, GameCreated_Line)
    if RabbitJump_LimitCount >= RabbitMaximum_Jump:
        Rabbit_UpDownDirection = 1
        pass
    pass

def dHideFootRest():
    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            if ( Game_Map[j][i] == 8 ):
                Game_Map[j][i] = -1
            if ( Game_Map[j][i] == 7 ):
                Game_Map[j][i] = 8
            if ( Game_Map[j][i] == 6 ):
                Game_Map[j][i] = 7
    pass

def dRabbitJet():
    global Rabbit_Jet, RabbitJet_Status, RabbitJet_Frame, Rabbit_Y, Rabbit_UpDownDirection, Rabbit_Frame, RabbitJump_LimitCount
    if ( Rabbit_Jet == True and RabbitJet_Status == False ):
        RabbitJet_Status = True
    elif ( Rabbit_Jet == True and RabbitJet_Status == True ):
        RabbitJet_Frame += 1
        if( Rabbit_Y <= Canvas_Height-300):
            Rabbit_Y += 12
        else:
            Rabbit_Y = Canvas_Height-300
        Rabbit_UpDownDirection = 0
        if ( RabbitJet_Frame >= 100 ):
            Rabbit_UpDownDirection = 1
            RabbitJet_Frame = 0
            RabbitJump_LimitCount = 0
            Rabbit_Frame = 1
            RabbitJet_Status = False
            Rabbit_Jet = False
        pass
    pass


def exit():
    global lBackGround, lMiscPictures, lRabbit, lFootrest
    del(lBackGround)
    del(lMiscPictures)
    del(lRabbit)
    del(lFootrest)
    print("Unload : game_main.py Code")
    pass