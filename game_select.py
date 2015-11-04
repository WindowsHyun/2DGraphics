__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import main
#print("- Module main -")
import game_main
#print("- Module game_main -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0
Game_Running = True
Rabbit_Direction = True


print("game_select.py : Create Local -> Global function")

def handle_events():
    global Game_Running, Rabbit_Frame, Rabbit_Direction, GAME_Scenes
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, Canvas_Height - event.y
            GAME_Scenes = dMenuClick(GAME_Scenes, x, y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            if GAME_Scenes == "Game_Easy":
                dUpdateMenu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Middle":
                dUpdateMenu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Hard":
                dUpdateMenu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Main":
                dUpdateMenu(GAME_Scenes)
                game_framework.change_state(main)
            ##################################################
            pass
    pass

def enter():
    global lBackGround, lMiscPictures, GAME_Scenes
    GAME_Scenes = "Game_Select"
    print("Open : game_select.py Code")
    lBackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    lMiscPictures = DrawMiscPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    dUpdateMenu(GAME_Scenes)
    pass


def update():
    global Background_Y, BackgroundSub_Y
    Background_Y, BackgroundSub_Y = dAutoSlideBG(Background_Y, BackgroundSub_Y)                                                    # 이미지 내려주는 함수
    pass

def draw():
    global lBackGround, lPlanet, lMenu, lTitle, lBack
    global Canvas_Width, Canvas_Height
    clear_canvas()

    lBackGround.draw(Background_Y, BackgroundSub_Y, Canvas_Width, Canvas_Height, 0)                         # 배경 그려주는 함수
    lBackGround.draw(Background_Y, BackgroundSub_Y, Canvas_Width, Canvas_Height, 1)                         # 배경 그려주는 함수
    lMiscPictures.dDraw("planet", 415, 723)
    lMiscPictures.dDraw("title", 240, 550)
    lMiscPictures.dDraw("Easy", 240, 350)
    lMiscPictures.dDraw("Medium", 240, 250)
    lMiscPictures.dDraw("Hard", 240, 150)
    lMiscPictures.dDraw("back", 22, 22)

    dFontDraw(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global lBackGround, lMiscPictures
    del(lBackGround)
    del(lMiscPictures)
    print("Unload : gmae_select.py Code")
    pass