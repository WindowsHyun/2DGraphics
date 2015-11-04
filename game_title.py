__author__ = 'Administrator'

import game_framework
from pico2d import *

import main

image = None
logo_time = 0.0
Canvas_Width = 480
Canvas_Height = 800
GameMenu_PlayX = 600
GameMenu_TitleY = 800
GameMenu_ScoreX = -150
GameMenu_ExitY = -150
GameMenu_AppearsCount = 0
totalCount = 0
GameMenu_AppearsSpeed = 0.12

def enter():
    global title, Canvas_Width, Canvas_Height, font, background, planet, start, score, eexit
    open_canvas(Canvas_Width, Canvas_Height)
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
    global logo_time, GameMenu_TitleY, GameMenu_AppearsCount, totalCount, GameMenu_PlayX, GameMenu_ScoreX, GameMenu_ExitY, GameMenu_AppearsSpeed
    if (logo_time > 9000):
        logo_time = 0
        game_framework.change_state(main)
    #####################################################################
    # 타이틀이 내려온다.
    if totalCount == 0:
        if GameMenu_TitleY <= 550:
            GameMenu_TitleY = 550
            GameMenu_AppearsCount = 0
            totalCount = 1
        else:
            GameMenu_TitleY -= GameMenu_AppearsCount
            GameMenu_AppearsCount += GameMenu_AppearsSpeed

    elif totalCount == 1:
        if GameMenu_PlayX <= 240:
            GameMenu_PlayX = 240
            totalCount = 2
            GameMenu_AppearsCount = 0
        else:
            GameMenu_PlayX -= GameMenu_AppearsCount
            GameMenu_AppearsCount += GameMenu_AppearsSpeed

    elif totalCount == 2:
        if GameMenu_ScoreX >= 240:
            GameMenu_ScoreX = 240
            totalCount = 3
            GameMenu_AppearsCount = 0
        else:
            GameMenu_ScoreX += GameMenu_AppearsCount
            GameMenu_AppearsCount += GameMenu_AppearsSpeed

    elif totalCount == 3:
        if GameMenu_ExitY >= 150:
            GameMenu_ExitY = 150
            logo_time = 9001
            GameMenu_AppearsCount = 0
        else:
            GameMenu_ExitY += GameMenu_AppearsCount
            GameMenu_AppearsCount += GameMenu_AppearsSpeed

    #####################################################################
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    global start, eexit, GameMenu_TitleY, gbackY, GameMenu_PlayX, GameMenu_ScoreX, GameMenu_ExitY
    clear_canvas()
    background.draw_to_origin(0, 0, Canvas_Width, Canvas_Height)

    planet.draw(415, 723)

    title.draw(240, GameMenu_TitleY)
    start.draw(GameMenu_PlayX, 350)
    score.draw(GameMenu_ScoreX, 250)
    eexit.draw(240, GameMenu_ExitY)
    update_canvas()
    pass

def handle_events():
    global logo_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            logo_time = 9001
    pass

def pause(): pass

def resume(): pass
