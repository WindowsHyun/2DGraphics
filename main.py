__author__ = 'WindowsHyun'

import os
os.chdir('c:\\2DGraphics\\2DGraphics')
print("import OS And Dir Setting")

from pico2d import *
isCanvasWidth = 800
isCanvasHeight = 600
isRunning = True
print("import Pico2D And Open Canvas")

def handle_events():
    global isRunning

    events = get_events()

def main():
    open_canvas(isCanvasWidth, isCanvasHeight)

    while isRunning:
        handle_events()
        clear_canvas()
        update_canvas()
        #running = False
        delay(0.08)

    close_canvas()

if __name__ == '__main__':
    main()