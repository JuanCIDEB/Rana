import pygame as pg

import pygame.sprite

WIDTH = 640
HEIGHT = 480
TIMECLICK = 0
# currenttime = 0
# currenttime = pygame.time.get_ticks()
CURSOR_SIZE = 70
FLY_SIZE = 50

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
bg_img = pg.image.load('resources/backgrounds/background.png')
bg_img = pg.transform.scale(bg_img, (WIDTH, HEIGHT))

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
    # This pygame.Rect has the dimensions of the screen and
    # is used to clamp the player_rect to this area.
    screen_rect = screen.get_rect()
    speed = 7.5

    while True:
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
        if pressed[pg.K_SPACE]:  # and has_clicked:
            cursor = pg.image.load('resources/creatures/other/cursorCLICK.png')
            cursor = pg.transform.scale(cursor, (CURSOR_SIZE, CURSOR_SIZE))
            pg.mixer.music.load('resources/audio/FXclick.wav')
            pg.mixer.music.play(2)  #loops-1 en parentesis para que se repita infinitamente

        else:
            cursor = pg.image.load('resources/creatures/other/cursorNORM.png')
            cursor = pg.transform.scale(cursor, (CURSOR_SIZE, CURSOR_SIZE))

        # Clamp the rect to the dimensions of the screen_rect.
        player_rect.clamp_ip(screen_rect)
        bg_img = pg.image.load('resources/backgrounds/background.png')
        bg_img = pg.transform.scale(bg_img, (WIDTH, HEIGHT))
        screen.blit(bg_img, (0, 0))
        screen.blit(cursor, player_rect)

        # Update
        all_sprites.update()

        # Draw/render
        pg.display.flip()
        all_sprites.draw(screen)
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()
