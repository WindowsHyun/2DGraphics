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
    global gY, gY2, gFrame, gRabbitY, gRabbitX, gRabbitYD, gRabbitR, gLeftTRightF, gtest
#####################################################################################
    # gRabbitYD = 올라가거나 내려가거나를 체크하는 부분
    # gFrame = 캐릭터의 이미지 동작
    # gRabbitY = 캐릭터가 맵화면에 올라가는 좌표
    # gRabbitR = 캐릭터 올라가는 횟수 ( 추후 충돌체크시 초기화를 하여 그 위치부터 다시 올라가게 해야한다. )
    if gRabbitYD == 0:
        gFrame = 2
        gRabbitY += 12
        gRabbitR += 1
    else:
        gFrame = 1
        gRabbitY -= 12
        gRabbitR -= 1
#####################################################################################
    # 실제 캐릭터가 올라간 횟수 최대 10번 올라가면 다시 내리게 하는 부분
    if gRabbitR >= 10 and gRabbitYD == 0:
        gFrame = 1
        gRabbitYD = 1
    elif gRabbitR <= 0 and gRabbitYD == 1:
        gFrame = 1
        gtest = (gtest + 1) % 12
        gRabbitYD = 0
        gRabbitR = 0
#####################################################################################
    if gLeftTRightF == False:
        gRabbitX += 7
    elif gLeftTRightF == True:
        gRabbitX -= 7
        pass
#####################################################################################
    if gRabbitX >= gCanvasWidth:
        gLeftTRightF = False
        gRabbitX = 0
    elif gRabbitX <= 0:
        gLeftTRightF = True
        gRabbitX = gCanvasWidth
#####################################################################################

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
    global lBackGround, lMiscPictures
    del(lBackGround)
    del(lMiscPictures)
    print("Unload : game_ing.py Code")
    pass