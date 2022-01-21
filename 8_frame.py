import pygame
####################################################################
#기본 초기화 (반드시 해야하는 것들)
from pygame.constants import KEYDOWN

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("game") #게임 이름

#FPS
clock = pygame.time.Clock()


####################################################################

#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

running = True #게임이 진행 중인가 
while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수를 설정

#캐릭터가 100만큼 이동해야 함
#10 fps : 1초 동안에 10번 동작 -> 한번에 10만큼 이동 10*10 = 100
#20 fps : 1초 동안에 20번 동작 -> 한번에 5만큼 5*20 =100 


    # 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    # 3.게임 캐릭터 위치 정의
    
  
    # 4.충돌 처리

    # 5.화면에 그리기
   
    pygame.display.update() #게임 화면을 다시 그리기


#pygame 종료
pygame.quit()