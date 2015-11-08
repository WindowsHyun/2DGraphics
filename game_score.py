__author__ = 'Administrator'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
import main
#print("- Module main -")
import re
#print("- Module re -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0
Game_Running = True
Rabbit_Direction = True
GameScore_Data = None
GameFont_Title = None
GameFont_Contents = None

print("gmae_score.py : Create Local -> Global function")

def handle_events():
    global Game_Running, Rabbit_Frame, Rabbit_Direction, GAME_Scenes
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, Canvas_Height - event.y
            print (x, "-", y)
            GAME_Scenes = GameMenu_Click(GAME_Scenes, x, y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            if GAME_Scenes == "Game_Main":
                GameUpdate_Menu(GAME_Scenes)
                game_framework.change_state(main)
            ##################################################
            pass
    pass

def enter():
    global GameLoad_BackGround, GameLoad_Menu, GAME_Scenes, GameScore_Data
    global GameFont_Title, GameFont_Content
    #Game_MsgBox('CrageneRabbit', '스코어 기능을 아직 구현하지 못했습니다..!', 0)
    GAME_Scenes = "Game_Score"
    print("Open : game_score.py Code")
    GameLoad_BackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    GameLoad_Menu = MenuPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    GameUpdate_Menu(GAME_Scenes)
    # gamescore_data.score 파일 불러와서 기록하기.
    GameScore_Load()
    # 폰트 미리 불러오기.
    GameFont_Title = Font("훈솜사탕R.ttf",50)
    GameFont_Content = Font("훈솜사탕R.ttf",30)
    pass


def update():
    global Background_Y, BackgroundSub_Y
    Background_Y, BackgroundSub_Y = GameMap_Slide(Background_Y, BackgroundSub_Y)                                                    # 이미지 내려주는 함수
    pass

def draw():
    global GameLoad_BackGround, GameLoad_Menu
    global Canvas_Width, Canvas_Height
    clear_canvas()

    GameLoad_BackGround._MainDraw(Background_Y, Canvas_Width, Canvas_Height)
    GameLoad_BackGround._SubDraw(BackgroundSub_Y, Canvas_Width, Canvas_Height)
    GameLoad_Menu._DrawPlanet()
    GameLoad_Menu._DrawBack()

    GameFont_Title.draw(45, 758, "Game Rankings Score", (255, 255, 255))

    GameFont_Content.draw(10,650, "Stand        Score       Mode        Time", (0, 0, 0))

    for i in range(0, 10):
        GameFont_Content.draw(25,600-(i*60), str(i+1) + "st" , (255, 255, 255))

    for i in range(0, 10):
        GameFont_Content.draw(125, 600-(i*60), "009999" , (255, 255, 255))

    for i in range(0, 10):
        if(len(str(i)) == 10):
            GameFont_Content.draw(245, 600-(i*60), "Medium" , (255, 255, 255))
        else:
            GameFont_Content.draw(255, 600-(i*60), "Hard" , (255, 255, 255))

    for i in range(0, 10):
        GameFont_Content.draw(357, 600-(i*60), "00:55:55" , (255, 255, 255))

    #GameDraw_Font(10,600, "1st          999999      Hard      00:55:55", 255, 255, 255, 30)

    #GameDraw_Font(10,550, "2st         000888      Medium  00:25:55", 255, 255, 255, 30)

    GameDraw_Font(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global GameLoad_BackGround, GameLoad_Menu
    del(GameLoad_BackGround)
    del(GameLoad_Menu)
    print("Unload : game_score.py Code")
    pass

def GameScore_Load():
    GameScoreData_Location = "C:\\2DGraphics\\2DGraphics\\gamescore_data.score"
    if (os.path.isfile(GameScoreData_Location) == False):
        # 파일이 없을경우 임시로 파일을 만든다.
        f = open(GameScoreData_Location, 'wb')
        Default_Data = Base64_Encode("""
<score>/009999/008888/007777/</score>
<select>/Hard/Medium/Easy/</select>
<time>/00:55:55/00:25:55/00:15:00/</time>
        """)
        f.write(Default_Data)
        f.close()
    else:
        #파일이 있을경우 해당 파일을 불러와서 복호화 시킨다.
        f = open(GameScoreData_Location, 'r')
        GameScore_Data = f.read()
        GameScore_Data = Base64_Decode(GameScore_Data)

        GameScore_Score = re.search('\<score\>(.*?)\<\/score\>', GameScore_Data)
        print(GameScore_Score.group(1))
        GameScore_Select = re.search('\<select\>(.*?)\<\/select\>', GameScore_Data)
        print(GameScore_Select.group(1))
        GameScore_Time = re.search('\<time\>(.*?)\<\/time\>', GameScore_Data)
        print(GameScore_Time.group(1))

        #print(GameScore_Data)
        print("불러오기")
        f.close()
    pass