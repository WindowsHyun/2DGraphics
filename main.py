__author__ = 'WindowsHyun'

import os
os.chdir('c:\\2DGraphics\\2DGraphics')
print("import OS And Dir Setting")

from pico2d import *
print("import Pico2D")
global gCanvasWidth, gCanvasHeight
gCanvasWidth = 480
gCanvasHeight = 800
gRunning = True
print("Create Local -> Global function")

def handle_events():
    global gRunning
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            gRunning = False
            print("Bye Bye~!!!")

    pass

def main():
    open_canvas(gCanvasWidth, gCanvasHeight)

    while (gRunning):
        clear_canvas()
        update_canvas()
        delay(0.05)
        handle_events()

    close_canvas()


if __name__ == '__main__':
    main()