__author__ = 'WindowsHyun'

import os
print("import OS And Dir Settings")
os.chdir('C:\\2DGraphics\\2DGraphics\\ResourceData\\BackgroundImage')


class cBackGround:
    def __init__(self):
        self.image = load_image('SBT.png')
        print("Import Backgroung Data")
    def draw(self):
        self.image.draw_to_origin(0, 0, gCanvasWidth, gCanvasHeight)
        # draw_to_origin을 사용하면 원본이미지를 그대로 사용 가능하면서 사이즈 크기를 자신이 원하는만큼 조절이 가능하다.
    def dAimage(self):
        self.image = load_image('DBT.png')
        print("Import Backgroung Data")

from pico2d import *
print("import Pico2D")
global gCanvasWidth, gCanvasHeight
gCanvasWidth = 480
gCanvasHeight = 800
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
            print("",SDLK_KP_1)
        if event.type == SDL_KEYDOWN and event.key == SDLK_KP_2:
            gBackGround = 2
            print("",SDLK_KP_2)

    pass

def main():
    open_canvas(gCanvasWidth, gCanvasHeight)
    lBackGround = cBackGround()
    # cBackGround라는 클래스를 lBackGround로 가져오기
    while (gRunning):
        clear_canvas()
        if gBackGround == 1:
            lBackGround.dAimage()
        if gBackGround == 2:
            lBackGround.__init__()
        # 이미지 로드를 바꾸면 클래스 내에서도 여러 이미지를 불러올수있다!
        lBackGround.draw()
        # 해당 클래스에서 이미지 그려주기.
        update_canvas()
        delay(0.05)
        handle_events()

    close_canvas()


if __name__ == '__main__':
    main()