import pygame
pygame.init()

screen = pygame.display.set_mode((1080, 720))
screen.fill((50,50,50))
info = pygame.display.Info()
width = info.current_w
height = info.current_h

choix1 = "Choix numéro 1"
choix2 = "Choix numéro 2"
choix3 = "Choix numéro 3"

nbchoix = 3

while True:    
    font = pygame.font.SysFont('Helvetica', 22, bold=True)
    choice = True
    i = 0
    while choice:
        pygame.display.flip()
        if i < 3:
            for tt in range(3):
                pygame.draw.rect(screen, (100, 5, 5), (tt*width/3+10, height-110, width/3-20, 100))
                if tt == 0:
                    TEXT=choix1
                if tt == 1 and nbchoix == 3:
                    TEXT=choix2
                if tt == 1 and nbchoix == 2:
                    TEXT=""
                if tt == 2 and nbchoix == 3:
                    TEXT=choix3
                if tt == 2 and nbchoix == 2:
                    TEXT=choix2
                button_text = font.render(TEXT, True, (255, 255, 255))
                screen.blit(button_text, (tt*width/3+20, height-100))
                i+=1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.quit:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1 \
                or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 0*width/3+10 and pygame.mouse.get_pos()[0] < (0*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                pygame.draw.rect(screen, (255,255,255), (0*width/3+8, height-113, width/3-16, 106), 6)
                choice = False
                break
            if nbchoix == 2:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                    pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                    choice = False
                    break
            if nbchoix == 3:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1*width/3+10 and pygame.mouse.get_pos()[0] < (1*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                    pygame.draw.rect(screen, (255,255,255), (1*width/3+8, height-113, width/3-16, 106), 6)
                    choice = False
                    break
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c or event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                    pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                    choice = False
                    break