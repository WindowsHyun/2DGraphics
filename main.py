__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import game_select
#print("- Module game_select -")
import game_score
#print("- Module game_score -")
import game_help
#print("- Module game_score -")

gCanvasWidth = 480
gCanvasHeight = 800
gY = 0
gY2 = 800
gFrame = 0
gType = 0
gRunning = True
gLeftTRightF = True
gBackGround = 0
nowRMenu = None
print("main.py : Create Local -> Global function")

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
            if gWhatScenes == "GameSelect":
                dUpdateMenu("Game_Select")
                game_framework.change_state(game_select)
            if gWhatScenes == "Game_Score":
                dUpdateMenu("Game_Score")
                game_framework.change_state(game_score)
            if gWhatScenes == "Game_Help":
                dUpdateMenu("Game_Help")
                game_framework.change_state(game_help)
            ##################################################
            pass
    pass

def enter():
    global lBackGround, lMiscPictures, gWhatScenes
    gWhatScenes = "Game_Main"
    print("Open : main.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    dUpdateMenu(gWhatScenes)
    pass


def update():
    global gY, gY2
    gY, gY2 = dAutoSlideBG(gY, gY2)                                                    # 이미지 내려주는 함수
    pass

def draw():
    global lBackGround
    global gCanvasWidth, gCanvasHeight
    clear_canvas()

    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 0)                         # 배경 그려주는 함수
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)
    lMiscPictures.dDraw("title", 240, 550)
    lMiscPictures.dDraw("Start", 240, 350)
    lMiscPictures.dDraw("Score", 240, 250)
    lMiscPictures.dDraw("Exit", 240, 150)
    lMiscPictures.dDraw("Help", 428, 20)

    dFontDraw(3,10, gWhatScenes, 255, 255, 255)
    #dFontDraw(200,10, "한글 Korea Print -____-", 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global lBackGround, lMiscPictures, gWhatScenes
    del(lBackGround)
    del(lMiscPictures)
    print("Unload : main.py Code")
    pass