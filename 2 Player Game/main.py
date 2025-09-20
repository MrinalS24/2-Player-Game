import pygame

WIDTH = 1300
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("2 Player Game")

w_wiz = 300
h_wiz = 400

w_wic = 300
h_wic = 400


wizard = pygame.image.load("images/wizard.png")
witch = pygame.image.load("images/witch.png")

wizard = pygame.transform.scale(wizard, (w_wiz, h_wiz))
witch = pygame.transform.scale(witch, (w_wic, h_wic))

# Modulization of code
def create_setting():
    pass


def main():
    wiz_rect = pygame.Rect(0,500, w_wiz, h_wiz )
    wic_rect = pygame.Rect(1300, 500, w_wic, h_wic)


