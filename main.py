__author__ = 'WindowsHyun'

from class_data import *
print("import Class Data py")

import os
os.chdir('C:\\2DGraphics\\2DGraphics\\ResourceData')
print("import OS And Dir Settings")

from pico2d import *
print("import Pico2D")

global gCanvasWidth, gCanvasHeight
gCanvasWidth = 480
gCanvasHeight = 800
gY = 0
gY2 = 800
gFrame = 0
gType = 0
gRunning = True
gLeftTRightF = True
gWhatScenes = "Main"
# Main, Score, GameSelect, Game 이렇게 4개의 장면을 만들예정.
gBackGround = 0
print("Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF, gWhatScenes, gType
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            gRunning = dExits()
        """
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_0:
            gBackGround = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_1:
            gBackGround = 1
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_2:
            gBackGround = 2
        """

        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, gCanvasHeight - event.y
            gWhatScenes = dMenuClick(gWhatScenes, x, y)
            ##################################################
            # 종료할경우 gRunning를 죽인다.
            if gWhatScenes == False:
                gRunning = dExits()
            ##################################################
            pass
        """
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_5:
            gType += 1
            if gType == 12:
                gType = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            gFrame = (gFrame + 1) % 3
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            gLeftTRightF = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            gLeftTRightF = False
        """
    pass

def main():
    global gY, gY2, gFrame, gLeftTRightF, gWhatScenes
    open_canvas(gCanvasWidth, gCanvasHeight)
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

    """
    lFootres = DrawFootrest()
    lRabbit = class_data.cDrawRabbit()
    lRabbit = class_data.cDrawRabbitJet()
    """

    while (gRunning):
        clear_canvas()

        dAutoSlideBG()                              # 이미지 내려주는 함수
        lBackGround.draw(0)                         # 배경 그려주는 함수
        lBackGround.draw(1)                         # 배경 그려주는 함수
        lPlanet.dDraw()                             # 행성 그려주는 함수

        if gWhatScenes == "Main":
            lTitle.dDraw(240,550)                   # Title
            lMenu.dDraw(0,240,400)                  # Start
            lMenu.dDraw(1,240,250)                  # Score
            lMenu.dDraw(2,240,100)                  # Exits

        if gWhatScenes == "GameSelect":
            lTitle.dDraw(240,550)                   # Title
            lMenu.dDraw(3,240,400)                  # Easy
            lMenu.dDraw(4,240,250)                  # Middle
            lMenu.dDraw(5,240,100)                  # Hard
            lBack.dDraw(22,22)                      # Back

        if gWhatScenes == "Score":
            lBack.dDraw(22,22)                      # Back

        """
        lFootres.dDraw(gType,220,650)
        lRabbit.dDraw(gFrame, gLeftTRightF)
        lRabbit.dDraw(gFrame, gLeftTRightF)
        """

        update_canvas()
        handle_events()
        delay(0.015)

    close_canvas()

if __name__ == '__main__':
    main()