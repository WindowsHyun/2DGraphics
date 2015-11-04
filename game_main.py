__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
#print("- Module random -")
import game_select
#print("- Module main -")

gCanvasWidth = 480
gCanvasHeight = 800
gY = 0
gY2 = 800
gFrame = 0
gType = 0
lRabbit = None
gRunning = True
gLeftTRightF = True
gRabbitY = 100
gRabbitX = 100
gRabbitYD = 0
gRabbitR = 0
gRabbitJet = False
gRabbitJetStart = False
gJetFrame = 0
gRabbitLimitJump = 10

gCol = 22
gRow = 30
gGameMap = [[0 for col in range(gCol)] for row in range(gRow)]
for i in range(gRow): #gCol==> gRow
    for j in range(gCol):  #gRow==> gCol
        gGameMap[i][j] = -1
gGameMapCheck = [0 for row in range(gRow)]
gRandLine = 2

nowRMenu = None
print("gmae-ing.py : Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF, gWhatScenes, gType
    global gGameMap, gGameMapCheck, gCol, gRow, gRandLine, gRabbitY, gRabbitX, gRabbitYD, gRabbitR, gRabbitJet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            dUpdateMenu("Game_Select")
            gRabbitY ,gRabbitX, gRabbitYD, gRabbitR = 100, 100, 0, 0
            gGameMap, gGameMapCheck, gRandLine = dResetMap(gCol, gRow, gGameMap, gGameMapCheck)
            game_framework.change_state(game_select)
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, gCanvasHeight - event.y
            #gWhatScenes = dMenuClick(gWhatScenes, x, y)
            print(x, "-", y)
            ##################################################
            # 종료할경우 gRunning를 죽인다.
            if gWhatScenes == False:
                game_framework.quit()
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            gLeftTRightF = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            gLeftTRightF = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            gRabbitJet = True
    pass

def enter():
    global lBackGround, lMiscPictures, gWhatScenes, lRabbit, lFootrest, lRabbitJet
    gWhatScenes = dShowMenu()
    print("Open : game_main.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    lRabbit = cDrawRabbit()
    lRabbitJet = cDrawRabbitJet()
    lFootrest = DrawFootrest()
    gGameMap[1][3] = 0
    gGameMap[1][8] = 0
    gGameMap[1][13] = 0
    gGameMap[1][18] = 0
    pass


def update():
    global lRabbit, lRabbitJet, gFrame, gRabbitYD, gRabbitY, gRabbitR, gRabbitX, gLeftTRightF, gCanvasWidth, gRabbitLimitJump, gRabbitJet
    global gGameMapCheck, gGameMap, gRow, gRandLine, gWhatScenes
    gFrame, gRabbitY, gRabbitR = lRabbit.dUpdateRabbitUpDown(gFrame, gRabbitYD, gRabbitY, gRabbitR)
    gFrame, gRabbitR, gRabbitYD = lRabbit.dLimitJump(gFrame, gRabbitR, gRabbitYD, gRabbitLimitJump)
    gRabbitX = lRabbit.dRabbitMove(gLeftTRightF, gRabbitX)
    gRabbitX, gLeftTRightF = lRabbit.dRabbitPass(gRabbitX, gLeftTRightF, gCanvasWidth)
    gRandLine, gGameMapCheck, gGameMap, gRabbitLimitJump = dCreateFootrest(gRow, gRandLine, gGameMapCheck, gGameMap, gWhatScenes, gRabbitLimitJump)
    gRabbitYD, gRabbitR, gRabbitJet, gGameMap = dFootrestCheck(gCol, gRow, gRabbitX, gRabbitY, gRabbitYD, gRabbitR, gGameMap, gRabbitJet)
    dMapDown()
    dHideFootRest()


    delay(0.015)
    pass

def draw():
    global lBackGround, lMiscPictures, lRabbit, lFootrest, gRabbitJet, gJetFrame
    global gCanvasWidth, gCanvasHeight, gLeftTRightF, gFrame, gRabbitX, gRabbitY, gtest, gRabbitYD
    global gCol, gRow, gGameMap
    clear_canvas()

    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 0)                         # 배경 그려주는 함수
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)

    if ( gRabbitJet == False ):
        lRabbit.dDraw(gFrame, gLeftTRightF, gRabbitX, gRabbitY)
    else:
        lRabbitJet.dDraw(2, 0, gRabbitX, gRabbitY)
        dRabbitJet()

    for i in range(gCol):
        for j in range(gRow):
            lFootrest.dDraw(gGameMap[j][i],(gCol) * i, gRow * j)

    dFontDraw(3,10, gWhatScenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def dMapDown():
    global gY, gY2, gRabbitY, gCanvasHeight, gRabbitYD
    global gGameMap, gGameMapCheck, gRandLine
    if( gRabbitY >= gCanvasHeight-300):
        for i in range(10):
            gY, gY2 = dAutoSlideBG(gY, gY2)
        gRabbitYD = 2
        gGameMap, gGameMapCheck, gRandLine = dMapAllDown(gGameMap, gGameMapCheck, gCol, gRow, gRandLine)
    if gRabbitR >= gRabbitLimitJump:
        gRabbitYD = 1
        pass
    pass

def dHideFootRest():
    for i in range(gCol):
        for j in range(gRow):
            if ( gGameMap[j][i] == 8 ):
                gGameMap[j][i] = -1
            if ( gGameMap[j][i] == 7 ):
                gGameMap[j][i] = 8
            if ( gGameMap[j][i] == 6 ):
                gGameMap[j][i] = 7
    pass

def dRabbitJet():
    global gRabbitJet, gRabbitJetStart, gJetFrame, gRabbitY, gRabbitYD, gFrame, gRabbitR
    if ( gRabbitJet == True and gRabbitJetStart == False ):
        gRabbitJetStart = True
    elif ( gRabbitJet == True and gRabbitJetStart == True ):
        gJetFrame += 1
        if( gRabbitY <= gCanvasHeight-300):
            gRabbitY += 12
        else:
            gRabbitY = gCanvasHeight-300
        gRabbitYD = 0
        if ( gJetFrame >= 100 ):
            gRabbitYD = 1
            gJetFrame = 0
            gRabbitR = 0
            gFrame = 1
            gRabbitJetStart = False
            gRabbitJet = False
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