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
            GAME_Scenes = GameMenu_Click(GAME_Scenes, x, y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            if GAME_Scenes == "Game_Easy":
                GameUpdate_Menu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Middle":
                GameUpdate_Menu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Hard":
                GameUpdate_Menu(GAME_Scenes)
                game_framework.change_state(game_main)
            if GAME_Scenes == "Game_Main":
                GameUpdate_Menu(GAME_Scenes)
                game_framework.change_state(main)
            ##################################################
            pass
    pass

def enter():
    global GameLoad_BackGround, GameLoad_Menu, GAME_Scenes
    GAME_Scenes = "Game_Select"
    print("Open : game_select.py Code")
    GameLoad_BackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    GameLoad_Menu = MenuPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    GameUpdate_Menu(GAME_Scenes)
    pass


def update():
    global Background_Y, BackgroundSub_Y
    Background_Y, BackgroundSub_Y = GameMap_Slide(Background_Y, BackgroundSub_Y)                                                    # 이미지 내려주는 함수
    pass

def draw():
    global GameLoad_BackGround, lPlanet, lMenu, lTitle, lBack
    global Canvas_Width, Canvas_Height
    clear_canvas()

    GameLoad_BackGround._mainDraw(Background_Y, Canvas_Width, Canvas_Height)
    GameLoad_BackGround._subDraw(BackgroundSub_Y, Canvas_Width, Canvas_Height)
    GameLoad_Menu._DrawPlanet(415, 723)
    GameLoad_Menu._DrawTitle(240, 550)
    GameLoad_Menu._DrawEasy(240, 350)
    GameLoad_Menu._DrawMedium(240, 250)
    GameLoad_Menu._DrawHard(240, 150)
    GameLoad_Menu._DrawBack(22, 22)

    GameDraw_Font(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global GameLoad_BackGround, GameLoad_Menu
    del(GameLoad_BackGround)
    del(GameLoad_Menu)
    print("Unload : gmae_select.py Code")
    pass