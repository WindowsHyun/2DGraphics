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
gRunning = True
gBackGround = 0
print("Create Local -> Global function")

def handle_events():
    global gRunning
    global gBackGround
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            gRunning = False
            print("Bye Bye~!!!")
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_1:
            gBackGround = 1
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_2:
            gBackGround = 2
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_3:
            gBackGround = 3

    pass

def main():
    global gY, gY2
    open_canvas(gCanvasWidth, gCanvasHeight)
    lBackGround = class_data.cBackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lAuto = class_data.cAutoBackGround()
    # 클래스 함수를 만들어서 배경화면 내려오게 만들기
    lPlanet = class_data.cDrawPlanet()
    # 클래스 함수를 만들어서 행성이 보이게 만들기

    while (gRunning):
        clear_canvas()

        lAuto.__init__()

        if gBackGround == 1:
            lBackGround.dAimage()
        if gBackGround == 2:
            lBackGround.__init__()
        if gBackGround == 3:
            lBackGround.dBimage()
        # 이미지 로드를 바꾸면 클래스 내에서도 여러 이미지를 불러올수있다!

        lBackGround.draw()
        lBackGround.drawTwo()
        # 해당 클래스에서 이미지 그려주기.
        lPlanet.__init__()
        # 배경 그려주고 난뒤 행성 그려주기.

        update_canvas()
        delay(0.05)
        handle_events()

    close_canvas()

if __name__ == '__main__':
    main()