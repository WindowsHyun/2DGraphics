__author__ = 'Administrator'

import game_framework
from pico2d import *

import main

name = "StartState"
image = None
logo_time = 0.0
gCanvasWidth = 480
gCanvasHeight = 800
gplayX = 600
gtitleY = 800
gscoreX = -150
gexitY = -150
gCount = 0
totalCount = 0
dSpeed = 0.12

def enter():
    global title, gCanvasWidth, gCanvasHeight, font, background, planet, start, score, eexit
    open_canvas(gCanvasWidth, gCanvasHeight)
    print("Open : game_title.py Code")
    font = Font("훈솜사탕R.ttf",40)
    title = load_image('GeneralImage\\Mtitle.png')
    background = load_image('BackgroundImage\\SBT.png')
    planet = load_image('GeneralImage\\planet.png')
    start = load_image('GeneralImage\\Mstart.png')
    score = load_image('GeneralImage\\Mscore.png')
    eexit = load_image('GeneralImage\\Mexits.png')
    pass

def exit():
    global title, font, background, planet, start, score, eexit
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
    global logo_time, gtitleY, gCount, totalCount, gplayX, gscoreX, gexitY, dSpeed
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

    elif totalCount == 1:
        if gplayX <= 240:
            gplayX = 240
            totalCount = 2
            gCount = 0
        else:
            gplayX -= gCount
            gCount += dSpeed

    elif totalCount == 2:
        if gscoreX >= 240:
            gscoreX = 240
            totalCount = 3
            gCount = 0
        else:
            gscoreX += gCount
            gCount += dSpeed

    elif totalCount == 3:
        if gexitY >= 150:
            gexitY = 150
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
    global start, eexit, gtitleY, gbackY, gplayX, gscoreX, gexitY
    clear_canvas()
    background.draw_to_origin(0, 0, gCanvasWidth, gCanvasHeight)
    planet.draw(415, 723)

    title.draw(240, gtitleY)
    start.draw(gplayX, 350)
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
