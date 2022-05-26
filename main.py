import pygame as pg

import pygame.sprite

WIDTH = 640
HEIGHT = 480
TIMECLICK = 0
# currenttime = 0
# currenttime = pygame.time.get_ticks()
CURSOR_SIZE = 70

FLY_SIZE = 50
TOUNGE_COLOR= (255, 156, 122)
TOUNGE_COLOR_W= (255,255,255)
TOUNGE_COLOR_B= (0,68,19)
TOUNGE_WIDTH = 9
TOUNGE_START = (WIDTH-317, HEIGHT-130)


SPACE_CLICKED = True
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        self.enemy_fly1_surf = pygame.image.load('resources/creatures/enemies/emboscadademoscas.png')
        self.image = pg.Surface((50, 50))
        self.image = pg.transform.scale(self.image, (FLY_SIZE, FLY_SIZE))


class Cursor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.image = pg.transform.scale(self.image, (CURSOR_SIZE, CURSOR_SIZE))


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))






all_sprites = pg.sprite.Group()
cursor = Cursor()
all_sprites.add(cursor)


def current_time():
    current_time = pg.time.get_ticks()
    return current_time


def has_clicked():
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                return True


def main():
    clock = pg.time.Clock()
    cursor = pg.image.load('resources/creatures/other/cursorNORM.png')
    cursorclick = pg.image.load('resources/creatures/other/cursorCLICK.png')
    cursor = pg.transform.scale(cursor, (CURSOR_SIZE, CURSOR_SIZE))

    player_rect = cursor.get_rect(topleft=(300, 200))
    screen_rect = screen.get_rect()
    speed = 7.5


    while True:
        SPACE_CLICKED = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pressed = pg.key.get_pressed()
        if pressed[pg.K_w]:
            player_rect.y -= speed
        if pressed[pg.K_s]:
            player_rect.y += speed
        if pressed[pg.K_a]:
            player_rect.x -= speed
        if pressed[pg.K_d]:
            player_rect.x += speed
        if pressed[pg.K_SPACE] and SPACE_CLICKED:  # and has_clicked:
            cursor = pg.image.load('resources/creatures/other/cursorCLICK.png')
            cursor = pg.transform.scale(cursor, (CURSOR_SIZE, CURSOR_SIZE))
            pg.mixer.music.load('resources/audio/FXclick.wav')
            pg.mixer.music.set_volume(0.1)
            pg.mixer.music.play(1)  #loops-1 en parentesis para que se repita infinitamente
            cursor_pressed = True
            SPACE_CLICKED = False

        else:
            cursor = pg.image.load('resources/creatures/other/cursorNORM.png')
            cursor = pg.transform.scale(cursor, (CURSOR_SIZE, CURSOR_SIZE))
            cursor_pressed = False

        # Clamp the rect to the dimensions of the screen_rect.
        player_rect.clamp_ip(screen_rect)
        bg_img = pg.image.load('resources/backgrounds/background.png')
        bg_img = pg.transform.scale(bg_img, (WIDTH, HEIGHT))
        frog_img = pg.image.load('resources/creatures/frog/rana.png')
        frog_img = pg.transform.scale(frog_img, (WIDTH/5.5, HEIGHT/5))
        fly_img = pg.image.load('resources/creatures/enemies/emboscadademoscas.png')
        fly_img = pg.transform.scale(fly_img, (WIDTH / 14, HEIGHT / 19))
        pg.display.set_icon(frog_img)
        screen.blit(bg_img, (0, 0))
        screen.blit(frog_img, (WIDTH-375, HEIGHT-135))
        screen.blit(fly_img, (WIDTH/2.1, HEIGHT/16))
        if cursor_pressed:
            pg.draw.line(screen, TOUNGE_COLOR_W, (TOUNGE_START), (player_rect.x + 35, player_rect.y + 40), TOUNGE_WIDTH+6)
            pg.draw.line(screen, TOUNGE_COLOR_B, (TOUNGE_START), (player_rect.x + 35, player_rect.y + 40),
                         TOUNGE_WIDTH + 4)
            pg.draw.line(screen, TOUNGE_COLOR, (TOUNGE_START), (player_rect.x + 35, player_rect.y + 40), TOUNGE_WIDTH)
        screen.blit(cursor, player_rect)
        print(player_rect.x, player_rect.y)


        # Update
        all_sprites.update()

        # Draw/render
        pg.display.flip()
        all_sprites.draw(screen)
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()
