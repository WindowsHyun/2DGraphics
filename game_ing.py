__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")

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

gtest = 0
print("gmae-ing.py : Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF, gWhatScenes, gType
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, gCanvasHeight - event.y
            gWhatScenes = dMenuClick(gWhatScenes, x, y)
            ##################################################
            # 종료할경우 gRunning를 죽인다.
            if gWhatScenes == False:
                game_framework.quit()
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            gLeftTRightF = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            gLeftTRightF = False
    pass

def enter():
    global lBackGround, lMiscPictures, gWhatScenes, lRabbit, lFootrest
    gWhatScenes = "Easy"
    print("Open : game_ing.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    lRabbit = cDrawRabbit()
    lFootrest = DrawFootrest()
    pass


def update():
    global lRabbit, gFrame, gRabbitYD, gRabbitY, gRabbitR, gtest, gRabbitX, gLeftTRightF, gCanvasWidth

    gFrame, gRabbitY, gRabbitR = lRabbit.dUpdateRabbitUpDown(gFrame, gRabbitYD, gRabbitY, gRabbitR)
    gFrame, gRabbitR, gRabbitYD, gtest = lRabbit.dLimitJump(gFrame, gRabbitR, gRabbitYD, gtest)
    gRabbitX = lRabbit.dRabbitMove(gLeftTRightF, gRabbitX)
    gRabbitX, gLeftTRightF = lRabbit.dRabbitPass(gRabbitX, gLeftTRightF, gCanvasWidth)
    delay(0.05)
    pass

def draw():
    global lBackGround, lMiscPictures, lRabbit, lFootrest
    global gCanvasWidth, gCanvasHeight, gLeftTRightF, gFrame, gRabbitX, gRabbitY, gtest
    clear_canvas()

    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 0)                         # 배경 그려주는 함수
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)

    lRabbit.dDraw(gFrame, gLeftTRightF, gRabbitX, gRabbitY)

    lFootrest.dDraw(gtest,55,50)

    lFootrest.dDraw(gtest,182,50)
    lFootrest.dDraw(gtest,298,50)

    lFootrest.dDraw(gtest,425,50)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global lBackGround, lMiscPictures, lRabbit, lFootrest
    del(lBackGround)
    del(lMiscPictures)
    del(lRabbit)
    del(lFootrest)
    print("Unload : game_ing.py Code")
    pass