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
gBackGround = 0
print("Create Local -> Global function")

def handle_events():
    global gRunning, gBackGround, gFrame, gLeftTRightF
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
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_4:
            gFrame = (gFrame + 1) % 3
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            gLeftTRightF = True
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            gLeftTRightF = False
    pass

def main():
    global gY, gY2, gFrame, gLeftTRightF
    open_canvas(gCanvasWidth, gCanvasHeight)
    lBackGround = class_data.cBackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lAuto = class_data.cAutoBackGround()
    # 클래스 함수를 만들어서 배경화면 내려오게 만들기
    lPlanet = class_data.cDrawPlanet()
    # 클래스 함수를 만들어서 행성이 보이게 만들기

    """
    lRabbit = class_data.cDrawRabbit()
    """

    while (gRunning):
        clear_canvas()

        lAuto.__init__()


        lBackGround.dChangeBackground(gBackGround)

        # 이미지 로드를 바꾸면 클래스 내에서도 여러 이미지를 불러올수있다!

        lBackGround.draw(0)
        lBackGround.draw(1)
        # 해당 클래스에서 이미지 그려주기.
        lPlanet.__init__()
        # 배경 그려주고 난뒤 행성 그려주기.

        """
        lRabbit.dDraw(gFrame, gLeftTRightF)
        """

        update_canvas()
        handle_events()
        delay(0.015)

    close_canvas()

if __name__ == '__main__':
    main()