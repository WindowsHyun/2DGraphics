__author__ = 'Administrator'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import main
#print("- Module main -")

gCanvasWidth = 480
gCanvasHeight = 800
gY = 0
gY2 = 800
gFrame = 0
gType = 0
gRunning = True
gBackGround = 0
nowRMenu = None
######################################################
# 토끼 불러오는 함수
gLeftTRightF = True
gRabbitY = 237
gRabbitX = 417
gRabbitYD = 0
gRabbitR = 0
gRabbitJet = False
gRabbitJetStart = False
gJetFrame = 0
gRabbitLimitJump = 10
######################################################
gCol = 22
gRow = 30
gGameMap = [[0 for col in range(gCol)] for row in range(gRow)]
for i in range(gRow): #gCol==> gRow
    for j in range(gCol):  #gRow==> gCol
        gGameMap[i][j] = -1
gGameMapCheck = [0 for row in range(gRow)]
gRandLine = 2
######################################################

print("gmae_help.py : Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF, gWhatScenes, gType
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, gCanvasHeight - event.y
            print(x, "-", y)
            gWhatScenes = dMenuClick(gWhatScenes, x, y)
            ##################################################
            # 종료할경우 gRunning를 죽인다.
            if gWhatScenes == False:
                game_framework.quit()
            if gWhatScenes == "Game_Main":
                dUpdateMenu(gWhatScenes)
                game_framework.change_state(main)
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            gLeftTRightF = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            gLeftTRightF = False
    pass

def enter():
    global lBackGround, lMiscPictures, gWhatScenes, lRabbit, lFootrest, lRabbitJet, gGameMap
    gWhatScenes = "Game_Help"
    print("Open : game_help.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    lRabbit = cDrawRabbit()
    lRabbitJet = cDrawRabbitJet()
    lFootrest = DrawFootrest()

    gGameMap[24][4] = 0
    gGameMap[20][4] = 1
    gGameMap[16][4] = 4
    gGameMap[12][4] = 5
    gGameMap[8][4] = 12
    gGameMap[4][4] = 9

    #토끼, 발판 이미지 불러오기
    dUpdateMenu(gWhatScenes)
    pass


def update():
    global gY, gY2, lRabbit, lRabbitJet
    global gRabbitX, gLeftTRightF, gRabbitYD, gRabbitR, gRabbitJet, gGameMap, gCol, gRow, gFrame, gRabbitY, gRabbitLimitJump
    gY, gY2 = dAutoSlideBG(gY, gY2)                                                    # 이미지 내려주는 함수
    gFrame, gRabbitY, gRabbitR = lRabbit.dUpdateRabbitUpDown(gFrame, gRabbitYD, gRabbitY, gRabbitR)
    gFrame, gRabbitR, gRabbitYD = lRabbit.dLimitJump(gFrame, gRabbitR, gRabbitYD, gRabbitLimitJump)
    gRabbitX, gLeftTRightF = lRabbit.dRabbitPass(gRabbitX, gLeftTRightF, gCanvasWidth)
    gRabbitYD, gRabbitR, gRabbitJet, gGameMap = dFootrestCheck(gCol, gRow, gRabbitX, gRabbitY, gRabbitYD, gRabbitR, gGameMap, gRabbitJet)
    delay(0.015)
    pass

def draw():
    global lBackGround, lMiscPictures
    global gCanvasWidth, gCanvasHeight, gLeftTRightF, gRabbitX, gRabbitY, gFrame
    clear_canvas()

    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 0)                         # 배경 그려주는 함수
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)
    lMiscPictures.dDraw("back", 22, 22)

    if ( gRabbitJet == False ):
        lRabbit.dDraw(gFrame, gLeftTRightF, gRabbitX, gRabbitY)
    else:
        lRabbitJet.dDraw(2, 0, gRabbitX, gRabbitY)
        #dRabbitJet()

    gGameMap[4][19] = 0

    for i in range(gCol):
        for j in range(gRow):
            lFootrest.dDraw(gGameMap[j][i],(gCol) * i, gRow * j)

    lMiscPictures.dDraw("Help01", 285, 720)
    lMiscPictures.dDraw("Help02", 285, 605)
    lMiscPictures.dDraw("Help03", 285, 483)
    lMiscPictures.dDraw("Help04", 285, 360)
    lMiscPictures.dDraw("Help05", 285, 245)
    #lMiscPictures.dDraw("Help01", 285, 125)

    dFontDraw(3,10, gWhatScenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global lBackGround, lMiscPictures
    del(lBackGround)
    del(lMiscPictures)
    print("Unload : game_help.py Code")
    pass