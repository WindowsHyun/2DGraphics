__author__ = 'WindowsHyun'

import class_data
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
gRunning = True
gLeftTRightF = True
gWhatScenes = "Main"
# Main, Score, GameSelect, Game 이렇게 4개의 장면을 만들예정.
gBackGround = 0
print("Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF, gWhatScenes
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            gRunning = False
            print("Bye Bye~!!!")
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_0:
            gBackGround = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_1:
            gBackGround = 1
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_2:
            gBackGround = 2

        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, gCanvasHeight - event.y
            if x >= 131 and x <= 349 and y >= 363 and y <= 437 and gWhatScenes == "Main":
                gWhatScenes = "GameSelect"
                print("Start")
            if x >= 131 and x <= 349 and y >= 213 and y <= 287 and gWhatScenes == "Main":
                print("Score")
            if x >= 131 and x <= 349 and y >= 63 and y <= 137 and gWhatScenes == "Main":
                gRunning = False
                print("EXIT")
        """
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
    lBackGround = class_data.cBackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lAuto = class_data.cAutoBackGround()
    # 클래스 함수를 만들어서 배경화면 내려오게 만들기
    lPlanet = class_data.cDrawPlanet()
    # 클래스 함수를 만들어서 행성이 보이게 만들기
    lMenu = class_data.cDrawMenu()
    # 클래스 함수를 만들어서 메뉴 만들기

    """
    lRabbit = class_data.cDrawRabbit()
    lRabbit = class_data.cDrawRabbitJet()
    """

    while (gRunning):
        clear_canvas()

        lAuto.__init__()                            # 이미지 내려주는 함수
        lBackGround.dChangeBackground(gBackGround)  # 이미지 바꿔주는 함수
        lBackGround.draw(0)                         # 배경 그려주는 함수
        lBackGround.draw(1)                         # 배경 그려주는 함수
        lPlanet.__init__()                          # 행성 그려주는 함수

        if gWhatScenes == "Main":
            lMenu.dDraw("Title",240,550)                  # Start
            lMenu.dDraw("Start",240,400)                  # Start
            lMenu.dDraw("Score",240,250)                  # Score
            lMenu.dDraw("Exits",240,100)                  # Exits
            lMenu.dDraw("Back",22,22)                  # Back

        if gWhatScenes == "GameSelect":
            lMenu.dDraw("Title",240,550)                  # Start
            lMenu.dDraw("Easy",240,400)                  # Easy
            lMenu.dDraw("Middle",240,250)                  # Middle
            lMenu.dDraw("Hard",240,100)                  # Hard



        """
        lRabbit.dDraw(gFrame, gLeftTRightF)
        lRabbit.dDraw(gFrame, gLeftTRightF)
        """

        update_canvas()
        handle_events()
        delay(0.015)

    close_canvas()

if __name__ == '__main__':
    main()