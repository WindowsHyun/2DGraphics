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

Rank_Data = []
Score_Data = []
Mode_Data = []
Time_Data = []
Registered_Number = 0

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
    GAME_Scenes = "Game_Score"
    print("Open : game_score.py Code")
    GameLoad_BackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    GameLoad_Menu = MenuPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    GameUpdate_Menu(GAME_Scenes)
    # gamescore_data.score 파일 불러와서 기록하기.
    Score_Init()
    GameScore_Load()
    # 폰트 미리 불러오기.
    GameFont_Title = Font("ResourceData\\훈솜사탕R.ttf",50)
    GameFont_Content = Font("ResourceData\\훈솜사탕R.ttf",30)
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

    GameFont_Title.draw(LoadJson_ScoreData['Title']['x'], LoadJson_ScoreData['Title']['y'], "Game Rankings Score", (255, 255, 255))
    GameFont_Content.draw(LoadJson_ScoreData['Content']['x'], LoadJson_ScoreData['Content']['y'], "Stand        Score       Mode        Time", (0, 0, 0))

    for i in range(0, Registered_Number):
        GameFont_Content.draw(LoadJson_ScoreData['Rank']['x'], LoadJson_ScoreData['Rank']['y']-(i*60), Rank_Data[i] , (255, 255, 255))
        GameFont_Content.draw(LoadJson_ScoreData['Score']['x'], LoadJson_ScoreData['Score']['y']-(i*60), Score_Data[i] , (255, 255, 255))
        GameFont_Content.draw(LoadJson_ScoreData['Time']['x'], LoadJson_ScoreData['Time']['y']-(i*60), Time_Data[i] , (255, 255, 255))
        if(len(Mode_Data[i]) == 6):
            GameFont_Content.draw(LoadJson_ScoreData['Mode_6']['x'], LoadJson_ScoreData['Mode_6']['y']-(i*60), Mode_Data[i] , (255, 255, 255))
        else:
            GameFont_Content.draw(LoadJson_ScoreData['Mode_4']['x'], LoadJson_ScoreData['Mode_4']['y']-(i*60), Mode_Data[i] , (255, 255, 255))

    GameDraw_Font(3,10, GAME_Scenes, 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def exit():
    global GameLoad_BackGround, GameLoad_Menu, GameFont_Title, GameFont_Content
    del(GameLoad_BackGround)
    del(GameLoad_Menu)
    del(GameFont_Title)
    del(GameFont_Content)
    print("Unload : game_score.py Code")
    pass

def Score_Init():
    global Rank_Data, Score_Data, Mode_Data, Time_Data, Registered_Number
    del Rank_Data
    del Score_Data
    del Mode_Data
    del Time_Data
    Rank_Data = []
    Score_Data = []
    Mode_Data = []
    Time_Data = []
    Registered_Number = 0
    pass

def GameScore_Load():
    global Registered_Number
    if (os.path.isfile("gamescore_data.score") == False):
        # 파일이 없을경우 임시로 파일을 만든다.
        f = open("gamescore_data.score", 'wb')
        Default_Data = Base64_Encode("""
<list>/1st/2nd/3rd/4th/5th/6th/7th/8th/9th/10th/</list>
<score>/009999/008888/007777/</score>
<select>/Hard/Medium/Easy/</select>
<time>/00:55:55/00:25:55/00:15:00/</time>
        """)
        f.write(Default_Data)
        f.close()
    else:
        #파일이 있을경우 해당 파일을 불러와서 복호화 시킨다.
        f = open("gamescore_data.score", 'r')
        GameScore_Data = f.read()
        GameScore_Data = Base64_Decode(GameScore_Data)
        ###############################################################################################################
        GameScore_Rank = re.search('\<list\>(.*?)\<\/list\>', GameScore_Data)
        GameScore_Rank = str(GameScore_Rank.group(1))
        for i in range(0, 10):
            Temp_Data = re.search('\/(.*?)\/', GameScore_Rank)
            GameScore_Rank = GameScore_Rank.replace("/" + str(Temp_Data.group(1)),  "")
            Rank_Data.insert(i, Temp_Data.group(1))
        ###############################################################################################################
        GameScore_Score = re.search('\<score\>(.*?)\<\/score\>', GameScore_Data)
        GameScore_Score = str(GameScore_Score.group(1))
        for i in range(0, 10):
            if ( GameScore_Score != "/"):
                Temp_Data = re.search('\/(.*?)\/', GameScore_Score)
                GameScore_Score = GameScore_Score.replace("/" + str(Temp_Data.group(1)),  "")
                Score_Data.insert(i, Temp_Data.group(1))
                Registered_Number += 1
        ###############################################################################################################
        GameScore_Mode = re.search('\<select\>(.*?)\<\/select\>', GameScore_Data)
        GameScore_Mode = str(GameScore_Mode.group(1))
        for i in range(0, 10):
            if ( GameScore_Mode != "/"):
                Temp_Data = re.search('\/(.*?)\/', GameScore_Mode)
                GameScore_Mode = GameScore_Mode.replace("/" + str(Temp_Data.group(1)),  "")
                Mode_Data.insert(i, Temp_Data.group(1))
        ###############################################################################################################
        GameScore_Time = re.search('\<time\>(.*?)\<\/time\>', GameScore_Data)
        GameScore_Time = str(GameScore_Time.group(1))
        for i in range(0, 10):
            if ( GameScore_Time != "/"):
                Temp_Data = re.search('\/(.*?)\/', GameScore_Time)
                GameScore_Time = GameScore_Time.replace("/" + str(Temp_Data.group(1)),  "")
                Time_Data.insert(i, Temp_Data.group(1))
        ###############################################################################################################
        f.close()
    pass