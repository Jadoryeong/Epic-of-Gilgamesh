import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Epic of Gilgamesh") # 게임 이름

# FPS
clock = pygame.time.Clock()

Gilgamesh_hp = 100
Gilgamesh_ack = 10
Enkidu_hp = 110
Enkidu_ack = 11

# 배경 이미지 불러오기
start_screen = pygame.image.load("start screen.png")
clay_tablet = pygame.image.load("clay_tablet.png")
background = pygame.image.load("background.png")
Enkidu = pygame.image.load("Enkidu.png")
battle_help = pygame.image.load("help.png")
battle = pygame.image.load("battle.png")

# 색깔 결정
White = (255, 255,255)
Black = (0, 0, 0)

#  텍스트 출력 함수
def draw_text(text, size, color, x, y):
    font = pygame.font.Font("Ansungtangmyun-Bold.ttf", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# 화면 전환
screen_mode = 0
def game_screen(self):
    if screen_mode == 0:
        screen.blit(start_screen, (0, 0)) # 배경 그리기
        draw_text('시작하려면 SPACE를 눌러주세요', 30, White, 240, 450) # 텍스트 출력
    if screen_mode == 1:
        screen.blit(clay_tablet, (0,0))
        draw_text('홍수를 일으키던 신의 노여움도 잊혀지고', 25, White, 240, 150)
        draw_text('신의 온정이 홍수속에 묻혀버린', 25, White, 240, 200)
        draw_text('그리고 그런것들에 아무도 신경쓰지 않는', 25, White, 240, 250)
        draw_text('영생이 전설이 된 시대에', 25, White, 240, 300)
        draw_text('한 남자가 왕좌에 앉아있었다', 25, White, 240, 370)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, White, 240, 500)
    if screen_mode == 2:
        screen.blit(clay_tablet, (0,0))
        draw_text('우르크의 선왕과 들소의 여신 사이에서', 25, White, 240, 200)
        draw_text('태어나 건장한 체격과 통찰력,', 25, White, 240, 250)
        draw_text('용맹함, 아름다움을 지니고 있던 강력한 왕은', 25, White, 240, 300)
        draw_text('백성들의 고됨을 이해하지 못했다', 25, White, 240, 350)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, White, 240, 500)
    if screen_mode == 3:
        screen.blit(background, (0,0))
        draw_text('???', 20, Black, 240, 470)
        draw_text('고작 이만큼 일 한 것으로 지치다니', 20, Black, 240, 500)
        draw_text('어찌이리도 나약하단 말인가', 20, Black, 240, 530)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 4:
        screen.blit(background, (0,0))
        draw_text('???', 20, Black, 240, 470)
        draw_text('이리하여서 언제 이 일들을 끝마칠 것인가?!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 5:
        screen.blit(background, (0,0))
        draw_text('신하', 20, Black, 240, 470)
        draw_text('전하 지금 이들이 사흘 밤낮으로 일하여 지쳤습니다', 20, Black, 240, 500)
        draw_text('이들을 쉬게 하는것이 어떠신지...', 20, Black, 240, 530)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 6:
        screen.blit(background, (0,0))
        draw_text('???', 20, Black, 240, 470)
        draw_text('나약하긴.. 잠시 쉬고 다시 일들을 시작하거라', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 6:
        screen.blit(background, (0,0))
        draw_text('일꾼', 20, Black, 240, 470)
        draw_text('휴... 며칠만의 휴식인지...', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)   
    if screen_mode == 7:
        screen.blit(background, (0,0))
        draw_text('일꾼', 20, Black, 240, 470)
        draw_text('아무리 왕이라 하더라도 이렇게 일을 시키다니', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 8:
        screen.blit(background, (0,0))
        draw_text('그의 이름은 길가메쉬 우루투의 왕이며', 20, Black, 240, 475)
        draw_text('신이 현세에서 세력을 거뒀음에도 반인반신으로', 20, Black, 240, 505)
        draw_text('신의 축복을 받은 자이다', 20, Black, 240, 535)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 9:
        screen.blit(background, (0,0))       
        draw_text('신의 축복을 받은 그에게 대적할 자는 없었기에', 20, Black, 240, 490)
        draw_text('그는 오만하고 방탕하였다', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 10:
        screen.blit(background, (0,0))       
        draw_text('길가메쉬에 대한 탄식이 신들에게까지 들리자', 20, Black, 240, 490)
        draw_text('신들은 그를 바른길로 이끌 존재를 내려보낸다', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 11:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('이만큼 쉬었으면 충분하지 않느냐', 20, Black, 240, 500)
        draw_text('어찌 이리도 나태하게 구는 것이냐!', 20, Black, 240, 530)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 12:
        screen.blit(background, (0,0))
        draw_text('???', 20, Black, 240, 470)
        draw_text('지금당장 악행을 멈춰라 길가메쉬!!!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 13:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('감히 나에게 명령한 자가 누구냐!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 14:
        screen.blit(background, (0,0))
        draw_text('엔키두', 20, Black, 240, 470)
        draw_text('내 이름은 엔키두 그대를 바른길로 이끌 신의 사자다!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 15:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('아.....', 20, Black, 240, 495)
        draw_text('(어째서 내 나라에 저런 생명체가 존재하는 것이지?)', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 16:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('지중해의 미궁에 갇힌 괴수같은 모습을 하곤', 20, Black, 240, 495)
        draw_text('신의 사자를 자칭하다니 감히 나를 능욕하는 것이냐?', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)    
    if screen_mode == 17:
        screen.blit(background, (0,0))
        draw_text('엔키두', 20, Black, 240, 470)
        draw_text('무슨 소리를 하는 것인지 모르겠지만 아무래도', 20, Black, 240, 500)
        draw_text('자네와는 몸의 대화가 필요할 것 같군!', 20, Black, 240, 530)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 18:
        screen.blit(Enkidu, (0,0))
        draw_text('엔키두', 20, Black, 240, 470)
        draw_text('흠!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 19:
        screen.blit(Enkidu, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('(옷..옷이! 저딴게 도대체 왜 존재하는 것이냐!!!!)', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 20:
        screen.blit(battle_help, (0,0))
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 21:
        screen.blit(battle, (0,0)) # 전투
        draw_text('어떻게든 여기 부분을 구현을 해 볼려고 했는데', 18, Black, 240, 250)
        draw_text('더 이상 제출을 미루는 건 안 될거 같아서', 18, Black, 240, 270)
        draw_text('전투 부분만 제외하고 만들어진 반쪽짜리가 만들어졌네요..', 18, Black, 240, 290)
        draw_text('시간이 더 있다면 더 해볼텐데 아쉽네요...', 18, Black, 240, 310)
        draw_text('연휴 잘 보내시고 방학 끝나고 뵈요', 18, Black, 240, 330)
    if screen_mode == 22:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('나를 이렇게나 밀어붙이다니!', 20, Black, 240, 495)
        draw_text('신의 사자라는 것이 허풍이 아니였나 보군', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)            
    if screen_mode == 23:
        screen.blit(background, (0,0))
        draw_text('엔키두', 20, Black, 240, 470)
        draw_text('나는 그대를 바른 길로 이끌기 위한 존재니까! 하하', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 24:
        screen.blit(background, (0,0))
        draw_text('길가메쉬', 20, Black, 240, 470)
        draw_text('그대의 호탕함이 마음에 들었다!', 20, Black, 240, 500)
        draw_text('엔키두라고 했나? 너 내 동료가 되어라!', 20, Black, 240, 530)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 25:
        screen.blit(background, (0,0))
        draw_text('엔키두', 20, Black, 240, 470)
        draw_text('나도 그대가 마음에 들었다! 좋다!!', 20, Black, 240, 507)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 26:
        screen.blit(background, (0,0))
        draw_text('그들은 싸우면서 친해진다는 말을 입증하듯', 20, Black, 240, 490)
        draw_text('서로를 인정하고 우정을 맹세하게 되었다', 20, Black, 240, 520)
        draw_text('계속하려면 SPACE를 눌러주세요', 20, Black, 240, 600)
    if screen_mode == 27:
        screen.blit(background, (0,0))
        draw_text('Act 1 End', 20, Black, 240, 505)
    if screen_mode == 28:
        screen.blit(background, (0,0))

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 실행 종료
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                screen_mode += 1
            if screen_mode >= 28 and event.key == pygame.K_0:
                LOL = pygame.image.load("LOL.png")
                screen.blit(LOL, (0,0))
            
    game_screen(screen_mode)

    pygame.display.update() # !!게임화면을 다시 그리기!!

# pygame 종료
pygame.quit()