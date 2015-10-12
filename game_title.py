__author__ = 'Administrator'

import game_framework
from pico2d import *

import main

name = "StartState"
image = None
logo_time = 0.0
gCanvasWidth = 480
gCanvasHeight = 800
gplayY = 900
gtitleY = 800
gbackY = 800
gplanetX = -70
gscoreX = -150
gexitY = -150
gCount = 0
totalCount = 0

dSpeed = 0.12



def enter():
    global image, title, gCanvasWidth, gCanvasHeight, font, background, planet, start, score, eexit
    open_canvas(gCanvasWidth, gCanvasHeight)
    print("Open : game_title.py Code")
    font = Font("훈솜사탕R.ttf",40)
    image = load_image('GeneralImage\\start_title.png')
    title = load_image('GeneralImage\\Mtitle.png')
    background = load_image('BackgroundImage\\SBT.png')
    planet = load_image('GeneralImage\\planet.png')
    start = load_image('GeneralImage\\Mstart.png')
    score = load_image('GeneralImage\\Mscore.png')
    eexit = load_image('GeneralImage\\Mexits.png')
    pass


def exit():
    global image, title, font, background, planet, start, score, eexit
    del(image)
    del(title)
    del(font)
    del(background)
    del(planet)
    del(start)
    del(score)
    del(eexit)
    print("Unload : game_title.py Code")
    pass


def update():
    global logo_time, gtitleY, gCount, totalCount, gbackY, gplanetX, gplayY, gscoreX, gexitY, dSpeed
    if (logo_time > 9000):
        logo_time = 0
        game_framework.change_state(main)
    #####################################################################
    # 타이틀이 내려온다.
    if totalCount == 0:
        if gtitleY <= 550:
            gtitleY = 550
            gCount = 0
            totalCount = 1
        else:
            gtitleY -= gCount
            gCount += dSpeed
    # 배경화면이 내려온다.
    elif totalCount == 1:
        if gbackY <= 0:
            gbackY = 0
            totalCount = 2
            gCount = 0
        else:
            gbackY -= gCount
            gCount += dSpeed

    elif totalCount == 2:
        if gplanetX >= 415:
            gplanetX = 415
            totalCount = 3
            gCount = 0
        else:
            gplanetX += gCount
            gCount += dSpeed

    elif totalCount == 3:
        if gplayY <= 400:
            gplayY = 400
            totalCount = 4
            gCount = 0
        else:
            gplayY -= gCount
            gCount += dSpeed

    elif totalCount == 4:
        if gscoreX >= 240:
            gscoreX = 240
            totalCount = 5
            gCount = 0
        else:
            gscoreX += gCount
            gCount += dSpeed

    elif totalCount == 5:
        if gexitY >= 100:
            gexitY = 100
            logo_time = 9001
            gCount = 0
        else:
            gexitY += gCount
            gCount += dSpeed

    #####################################################################
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image, background, planet, start, eexit, gtitleY, gbackY, gplanetX, gplayY, gscoreX, gexitY
    clear_canvas()
    image.draw_to_origin(0, 0, gCanvasWidth, gCanvasHeight)
    background.draw_to_origin(0, gbackY, gCanvasWidth, gCanvasHeight)
    planet.draw(gplanetX, 723)
    title.draw(240, gtitleY)
    start.draw(240, gplayY)
    score.draw(gscoreX, 250)
    eexit.draw(240, gexitY)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
    pass


def pause(): pass


def resume(): pass
