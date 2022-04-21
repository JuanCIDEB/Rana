
import pygame
from sys import exit

#CONSTANTES
pygame.init()  #inicializa pygames
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
CENTER = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2  #es divicion pero lo convierte a int
SNAIL_SPEED = 79
INV_FRAMES = 40
inv_counter = INV_FRAMES
inv_flag = False
print("Hola soy Leonardo")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("El juego de rana sin nombre")
clock= pygame.time.Clock()
font = pygame.font.Font('resources/fonts/32bit Regular.ttf', 100)
text_surf = font.render('Queso', False, 'White')  #False para  antialiasing

while True:
    #Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
