__author__ = 'Administrator'

from class_data import *
print("- import Class Data -")
import game_framework
print("- Module game_framework -")
import main
print("- Module main -")

gCanvasWidth = 480
gCanvasHeight = 800
gY = 0
gY2 = 800
gFrame = 0
gType = 0
gRunning = True
gLeftTRightF = True
gBackGround = 0
print("Create Local -> Global function")

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
            if gWhatScenes == "Main":
                game_framework.change_state(main)
            ##################################################
            pass
    pass

def enter():
    global lBackGround, lPlanet, lMenu, lTitle, lBack, gWhatScenes
    dMsgBox('CrageneRabbit', '스코어 기능을 아직 구현하지 못했습니다..!', 0)
    gWhatScenes = "Score"
    print("game_score.py Hello~!!!")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lPlanet = DrawPlanet()
    # 클래스 함수를 만들어서 행성이 보이게 만들기
    lMenu = DrawMenu()
    # 클래스 함수를 만들어서 메뉴 만들기
    lTitle = DrawTitle()
    # 클래스 함수를 만들어서 타이틀 만들기
    lBack = DrawBack()
    # 클래스 함수를 만들어서 뒤로가기 만들기
    pass


def update():
    global gY, gY2
    gY, gY2 = dAutoSlideBG(gY, gY2)                                                    # 이미지 내려주는 함수
    pass

def draw():
    global lBackGround, lPlanet, lBack
    global gCanvasWidth, gCanvasHeight
    clear_canvas()
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 0)                         # 배경 그려주는 함수
    lBackGround.draw(gY, gY2, gCanvasWidth, gCanvasHeight, 1)                         # 배경 그려주는 함수
    lPlanet.dDraw()                                                                   # 행성 그려주는 함수

    lBack.dDraw(22,22)                      # Back

    update_canvas()
    delay(0.015)
    pass

def exit():
    global lBackGround, lPlanet, lBack
    del(lBackGround)
    del(lPlanet)
    del(lBack)
    print("game_score.py Bye~!!!")
    pass