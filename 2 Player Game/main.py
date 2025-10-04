import pygame
pygame.font.init()


WIDTH = 1300
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("2 Player Game")

w_wiz = 300
h_wiz = 400

w_wic = 300
h_wic = 400

game_over = False


wizard = pygame.image.load("images/wizard.png")
witch = pygame.image.load("images/witch.png")
arena = pygame.image.load("images/empty-ancient-gladiator-arena-game-260nw-2307454813.webp")

wizard = pygame.transform.scale(wizard, (w_wiz, h_wiz))
witch = pygame.transform.scale(witch, (w_wic, h_wic))
arena = pygame.transform.scale(arena, (WIDTH, HEIGHT+200) )

clock = pygame.time.Clock()

divider = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

health_font = pygame.font.SysFont("Calibri", 25)

speed = 4


# Modulization of code
def create_setting(wiz_rect, wic_rect, witch_bullets, wizard_bullets, witch_health, wizard_health):
    screen.blit(arena, (0,0))
    pygame.draw.rect(screen, (0,0,0), divider)
    screen.blit(wizard, (wiz_rect.x, wiz_rect.y))
    screen.blit(witch, (wic_rect.x, wic_rect.y))
    wic_health_text = health_font.render(f"Witch Health: {witch_health}", 1, (0,0,0))
    wiz_health_text = health_font.render(f"Wizard Health: {wizard_health}", 1, (0,0,0))
    screen.blit(wiz_health_text, (125, 50))
    screen.blit(wic_health_text, (900, 50))
    pygame.display.update()


    


def main():
    global game_over
    wiz_rect = pygame.Rect(0,500, w_wiz, h_wiz )
    wic_rect = pygame.Rect(1000, 500, w_wic, h_wic)

    witch_bullets = []
    wizard_bullets = []

    witch_health = 10
    wizard_health = 10
    
    while not game_over:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
        

        keys_pressed = pygame.key.get_pressed()


        create_setting(wiz_rect, wic_rect, witch_bullets, wizard_bullets, witch_health, wizard_health)
        wiz_movements(keys_pressed, wiz_rect)
        wic_movement(keys_pressed, wic_rect)




def wiz_movements(keys_pressed, wiz_rect):
    if keys_pressed[pygame.K_a] and wiz_rect.x - speed > 0:
        wiz_rect.x -= speed
    
    elif keys_pressed[pygame.K_d] and wiz_rect.x + speed < divider.x:
        wiz_rect.x += speed
    
    elif keys_pressed[pygame.K_w] and wiz_rect.y -speed > 0:
        wiz_rect.y -= speed
    
    elif keys_pressed[pygame.K_s] and wiz_rect.y -speed < HEIGHT:
        wiz_rect.y += speed


def wic_movement(keys_pressed, wic_rect):
    if keys_pressed[pygame.K_LEFT] and wic_rect.x - speed > divider.x + 10:
        wic_rect.x -= speed

    elif keys_pressed[pygame.K_RIGHT] and wic_rect.x - speed  + 10:
        wic_rect.x -= speed






main()



