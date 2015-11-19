__author__ = 'WindowsHyun'

from class_data import *
#print("- import Class Data -")
import game_framework
#print("- Module game_framework -")
#print("- Module random -")
import game_select
#print("- Module main -")
import game_over
#print("- Module main -")

Canvas_Width = 480
Canvas_Height = 800
Background_Y = 0
BackgroundSub_Y = 800
Rabbit_Frame = 0

Load_Rabbit = None
Game_Running = True
Rabbit_Direction = "Left"
Rabbit_Y = 100
Rabbit_X = 100
Rabbit_UpDownDirection = "Up"
RabbitJump_LimitCount = 0
Rabbit_Jet = False
RabbitJet_Status = False
RabbitJet_Frame = 0
RabbitMaximum_Jump = 10

GameStart_Time = 0
GameEnd_Time = 0
DrawTime_Data = None
Game_Score = 0
LevelUpShow_Count = 0

GameOver_Sound = None
Stage_Sound = None

GameMap_Col = 22
GameMap_Row = 30
Game_Map = [[0 for col in range(GameMap_Col)] for row in range(GameMap_Row)]
for i in range(GameMap_Row): #GameMap_Col==> GameMap_Row
    for j in range(GameMap_Col):  #GameMap_Row==> GameMap_Col
        Game_Map[i][j] = -1
Game_MapCheck = [0 for row in range(GameMap_Row)]
GameCreated_Line = 2


print("gmae-ing.py : Create Local -> Global function")

def handle_events():
    global Game_Running, Rabbit_Frame, Rabbit_Direction, GAME_Scenes
    global Game_Map, Game_MapCheck, GameMap_Col, GameMap_Row, GameCreated_Line, Rabbit_Y, Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 종료버튼을 누르거나 or 키보드의 ESC 키를 누를경우 종료를 한다.
            """
            GameUpdate_Menu("Game_Select")
            Rabbit_Y ,Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount = 100, 100, "Up", 0
            Game_Map, Game_MapCheck, GameCreated_Line = GameMap_Reset(GameMap_Col, GameMap_Row, Game_Map, Game_MapCheck)
            game_framework.change_state(game_select)
            """
            Rabbit_Y = 0
            Game_Over()
            print("Game_Over")
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, Canvas_Height - event.y
            #GAME_Scenes = GameMenu_Click(GAME_Scenes, x, y)
            print(x, "-", y)
            ##################################################
            # 종료할경우 Game_Running를 죽인다.
            if GAME_Scenes == False:
                game_framework.quit()
            ##################################################
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Rabbit_Direction = "Left"
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Rabbit_Direction = "Right"
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Rabbit_Jet = True
    pass

def enter():
    global GameLoad_BackGround, GameLoad_Menu, GAME_Scenes, Load_Rabbit, Load_Footrest, Load_RabbitJet, Score_Board
    global GameStart_Time, GameEnd_Time, DrawTime_Data, Game_Score, Current_Time
    global GameOver_Sound, Stage_Sound
    GAME_Scenes = GameShow_Menu()
    print("Open : game_main.py Code")
    GameLoad_BackGround = BackGround()
    # cBackGround라는 클래스를 BackGround로 가져오기
    GameLoad_Menu = MenuPictures()
    # 클래스 함수를 만들어서 여러가지 이미지 불러오기
    Score_Board = GameScore_Board()
    #
    Load_Rabbit = Rabbit()
    Load_RabbitJet = RabbitJet()
    Load_Footrest = Footrest()
    Game_Map[1][3] = Nomal_Footrest
    Game_Map[1][8] = Nomal_Footrest
    Game_Map[1][13] = Nomal_Footrest
    Game_Map[1][18] = Nomal_Footrest
    GameStart_Time = 0
    GameEnd_Time = 0
    Game_Score = 0
    DrawTime_Data = None
    GameStart_Time = time.time()
    Current_Time = get_time()
    if GameOver_Sound == None:
        GameOver_Sound = load_wav('ResourceData\\SoundData\\GameOver.wav')
        GameOver_Sound.set_volume(100)
    if Stage_Sound == None:
        Stage_Sound = load_wav('ResourceData\\SoundData\\Stage.ogg')
        Stage_Sound.set_volume(100)
    Stage_Sound.repeat_play()
    pass


def update():
    global Load_Rabbit, Load_RabbitJet, Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount, Rabbit_X, Rabbit_Direction, Canvas_Width, RabbitMaximum_Jump, Rabbit_Jet
    global Game_MapCheck, Game_Map, GameMap_Row, GameCreated_Line, GAME_Scenes, Game_Score, Current_Time, Frame_Time
    global Level_Update, LevelUpShow_Count
    Frame_Time = get_time() - Current_Time
    Rabbit_Frame, Rabbit_Y, RabbitJump_LimitCount = Load_Rabbit.RabbitMove_UpDown(Rabbit_Frame, Rabbit_UpDownDirection, Rabbit_Y, RabbitJump_LimitCount, Frame_Time)
    Frame_Time = get_time() - Current_Time
    Rabbit_X = Load_Rabbit.Rabbit_LeftRightDirection(Rabbit_Direction, Rabbit_X, Frame_Time)
    Current_Time += Frame_Time

    Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection = Load_Rabbit.RabbitMove_Jump(Rabbit_Frame, RabbitJump_LimitCount, Rabbit_UpDownDirection, RabbitMaximum_Jump)
    Rabbit_X, Rabbit_Direction = Load_Rabbit.RabbitWall_Pass(Rabbit_X, Rabbit_Direction, Canvas_Width)
    GameCreated_Line, Game_MapCheck, Game_Map, RabbitMaximum_Jump, Level_Update = Create_Footrest(GameMap_Row, GameCreated_Line, Game_MapCheck, Game_Map, GAME_Scenes, RabbitMaximum_Jump, int(Game_Score))
    Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet, Game_Map, Game_Score = CollisionCheck_Footrest(GameMap_Col, GameMap_Row, Rabbit_X, Rabbit_Y, Rabbit_UpDownDirection, RabbitJump_LimitCount, Game_Map, Rabbit_Jet, int(Game_Score))
    GameMap_Down(Frame_Time)
    GameFootrest_Hide()
    GamesIn_Progress()
    GamesDraw_Score()
    Game_Over()

    if Level_Update == "Up":
        LevelUpShow_Count = -5

    delay(0.015)
    pass

def draw():
    global GameLoad_BackGround, GameLoad_Menu, Load_Rabbit, Load_Footrest, Rabbit_Jet, RabbitJet_Frame
    global Canvas_Width, Canvas_Height, Rabbit_Direction, Rabbit_Frame, Rabbit_X, Rabbit_Y, gtest, Rabbit_UpDownDirection
    global GameMap_Col, GameMap_Row, Game_Map
    global GameEnd_Time, GameStart_Time, Current_Time
    global Level_Update, LevelUpShow_Count
    clear_canvas()
    GameLoad_BackGround._MainDraw(Background_Y, Canvas_Width, Canvas_Height)
    GameLoad_BackGround._SubDraw(BackgroundSub_Y, Canvas_Width, Canvas_Height)
    GameLoad_Menu._DrawPlanet()

    if ( Rabbit_Jet == False ):
        if (Rabbit_Direction == "Left" ):
                Load_Rabbit._DrawLeft(Rabbit_Frame, Rabbit_X, Rabbit_Y)
        elif (Rabbit_Direction == "Right" ):
                Load_Rabbit._DrawRight(Rabbit_Frame, Rabbit_X, Rabbit_Y)
    else:
        Load_RabbitJet.Draw(2,Rabbit_X, Rabbit_Y)
        GameRabbit_Jet()

    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            Load_Footrest.Draw(Game_Map[j][i],(GameMap_Col) * i, GameMap_Row * j)

    if LevelUpShow_Count <= 0:
        GameLoad_Menu._DrawLevelUP()
        LevelUpShow_Count += 1
        pass

    Score_Board._Draw(0, Canvas_Width)
    GameDraw_Font(3,10, GAME_Scenes, 255, 255, 255)
    GameDraw_Font(355,10, DrawTime_Data , 255, 255, 255)
    GameDraw_Font(175,10, "Score : " + str(Game_Score) , 255, 255, 255)

    update_canvas()
    delay(0.015)
    pass

def GameMap_Down(Frame_Time):
    global Background_Y, BackgroundSub_Y, Rabbit_Y, Canvas_Height, Rabbit_UpDownDirection
    global Game_Map, Game_MapCheck, GameCreated_Line, Game_Score
    if( Rabbit_Y >= Canvas_Height-300):

        Rabbit_UpDownDirection = "Jet"
        Background_Y, BackgroundSub_Y = GameMap_Slide(Background_Y, BackgroundSub_Y, Frame_Time, Rabbit_Jet)

        if ( GAME_Scenes == "Game_Easy"):
            Game_Score += 1
        elif ( GAME_Scenes == "Game_Middle"):
            Game_Score += 2
        elif ( GAME_Scenes == "Game_Hard"):
            Game_Score += 3
        Game_Map, Game_MapCheck, GameCreated_Line = GameMap_Renewal(Game_Map, Game_MapCheck, GameMap_Col, GameMap_Row, GameCreated_Line)
    if RabbitJump_LimitCount >= RabbitMaximum_Jump:
        Rabbit_UpDownDirection = "Down"
        pass
    pass

def GameFootrest_Hide():
    for i in range(GameMap_Col):
        for j in range(GameMap_Row):
            if ( Game_Map[j][i] == Broke4_Footrest ):
                Game_Map[j][i] = Delete_Footrest
            if ( Game_Map[j][i] == Broke3_Footrest ):
                Game_Map[j][i] = Broke4_Footrest
            if ( Game_Map[j][i] == Broke2_Footrest ):
                Game_Map[j][i] = Broke3_Footrest
    pass

def GameRabbit_Jet():
    global Rabbit_Jet, RabbitJet_Status, RabbitJet_Frame, Rabbit_Y, Rabbit_UpDownDirection, Rabbit_Frame, RabbitJump_LimitCount
    if ( Rabbit_Jet == True and RabbitJet_Status == False ):
        RabbitJet_Status = True
    elif ( Rabbit_Jet == True and RabbitJet_Status == True ):
        RabbitJet_Frame += 1
        if( Rabbit_Y <= Canvas_Height-300):
            Rabbit_Y += 12
        else:
            Rabbit_Y = Canvas_Height-300
        Rabbit_UpDownDirection = "Up"
        if ( RabbitJet_Frame >= 150 ):
            Rabbit_UpDownDirection = "Down"
            RabbitJet_Frame = 0
            RabbitJump_LimitCount = 0
            Rabbit_Frame = 1
            RabbitJet_Status = False
            Rabbit_Jet = False
        pass
    pass

def GamesIn_Progress():
    global GameStart_Time, GameEnd_Time, DrawTime_Data
    GameEnd_Time = time.time()
    Temp_Text = str(int(GameEnd_Time - GameStart_Time))
    if ( len(Temp_Text) >= 2):
        if( int(GameEnd_Time - GameStart_Time) >= int(60) ):
            Temp_Cir = int(int(GameEnd_Time - GameStart_Time)/int(60))
            Temp_Text2 = str(int(round(GameEnd_Time - GameStart_Time, 2) - int(60*Temp_Cir)))
            if( len(Temp_Text2) == 1 ):
                DrawTime_Data = "0" + str(Temp_Cir) + ":0" + str(round(round(GameEnd_Time - GameStart_Time, 2) - int(60*Temp_Cir),2))
            else:
                DrawTime_Data = "0" + str(Temp_Cir) + ":" + str(round(round(GameEnd_Time - GameStart_Time, 2) - int(60*Temp_Cir),2))
        else:
            DrawTime_Data = "00:" + str(round(GameEnd_Time - GameStart_Time, 2))
    else:
        DrawTime_Data = "00:0" + str(round(GameEnd_Time - GameStart_Time, 2))
        pass
    DrawTime_Data = DrawTime_Data.replace(".", ":")
    DrawTime_Data  = "Time : " + str(DrawTime_Data)
    pass

def GamesDraw_Score():
    global Game_Score
    if( len(str(Game_Score)) == 1 ):
        Game_Score = "00000" +str(Game_Score)
    elif( len(str(Game_Score)) == 2 ):
        Game_Score = "0000" +str(Game_Score)
    elif( len(str(Game_Score)) == 3 ):
        Game_Score = "000" +str(Game_Score)
    elif( len(str(Game_Score)) == 4 ):
        Game_Score = "00" +str(Game_Score)
    elif( len(str(Game_Score)) == 5 ):
        Game_Score = "0" +str(Game_Score)
    elif( len(str(Game_Score)) == 6 ):
        Game_Score = "" +str(Game_Score)
    elif( len(str(Game_Score)) == 7 ):
        Game_Score = str(Game_Score)
    pass

def Game_Over():
    global Rabbit_Y, Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount
    global Game_Map, Game_MapCheck, GameCreated_Line, GameOver_Sound, Stage_Sound
    if ( Rabbit_Y <= 0):
        GameOver_Sound.play()
        Stage_Sound.set_volume(0)
        #Stage_Sound.__del__()
        Stage_Sound = None
        Rabbit_Y ,Rabbit_X, Rabbit_UpDownDirection, RabbitJump_LimitCount, Rabbit_Jet = 100, 100, "Up", 0, False
        Game_Map, Game_MapCheck, GameCreated_Line = GameMap_Reset(GameMap_Col, GameMap_Row, Game_Map, Game_MapCheck)
        GetGameOver_Data(GAME_Scenes, Game_Score, DrawTime_Data)
        GameUpdate_Menu("Game_Over")
        game_framework.change_state(game_over)
    pass

def exit():
    global GameLoad_BackGround, GameLoad_Menu, Load_Rabbit, Load_Footrest
    del(GameLoad_BackGround)
    del(GameLoad_Menu)
    del(Load_Rabbit)
    del(Load_Footrest)
    print("Unload : game_main.py Code")
    pass