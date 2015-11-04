__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import game_select
#print("- Module game_select -")
import game_score
#print("- Module game_score -")
import game_help
#print("- Module game_score -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0

Game_Running = True
Rabbit_Direction = True


print("main.py : Create Local -> Global function")

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
            if GAME_Scenes == "GameSelect":
                dUpdateMenu("Game_Select")
                game_framework.change_state(game_select)
            if GAME_Scenes == "Game_Score":
                dUpdateMenu("Game_Score")
                game_framework.change_state(game_score)
            if GAME_Scenes == "Game_Help":
                dUpdateMenu("Game_Help")
                game_framework.change_state(game_help)
            ##################################################
            pass
    pass

def enter():
    global GameLoad_BackGround, lMiscPictures, GAME_Scenes
    GAME_Scenes = "Game_Main"
    print("Open : main.py Code")
    GameLoad_BackGround = BackGround()
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
    global GameLoad_BackGround
    global Canvas_Width, Canvas_Height
    clear_canvas()

    GameLoad_BackGround._mainDraw(Background_Y, Canvas_Width, Canvas_Height)
    GameLoad_BackGround._subDraw(BackgroundSub_Y, Canvas_Width, Canvas_Height)

    lMiscPictures.dDraw("planet", 415, 723)
    lMiscPictures.dDraw("title", 240, 550)
    lMiscPictures.dDraw("Start", 240, 350)
    lMiscPictures.dDraw("Score", 240, 250)
    lMiscPictures.dDraw("Exit", 240, 150)
    lMiscPictures.dDraw("Help", 428, 20)

    dFontDraw(3,10, GAME_Scenes, 255, 255, 255)
    #dFontDraw(200,10, "한글 Korea Print -____-", 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global GameLoad_BackGround, lMiscPictures, GAME_Scenes
    del(GameLoad_BackGround)
    del(lMiscPictures)
    print("Unload : main.py Code")
    pass