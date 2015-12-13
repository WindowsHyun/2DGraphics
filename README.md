#2DGraphics TermProject [Cragene Rabbit]

+ 2012180004 권창현
+ Project 주간 B반
+ [프로젝트 업로드 주소](http://www.daehyunlee.com/dustinlee_new/doku.php?id=studentaccess:2015:02:2dgp:project_b)
+ [강의계획서](http://www.daehyunlee.com/dustinlee_new/lib/exe/fetch.php?media=lecture:2015:02:2dgameprogramming:2015_fall_2dgp_syllabus.pdf)

============
###GitHub Clone in Desktop

+ [GitHub Desktop 설치 & 사용방법](https://www.youtube.com/watch?v=fJqGGQIf4dk)

============
###Youtube 업로드 영상 & PPT 자료
+ [1차 발표 PPT](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/ProjectPPT/KwonChangHyun_1%EC%B0%A8%EB%B0%9C%ED%91%9C.pptx?raw=true) / [1차 발표 영상](https://www.youtube.com/watch?v=wmc25937s1s)
+ [2차 발표 PPT](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/ProjectPPT/KwonChangHyun_2%EC%B0%A8%EB%B0%9C%ED%91%9C.pptx?raw=true) / [2차 발표 영상](https://youtu.be/9CV9dXPFsC0)
+ [3차 발표 PPT](https://github.com/WindowsHyun/2DGraphics/blob/b9627407e56c46c6a0ffc0531442e25db1219758/Document/ProjectPPT/2015_2dgp_3%EC%B0%A8%EB%B0%9C%ED%91%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pptx?raw=true) / [3차 발표 영상](https://www.youtube.com/watch?v=GPo1HAbMvxE)

============
###프로젝트 일정.
+ 1주차 (09/23) 전체적인 맵 틀 및 게임 스토리 구성

  > 1. 백그라운드 맵 이미지 구상
  > 1. 게임시작시 어떻게 해야할지 구상
  > 1. 게임오버시 어떻게 해야할지 구상
  > 1. 게임 스코어를 어떻게 계산할지 구상
  > 1. 게임 스코어를 어떻게 저장하고 기록할지 구상
  > 1. 게임 난이도에 대한 구상
  > 1. 추석 연휴 조금만 하자..!
  > 1. [1주차 구상한 내용 정리 파일](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/TermProjectConcept/ConceptDATA_1%EC%A3%BC%EC%B0%A8.txt)
+ 2주차 (09/30) 리소스 및 사운드 와 알고리즘 계산

  > 1. 메인 이미지 (토끼 관련한 좌우 점프 이미지) 수집
  > 1. 함정 이미지 ( 중간중간 랜덤으로 출연할 함정) 수집
  > 1. 발판 이미지 (토끼가 밟고 올라갈수 있는 발판) 수집
  > 1. 사운드 (점프, 게임오버 등등...) 수집
  > 1. 백그라운드 이미지 적용 및 3주차 백그라운드 계속 올라가는 느낌 계산
  > 1. 발판 생성을 위한 알고리즘 계산
  
  > > + 발판을 어떻게 생성을 할것인가?
  > > + 발판을 생성할 위치는 어떻게 할것인가?
  > > + 발판에 대한 충돌체크를 대비하여 어떻게 생성을 할것인가?
  > > + 랜덤으로 생성할시 랜덤적으로 생성이 안되고 동일하게 생성되면 어떻게 할것인가?
  > > + 발판의 거리는 어떻게 조절을 할것인가?
  > > + 난이도에 따라 발판을 조절한다 하였는데, 그 조절을 어떻게 할것인가?
  > > + 발판이 생성된 이후 사라지는 방법은 어떻게 구현할 것인가?
  > > + 발판을 얼마만큼의 가로, 세로 크기로 만들것인가?
  > > + 발판을 밟을시 일괄적으로 왼쪽으로 움직이는 방법은 어떻게 구현할 것인가?
  > > + 발판이 시간에 따라서 있다가 사라졌다가 하는 방법은 어떻게 구현할 것인가?
  > > + 발판이 한번만 밟으면 사라지고 없어지는 방법은 어떻게 구현할 것인가?
  > > + [2주차 질문에 대한 내용 정리 파일](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/TermProjectConcept/ConceptDATA_2%EC%A3%BC%EC%B0%A8.txt)
+ 3주차 (10/07) 난이도 조절 관련 메뉴 및 시작 페이지 구성

  > 1. Gameframework 적용하여 시작 페이지 구성
  > 1. class_data.py global 함수등으로 불러오지 말고 return 하는 방식으로 클래스 구현
  > 1. 1번이 완료시 py 파일 이름을 조금더 직관적이에 수정하자
+ 4주차 (10/14) 캐릭터 애니메이션 구현 

  > 1. 캐릭터 좌/우 이동 추가및 이동에 따른 애니메이션 구현
  > 1. 캐릭터가 좌/우 끝으로 이동시 반대편으로 나오게 구현
  > 1. 캐릭터 점프 하는 애니메이션 구현.
+ 5주차 (10/21) 프로젝트 2차 발표를 위한 정리.

  > 1. PPT 작성
  > 1. GitHub 커밋
  > 1. PPT 발표 동영상 찍기
+ 6주차 (10/28) 발판 등 의 생성 부분 알고리즘 추가

  > 1. 발판을 생성하기 위하여 22*30 배열을 잡아서 초기화를 해주자.
  > 1. 게임 맵이 Easy, Mid, Hard 3가지인데, game_ing에서 어떻게 확인을 해줄지 생각하자.
  > 1. 발판을 최대 몇개까지 화면에 넣을수 있을까?
  > 1. 발판 알고리즘을 game_ing에 작성할까 class_data에 작성을 할까?
  > 1. 발판의 종류를 몇개 까지 추가를 할까?
  > 1. 발판 말고도 다른 함정들은 어떻게 추가를 해야할까?
  > 1. [6주차 구상한 내용 정리 파일](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/TermProjectConcept/ConceptDATA_6%EC%A3%BC%EC%B0%A8.txt)
+ 7주차 (11/04) 발판과 캐릭터의 충돌 체크 작업

  > 1. 캐릭터의 X 좌표와 발판의 X 좌표를 비교를 하자.
  > 1. 발판이 정확하게 충돌했는지 어떻게 구별할껀가?
  > 1. 각각의 발판마다 기능이 다른데 어떻게 설정을 할까?
  > 1. 코드가 엄청 길어질꺼 같은데 어떻게 하면 코드를 줄이면서 간략하게 할수 있을까?
  > 1. class_data에 무조건 클래스를 다 넣을 필요가 있을까?
  > 1. 변수명, 클래스명 정리를 하자.
  > 1. 좀 더 직관적으로 알아볼 수 있게 코드를 수정하자.
  > 1. Json 을 어디에 활용할지 생각을 해보자..!
  > 1. [7주차 구상한 내용 정리 파일](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/TermProjectConcept/ConceptDATA_7%EC%A3%BC%EC%B0%A8.txt)
+ 8주차 (11/11) 발판을 올라가면서 점수 체크 기능 작업

  > 1. 발판 한번 밟을때마다의 점수를 어떻게 줄것인가?
  > 1. 발판을 중복으로 밟을시 점수를 어떻게 줄것인가?
  > 1. 난이도에 따라 점수를 다르게 줄것인가?
  > 1. 점수 말고 흘러가는 시간은 어떻게 표현할 것인가?
  > 1. 게임이 끝나고 나서 어떻게 처리를 할것인가?
  > 1. 스코어 기능이 있는데 스코어는 어떻게 등록을 할것인가?
  > 1. 스코어는 어떻게 불러올것인가?
  > 1. Json 데이터를 더이상 수정할일이 없는데 어떻게 할것인가?
  > 1. 게임오버시 표시이후 어떠한 메뉴를 넣을것인가?
  > 1. 컴퓨터 마다 올라가거나, 이동하는 속도가 다른데 어떻게 처리할것인가?
  > 1. 스코어 데이터가 파일로 저장이 되는데, 다른사람이 수정을 어떻게 방지할것인가?
  > 1. json 데이터가 파일로 저장이 되어있는데, 다른사람이 수정을 어떻게 방지할것인가?
  > 1. pyc 파일이 계속 생성되는데, 줄일 수 있는 방법이 없을까?
  > 1. 중력가속도 설정하는 공식을 알아도 적용을 못하겠다... 어떻게 방법이 없을까?
  > 1. 그 외 추가할만한 기능이 뭐가 있을까?
  > 1. [8주차 구상한 내용 정리 파일](https://github.com/WindowsHyun/2DGraphics/blob/master/Document/TermProjectConcept/ConceptDATA_8%EC%A3%BC%EC%B0%A8.txt)
+ 9주차 (11/18) 프로젝트 3차 발표를 위한 정리.

  > 1. 사운드 기능 추가
  > 1. 발표를 위한 ppt 혹은 깃허브 커밋 정리
  > 1. 게임 시연중 오류가 있는지 확인.
  > 1. 게임 시연이 가능할정도로 게임 완성하기.
+ 10주차 (11/25) 전체적인 완성도 + 디버깅 + 오류검사
  > 1. 게임에서 절대 깨지 못할 발판 생성 방지
  > 1. 일부 함정 발판 생성
  > 1. 치트 삭제
+ 11주차 (12/02) 프로젝트 최종 발표를 위한 정리.
  > 1. install 가이드에 따라 exe 파일 제작 및 설치파일 제작
  > 1. 발표 영상 작성 및 마지막 발표 ppt 제작
  > 1. Github 최종 정리
  > 1. 게임 제작 완료..!
